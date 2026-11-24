#!/usr/bin/env python3
import os, sys, subprocess, json
sys.path.insert(0, os.path.dirname(__file__))
from build_video import (scene_hook, scene_begriff, scene_explain, scene_payoff, scene_outro,
                          render_scene_video, ffprobe_duration, ROOT)

AUDIO = {
    "tag4": "production/assets/audio/tag4",
    "tag5": "production/assets/audio/tag5",
}

SLOTS = [
    dict(tag="tag4", slot="slot1_sozialkompetenz", out="tag4_slot1_mimicry",
         icon_a="sozial_a_herzblasen.png", icon_b="sozial_b_auge.png", explain_icon="sozial_a_herzblasen.png",
         hook="Warum wirkt jemand, der deine Gestik spiegelt, automatisch sympathischer?",
         begriff="Mimicry-\nEffekt",
         explain="Unbewusstes Spiegeln von Haltung und Tonfall signalisiert dem Gehirn: diese Person ist wie ich.",
         warm="Probier es bewusst aus, und beobachte, wie Gespräche leichter werden."),
    dict(tag="tag4", slot="slot2_ernaehrung", out="tag4_slot2_oel",
         icon_a="ernaehrung_a_teller.png", icon_b="ernaehrung_b_oel.png", explain_icon="ernaehrung_b_oel.png",
         hook="Welches Öl solltest du niemals stark erhitzen?",
         begriff="Niedriger\nRauchpunkt",
         explain="Über dieser Temperatur zerfallen die Öle und bilden schädliche Stoffe.",
         warm="Zum scharfen Anbraten besser raffiniertes Öl oder Kokosöl nehmen."),
    dict(tag="tag4", slot="slot3_wissenschaft", out="tag4_slot3_fallschirm",
         icon_a="wissenschaft_a_atom.png", icon_b="wissenschaft_b_tacho.png", explain_icon="wissenschaft_b_tacho.png",
         hook="Warum werden Fallschirmspringer im freien Fall nicht immer weiter schneller?",
         begriff="Grenz-\ngeschwindigkeit",
         explain="Ab einer bestimmten Geschwindigkeit gleicht der Luftwiderstand die Schwerkraft genau aus.",
         warm="Bauchlage: etwa 200 km/h. Das ist die physikalische Grenze des freien Falls."),
    dict(tag="tag5", slot="slot1_psychologie", out="tag5_slot1_zeigarnik",
         icon_a="psychologie_a_hirnlampe.png", icon_b="psychologie_b_blasen.png", explain_icon="psychologie_a_hirnlampe.png",
         hook="Warum lässt dich eine unfertige Aufgabe nicht los?",
         begriff="Zeigarnik-\nEffekt",
         explain="Unser Gehirn merkt sich Unerledigtes stärker als Abgeschlossenes - wie eine offene Schleife.",
         warm="Teil große Aufgaben in kleine Schritte, dann beruhigt sich dein Kopf schneller."),
    dict(tag="tag5", slot="slot2_sport", out="tag5_slot2_muskelkater",
         icon_a="sport_a_laufschuhe.png", icon_b="sport_b_hantel.png", explain_icon="sport_b_hantel.png",
         hook="Ist Milchsäure wirklich schuld an deinem Muskelkater?",
         begriff="Milchsäure-\nMythos",
         explain="Muskelkater entsteht durch winzige Risse in den Muskelfasern nach ungewohnter Belastung.",
         warm="Die gute Nachricht: leichte Bewegung und Dehnen helfen beim Regenerieren."),
    dict(tag="tag5", slot="slot3_ernaehrung", out="tag5_slot3_schokolade",
         icon_a="ernaehrung_a_teller.png", icon_b="ernaehrung_b_oel.png", explain_icon="ernaehrung_a_teller.png",
         hook="Welche Schokolade hat eigentlich mehr Zucker: dunkel oder weiß?",
         begriff="Kakao-\nanteil",
         explain="Dunkle Schokolade mit hohem Kakaoanteil hat weniger Zucker und mehr Antioxidantien.",
         warm="Ab 70 Prozent Kakaoanteil triffst du die gesündere Wahl."),
]

def main(only=None):
    frames_dir = os.path.join(ROOT, "production/render/frames")
    scenes_dir = os.path.join(ROOT, "production/render/scenes")
    out_dir = os.path.join(ROOT, "videos")
    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs(scenes_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    results = {}
    for cfg in SLOTS:
        if only and cfg["out"] != only:
            continue
        audio_dir = os.path.join(ROOT, AUDIO[cfg["tag"]])
        a_hook = os.path.join(audio_dir, f"{cfg['slot']}_1hook.mp3")
        a_cur = os.path.join(audio_dir, f"{cfg['slot']}_2curious.mp3")
        a_calm = os.path.join(audio_dir, f"{cfg['slot']}_3calm.mp3")
        a_warm = os.path.join(audio_dir, f"{cfg['slot']}_4warm.mp3")
        for p in (a_hook, a_cur, a_calm, a_warm):
            assert os.path.exists(p), p

        dur_hook = ffprobe_duration(a_hook)
        dur_cur = ffprobe_duration(a_cur)
        dur_calm = ffprobe_duration(a_calm)
        dur_warm = ffprobe_duration(a_warm)
        dur_outro = 1.8

        name = cfg["out"]
        print("=== building", name)

        f1 = os.path.join(frames_dir, f"{name}_1.png")
        f2 = os.path.join(frames_dir, f"{name}_2.png")
        f3 = os.path.join(frames_dir, f"{name}_3.png")
        f4 = os.path.join(frames_dir, f"{name}_4.png")
        f5 = os.path.join(frames_dir, f"{name}_5.png")

        scene_hook(cfg["icon_a"], cfg["icon_b"], cfg["hook"]).convert("RGB").save(f1)
        scene_begriff(cfg["icon_a"], cfg["begriff"]).convert("RGB").save(f2)
        scene_explain(cfg["explain_icon"], cfg["explain"]).convert("RGB").save(f3)
        scene_payoff(cfg["warm"]).convert("RGB").save(f4)
        scene_outro().convert("RGB").save(f5)

        s1 = os.path.join(scenes_dir, f"{name}_1.mp4")
        s2 = os.path.join(scenes_dir, f"{name}_2.mp4")
        s3 = os.path.join(scenes_dir, f"{name}_3.mp4")
        s4 = os.path.join(scenes_dir, f"{name}_4.mp4")
        s5 = os.path.join(scenes_dir, f"{name}_5.mp4")

        render_scene_video(f1, s1, dur_hook, zoom_dir="in", audio_path=a_hook)
        render_scene_video(f2, s2, dur_cur, zoom_dir="out", audio_path=a_cur)
        render_scene_video(f3, s3, dur_calm, zoom_dir="in", audio_path=a_calm)
        render_scene_video(f4, s4, dur_warm, zoom_dir="static", audio_path=a_warm)
        render_scene_video(f5, s5, dur_outro, zoom_dir="static", audio_path=None)

        concat_list = os.path.join(scenes_dir, f"{name}_concat.txt")
        with open(concat_list, "w") as fh:
            for s in (s1, s2, s3, s4, s5):
                fh.write(f"file '{s}'\n")

        final = os.path.join(out_dir, f"{name}.mp4")
        tmp_final = final + ".tmp.mp4"
        cmd = ["ffmpeg","-y","-f","concat","-safe","0","-i", concat_list, "-c","copy", tmp_final]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-3000:])
            raise RuntimeError("concat failed for " + name)
        os.replace(tmp_final, final)
        total_dur = ffprobe_duration(final)
        print(name, "-> total duration", round(total_dur,2), "s")
        results[name] = total_dur

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    main(only)
