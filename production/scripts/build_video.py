#!/usr/bin/env python3
import os, sys, json, subprocess, math, random

ROOT = "/home/claude/dailyfaktor-media"
IMG = os.path.join(ROOT, "production/assets/images_rgba")
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1080, 1920
FPS = 30

from PIL import Image, ImageDraw, ImageFont, ImageFilter

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vgrad(size, top, bottom):
    im = Image.new("RGB", size, top)
    d = ImageDraw.Draw(im)
    h = size[1]
    for y in range(h):
        t = y / h
        d.line([(0,y),(size[0],y)], fill=lerp(top,bottom,t))
    return im

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_centered_text(im, text, font, fill, max_width, center_y, line_spacing=1.25, stroke_width=0, stroke_fill=None):
    d = ImageDraw.Draw(im)
    lines = wrap_text(d, text, font, max_width)
    sizes = [d.textbbox((0,0), l, font=font, stroke_width=stroke_width) for l in lines]
    heights = [s[3]-s[1] for s in sizes]
    total_h = sum(heights) * line_spacing
    y = center_y - total_h/2
    for l, hgt in zip(lines, heights):
        bbox = d.textbbox((0,0), l, font=font, stroke_width=stroke_width)
        w = bbox[2]-bbox[0]
        x = (im.width - w)/2
        d.text((x, y), l, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)
        y += hgt * line_spacing
    return im

def rounded_badge(im, text, font, center_x, top_y, pad_x=36, pad_y=16, bg=(255,255,255,235), fg=(40,10,60)):
    d = ImageDraw.Draw(im)
    bbox = d.textbbox((0,0), text, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    box_w, box_h = tw + pad_x*2, th + pad_y*2
    x0 = center_x - box_w/2
    y0 = top_y
    d.rounded_rectangle([x0, y0, x0+box_w, y0+box_h], radius=box_h/2, fill=bg)
    d.text((center_x - tw/2, y0 + pad_y - bbox[1]), text, font=font, fill=fg)
    return y0 + box_h

def paste_icon(im, icon_path, target_w, center, rotate=0, flip=False, opacity=255):
    icon = Image.open(icon_path).convert("RGBA")
    ratio = target_w / icon.width
    icon = icon.resize((int(icon.width*ratio), int(icon.height*ratio)), Image.LANCZOS)
    if flip:
        icon = icon.transpose(Image.FLIP_LEFT_RIGHT)
    if rotate:
        icon = icon.rotate(rotate, expand=True, resample=Image.BICUBIC)
    if opacity < 255:
        a = icon.getchannel("A").point(lambda p: int(p*opacity/255))
        icon.putalpha(a)
    x = int(center[0] - icon.width/2)
    y = int(center[1] - icon.height/2)
    im.alpha_composite(icon.convert("RGBA"), (x, y))

def tiled_icon_bg(im, icon_path, scale=0.42, opacity=46, step_mul=1.35, jitter=0.0):
    icon = Image.open(icon_path).convert("RGBA")
    tw = int(im.width * scale)
    ratio = tw / icon.width
    icon = icon.resize((tw, int(icon.height*ratio)), Image.LANCZOS)
    a = icon.getchannel("A").point(lambda p: int(p*opacity/255))
    icon.putalpha(a)
    step_x = int(tw*step_mul)
    step_y = int(icon.height*step_mul)
    rnd = random.Random(42)
    for row, y in enumerate(range(-step_y, im.height+step_y, step_y)):
        offset = (step_x//2) if row % 2 else 0
        for x in range(-step_x, im.width+step_x, step_x):
            jx = x + offset + rnd.randint(-20,20)
            jy = y + rnd.randint(-15,15)
            im.alpha_composite(icon, (jx, jy))

def character(im, w, center, bbox_glow=None):
    paste_icon(im, os.path.join(IMG,"character.png"), w, center)

def base_canvas(top, bottom):
    bg = vgrad((W,H), top, bottom).convert("RGBA")
    return bg

PURPLE_DARK = (34,14,54)
PURPLE_MID = (64,24,92)
PURPLE_WARM = (92,30,86)
ORANGE_TOP = (255,150,60)
ORANGE_BOT = (235,70,70)
WHITE = (255,255,255,255)
BADGE_FG = (50,14,70)

def font(sz, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, sz)

def scene_hook(icon_a, icon_b, hook_text):
    im = base_canvas(PURPLE_DARK, PURPLE_MID)
    tiled_icon_bg(im, os.path.join(IMG, icon_a), scale=0.5, opacity=40)
    tiled_icon_bg(im, os.path.join(IMG, icon_b), scale=0.42, opacity=30, step_mul=1.6)
    rounded_badge(im, "DR. WISSEN", font(42), W/2, 110)
    character(im, 320, (W/2, 430))
    draw_centered_text(im, hook_text, font(78), WHITE, W-160, H*0.62, line_spacing=1.22,
                        stroke_width=4, stroke_fill=(20,5,30,255))
    return im

def scene_begriff(icon_main, begriff_text, char_corner=True):
    im = base_canvas(PURPLE_MID, PURPLE_DARK)
    paste_icon(im, os.path.join(IMG, icon_main), int(W*0.72), (W/2, H*0.44))
    if char_corner:
        character(im, 190, (170, H-230))
    rounded_badge(im, "DR. WISSEN", font(36), W/2, 56)
    draw_centered_text(im, begriff_text, font(84), WHITE, W-140, H*0.76, line_spacing=1.2,
                        stroke_width=5, stroke_fill=(20,5,30,255))
    return im

def scene_explain(icon_main, explain_text, char_corner=True, zoom_crop=True):
    im = base_canvas(PURPLE_DARK, PURPLE_WARM)
    icon = Image.open(os.path.join(IMG, icon_main)).convert("RGBA")
    tw = int(W*1.05)
    ratio = tw/icon.width
    icon = icon.resize((tw, int(icon.height*ratio)), Image.LANCZOS)
    if zoom_crop:
        cw, ch = icon.width, icon.height
        crop = icon.crop((int(cw*0.15), int(ch*0.1), int(cw*0.85), int(ch*0.9)))
        crop = crop.resize((tw, int(tw*crop.height/crop.width)), Image.LANCZOS)
        icon = crop
    x = int(W/2 - icon.width/2); y = int(H*0.30 - icon.height/2)
    im.alpha_composite(icon, (x,y))
    d = ImageDraw.Draw(im)
    cx, cy = W/2, H*0.30
    d.ellipse([cx-icon.width*0.33, cy-icon.height*0.33, cx+icon.width*0.33, cy+icon.height*0.33],
              outline=(255,255,255,160), width=6)
    if char_corner:
        character(im, 170, (W-140, H-200))
    draw_centered_text(im, explain_text, font(66), WHITE, W-150, H*0.70, line_spacing=1.25,
                        stroke_width=4, stroke_fill=(20,5,30,255))
    return im

def scene_payoff(warm_text):
    im = base_canvas(PURPLE_WARM, (120,40,70))
    character(im, 420, (W/2, 460))
    rounded_badge(im, "DR. WISSEN", font(42), W/2, 110)
    draw_centered_text(im, warm_text, font(72), WHITE, W-160, H*0.66, line_spacing=1.22,
                        stroke_width=4, stroke_fill=(20,5,30,255))
    return im

def scene_outro():
    im = base_canvas(ORANGE_TOP, ORANGE_BOT)
    character(im, 260, (W/2, H*0.38))
    draw_centered_text(im, "FOLGE @DAILYFAKTOR", font(68), WHITE, W-160, H*0.62, line_spacing=1.2,
                        stroke_width=4, stroke_fill=(90,20,10,255))
    draw_centered_text(im, "Morgen: neuer Fakt", font(46, bold=False), (255,255,255,230), W-160, H*0.72,
                        line_spacing=1.2)
    return im

def ffprobe_duration(path):
    out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                           "-of","default=noprint_wrappers=1:nokey=1", path],
                          capture_output=True, text=True).stdout.strip()
    return float(out)

def render_scene_video(png_path, out_path, duration, zoom_dir="in", audio_path=None):
    tmp = out_path + ".tmp.mp4"
    frames = int(round(duration*FPS))
    if zoom_dir == "in":
        zexpr = "min(zoom+0.0012,1.18)"
    elif zoom_dir == "out":
        zexpr = "if(eq(on,1),1.18,max(1.18-0.0012*on,1.0))"
    else:
        zexpr = "1.06"
    vf = (f"scale=1600:-1,zoompan=z='{zexpr}':d={frames}:s={W}x{H}:fps={FPS},"
          f"format=yuv420p")
    cmd = ["ffmpeg","-y","-loop","1","-i", png_path]
    if audio_path:
        cmd += ["-i", audio_path]
    cmd += ["-t", str(duration), "-vf", vf, "-r", str(FPS)]
    if audio_path:
        cmd += ["-c:v","libx264","-crf","18","-preset","veryfast","-c:a","aac","-b:a","160k",
                "-shortest","-map","0:v","-map","1:a"]
    else:
        cmd += ["-c:v","libx264","-crf","18","-preset","veryfast","-an"]
    cmd += [tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise RuntimeError(f"ffmpeg failed for {out_path}")
    os.replace(tmp, out_path)

def build_slot(tag, slot_name, category, hook_icon_a, hook_icon_b, begriff_text, explain_icon,
               audio_dir, out_name, outdir):
    os.makedirs(outdir, exist_ok=True)
    a_hook = os.path.join(audio_dir, f"{slot_name}_1hook.mp3")
    a_cur = os.path.join(audio_dir, f"{slot_name}_2curious.mp3")
    a_calm = os.path.join(audio_dir, f"{slot_name}_3calm.mp3")
    a_warm = os.path.join(audio_dir, f"{slot_name}_4warm.mp3")
    return a_hook, a_cur, a_calm, a_warm
