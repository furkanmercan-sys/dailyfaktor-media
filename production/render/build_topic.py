#!/usr/bin/env python3
import json, sys, os

ICONS = {
    "sozialkompetenz": ("sozialkompetenz_a_herz.png", "sozialkompetenz_b_auge.png"),
    "ernaehrung": ("ernaehrung_a_teller.png", "ernaehrung_b_oel.png"),
    "wissenschaft": ("wissenschaft_a_atom.png", "wissenschaft_b_tacho.png"),
    "sport": ("sport_a_laufschuhe.png", "sport_b_hantel.png"),
    "psychologie": ("psychologie_a_gehirn.png", "psychologie_b_sprechblasen.png"),
}

W, H = 1300, 2310

GLOWS = {
    "hook":    dict(glow1=(0.72*W, 0.17*H, 750, (90, 40, 140)),  glow2=(0.80*W, 0.78*H, 850, (170, 40, 110))),
    "term":    dict(glow1=(0.25*W, 0.15*H, 700, (130, 50, 160)), glow2=(0.85*W, 0.85*H, 800, (90, 40, 140))),
    "explain": dict(glow1=(0.15*W, 0.85*H, 750, (170, 40, 110)),glow2=(0.85*W, 0.15*H, 700, (90, 40, 140))),
    "payoff":  dict(glow1=(0.30*W, 0.20*H, 800, (200, 60, 120)),glow2=(0.75*W, 0.80*H, 850, (140, 50, 150))),
}
OUTRO = dict(base=(40, 15, 10), glow1=(0.30*W, 0.30*H, 900, (230, 120, 40)), glow2=(0.80*W, 0.80*H, 900, (200, 60, 40)))

def build(category, hook, term, explain, payoff, audio_prefix):
    a, b = ICONS[category]
    segs = [
        {"audio": f"{audio_prefix}_hook.mp3",
         "cfg": {"kind": "hook", "text": hook, **GLOWS["hook"]}},
        {"audio": f"{audio_prefix}_curious.mp3",
         "cfg": {"kind": "term", "text": term,
                 "icons": [(a, 460, (W*0.35, H*0.40)), (b, 460, (W*0.68, H*0.40))],
                 **GLOWS["term"]}},
        {"audio": f"{audio_prefix}_calm.mp3",
         "cfg": {"kind": "explain", "text": explain, "icon": a, **GLOWS["explain"]}},
        {"audio": f"{audio_prefix}_warm.mp3",
         "cfg": {"kind": "payoff", "text": payoff, **GLOWS["payoff"]}},
        {"duration": 2.2,
         "cfg": {"kind": "outro", **OUTRO}},
    ]
    return {"segments": segs}

if __name__ == "__main__":
    category, hook, term, explain, payoff, audio_prefix, out_json = sys.argv[1:8]
    topic = build(category, hook, term, explain, payoff, audio_prefix)
    json.dump(topic, open(out_json, "w"), ensure_ascii=False, indent=2)
