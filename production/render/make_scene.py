#!/usr/bin/env python3
"""Render one Template-v2 scene frame (oversized for zoompan) as a PNG."""
import sys, json
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = FONT_DIR + "/DejaVuSans-Bold.ttf"

W, H = 1300, 2310  # oversized canvas; zoompan crops down to 1080x1920 while panning/zooming
ASSETS = "/home/claude/dailyfaktor-media/production/assets"

def gradient_bg(glow1, glow2, base=(21, 14, 38)):
    base = np.array(base, dtype=np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    def glow(cx, cy, radius, color):
        d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
        t = np.clip(1 - d / radius, 0, 1) ** 1.5
        return t[..., None] * (np.array(color, dtype=np.float32) - base)[None, None, :]
    bg = np.tile(base, (H, W, 1))
    bg += glow(*glow1)
    bg += glow(*glow2)
    bg = np.clip(bg, 0, 255).astype(np.uint8)
    return Image.fromarray(bg, mode="RGB").convert("RGBA")

def tight_crop(im, pad=8):
    arr = np.array(im)
    mask = arr[..., 3] > 20
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return im
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
    x1, y1 = min(im.width, x1 + pad), min(im.height, y1 + pad)
    return im.crop((x0, y0, x1, y1))

def load_asset(name):
    path = f"{ASSETS}/{name}"
    if not __import__("os").path.exists(path):
        path = f"{ASSETS}/icons/{name}"
    im = Image.open(path).convert("RGBA")
    return tight_crop(im)

def paste_scaled(canvas, im, target_w, cx, cy_top):
    scale = target_w / im.width
    im2 = im.resize((target_w, int(im.height * scale)), Image.LANCZOS)
    canvas.alpha_composite(im2, (int(cx - target_w / 2), int(cy_top)))
    return im2.height

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_centered_text(draw, text, font, cy, color, max_width, line_spacing=1.25, stroke=None, stroke_width=0):
    lines = wrap_text(draw, text, font, max_width)
    sizes = [draw.textbbox((0, 0), l, font=font) for l in lines]
    heights = [b[3] - b[1] for b in sizes]
    total_h = sum(heights) * line_spacing
    y = cy - total_h / 2
    for l, h in zip(lines, heights):
        bbox = draw.textbbox((0, 0), l, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) / 2
        if stroke:
            draw.text((x, y), l, font=font, fill=color, stroke_width=stroke_width, stroke_fill=stroke)
        else:
            draw.text((x, y), l, font=font, fill=color)
        y += h * line_spacing
    return y

def badge(draw, text, cy, fill=(236, 72, 153, 255), textcolor=(40, 10, 30, 255)):
    f = ImageFont.truetype(BOLD, 60)
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 55, 30
    bw, bh = tw + 2 * pad_x, th + 2 * pad_y
    bx = (W - bw) / 2
    draw.rounded_rectangle([bx, cy, bx + bw, cy + bh], radius=bh / 2, fill=fill)
    draw.text((bx + pad_x - bbox[0], cy + pad_y - bbox[1]), text, font=f, fill=textcolor)

def render(scene_cfg, out_path):
    bg = gradient_bg(scene_cfg["glow1"], scene_cfg["glow2"], scene_cfg.get("base", (21, 14, 38)))
    draw = ImageDraw.Draw(bg)
    char = load_asset("character_dr_wissen.png")

    kind = scene_cfg["kind"]
    if kind == "hook":
        badge(draw, "DR. WISSEN", 110)
        paste_scaled(bg, char, int(W * 0.5), W / 2, H * 0.30)
        f = ImageFont.truetype(BOLD, 78)
        draw_centered_text(draw, scene_cfg["text"], f, H * 0.78, (255, 255, 255, 255), W * 0.82,
                            stroke=(20, 8, 30, 255), stroke_width=4)
    elif kind == "term":
        for name, size, pos in scene_cfg["icons"]:
            ic = load_asset(name)
            paste_scaled(bg, ic, size, pos[0], pos[1])
        paste_scaled(bg, char, int(W * 0.30), W * 0.16, H * 0.80)
        f = ImageFont.truetype(BOLD, 92)
        draw_centered_text(draw, scene_cfg["text"], f, H * 0.22, (255, 255, 255, 255), W * 0.85,
                            stroke=(20, 8, 30, 255), stroke_width=5)
    elif kind == "explain":
        ic = load_asset(scene_cfg["icon"])
        paste_scaled(bg, ic, int(W * 0.95), W / 2, H * 0.30)
        paste_scaled(bg, char, int(W * 0.24), W * 0.84, H * 0.06)
        f = ImageFont.truetype(BOLD, 62)
        draw_centered_text(draw, scene_cfg["text"], f, H * 0.80, (255, 255, 255, 255), W * 0.85,
                            stroke=(20, 8, 30, 255), stroke_width=4)
    elif kind == "payoff":
        badge(draw, "DR. WISSEN", 110)
        paste_scaled(bg, char, int(W * 0.58), W / 2, H * 0.28)
        f = ImageFont.truetype(BOLD, 74)
        draw_centered_text(draw, scene_cfg["text"], f, H * 0.80, (255, 255, 255, 255), W * 0.82,
                            stroke=(20, 8, 30, 255), stroke_width=4)
    elif kind == "outro":
        paste_scaled(bg, char, int(W * 0.34), W / 2, H * 0.33)
        f1 = ImageFont.truetype(BOLD, 72)
        f2 = ImageFont.truetype(BOLD, 52)
        draw_centered_text(draw, "FOLGE @DAILYFAKTOR", f1, H * 0.63, (255, 255, 255, 255), W * 0.9)
        draw_centered_text(draw, "Morgen: neuer Fakt", f2, H * 0.70, (255, 230, 240, 255), W * 0.9)

    bg.convert("RGB").save(out_path, quality=95)

if __name__ == "__main__":
    cfg = json.loads(sys.argv[1])
    render(cfg, sys.argv[2])
