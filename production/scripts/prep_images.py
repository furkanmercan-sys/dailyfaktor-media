#!/usr/bin/env python3
"""Make white background transparent + autocrop for all source images."""
import os
from PIL import Image

SRC = "/home/claude/dailyfaktor-media/production/assets/images"
OUT = "/home/claude/dailyfaktor-media/production/assets/images_rgba"
os.makedirs(OUT, exist_ok=True)

def make_transparent(path_in, path_out, thresh=235):
    im = Image.open(path_in).convert("RGBA")
    datas = im.getdata()
    new_data = []
    for r, g, b, a in datas:
        if r > thresh and g > thresh and b > thresh:
            new_data.append((r, g, b, 0))
        else:
            new_data.append((r, g, b, 255))
    im.putdata(new_data)
    # autocrop to bbox of non-transparent pixels, with small padding
    bbox = im.getbbox()
    if bbox:
        l, t, r, b = bbox
        pad = 10
        l = max(0, l - pad); t = max(0, t - pad)
        r = min(im.width, r + pad); b = min(im.height, b + pad)
        im = im.crop((l, t, r, b))
    im.save(path_out)
    print(path_out, im.size)

for fn in os.listdir(SRC):
    if fn.lower().endswith(".jpg"):
        name = os.path.splitext(fn)[0]
        make_transparent(os.path.join(SRC, fn), os.path.join(OUT, name + ".png"))
