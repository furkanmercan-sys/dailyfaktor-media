#!/usr/bin/env python3
import json, os, sys, subprocess

BASE = "/home/claude/dailyfaktor-media"
AUDIO = f"{BASE}/production/audio"
RENDER = f"{BASE}/production/render"
OUT = f"{BASE}/videos_new"
os.makedirs(OUT, exist_ok=True)

TOPICS = [
    dict(id="tag4_slot1", out="tag4_slot1_mimicry.mp4", category="sozialkompetenz",
         hook="Warum wirkt jemand, der deine Gestik spiegelt, automatisch sympathischer?",
         term="Mimicry-Effekt",
         explain="Unbewusstes Spiegeln von Haltung und Tonfall signalisiert dem Gehirn: diese Person ist wie ich.",
         payoff="Probier es bewusst aus, und beobachte, wie Gespräche leichter werden."),
    dict(id="tag4_slot2", out="tag4_slot2_oel.mp4", category="ernaehrung",
         hook="Welches Öl solltest du niemals stark erhitzen?",
         term="Rauchpunkt",
         explain="Natives Olivenöl und Leinöl haben einen niedrigen Rauchpunkt - über dieser Temperatur zerfallen sie und bilden schädliche Stoffe.",
         payoff="Zum scharfen Anbraten besser raffiniertes Öl oder Kokosöl nehmen."),
    dict(id="tag4_slot3", out="tag4_slot3_fallschirm.mp4", category="wissenschaft",
         hook="Warum werden Fallschirmspringer im freien Fall nicht immer weiter schneller?",
         term="Grenzgeschwindigkeit",
         explain="Ab einer bestimmten Geschwindigkeit gleicht der Luftwiderstand die Schwerkraft genau aus.",
         payoff="Bauchlage: etwa 200 Kilometer pro Stunde. Das ist die physikalische Grenze des freien Falls."),
    dict(id="tag5_slot1", out="tag5_slot1_zeigarnik.mp4", category="psychologie",
         hook="Warum lässt dich eine unfertige Aufgabe nicht los?",
         term="Zeigarnik-Effekt",
         explain="Unser Gehirn merkt sich Unerledigtes viel stärker als Abgeschlossenes, weil es wie eine offene Schleife wirkt.",
         payoff="Teil große Aufgaben in kleine Schritte, dann beruhigt sich dein Kopf schneller."),
    dict(id="tag5_slot3", out="tag5_slot3_schokolade.mp4", category="ernaehrung",
         hook="Welche Schokolade hat eigentlich mehr Zucker: dunkel oder weiß?",
         term="Kakaoanteil zählt",
         explain="Weiße Schokolade enthält gar keinen Kakaoanteil, nur Kakaobutter, Milch und Zucker - dunkle Schokolade mit hohem Kakaoanteil hat dagegen weniger Zucker und mehr Antioxidantien.",
         payoff="Ab 70 Prozent Kakaoanteil triffst du die gesündere Wahl."),
    dict(id="tag6_slot1", out="tag6_slot1_katzen.mp4", category="wissenschaft",
         hook="Warum landen Katzen fast immer auf den Pfoten?",
         term="Aufrichtereflex",
         explain="Ihr Innenohr erkennt in Sekundenbruchteilen, wo oben und unten ist, und ihre flexible Wirbelsäule dreht den Körper automatisch.",
         payoff="Trotzdem: aus großer Höhe ist ein Sturz auch für Katzen gefährlich."),
    dict(id="tag6_slot2", out="tag6_slot2_2minuten.mp4", category="sozialkompetenz",
         hook="Wie schaffst du es, weniger aufzuschieben?",
         term="Die 2-Minuten-Regel",
         explain="Dauert eine Aufgabe weniger als 2 Minuten, mach sie sofort, statt sie auf später zu schieben.",
         payoff="Kleine erledigte Aufgaben geben dir Momentum für die großen."),
]

def main():
    for t in TOPICS:
        print("=== building", t["id"], "===")
        json_path = f"/tmp/claude-0/{t['id']}.json"
        subprocess.run(["python3", f"{RENDER}/build_topic.py", t["category"], t["hook"], t["term"],
                         t["explain"], t["payoff"], f"{AUDIO}/{t['id']}", json_path], check=True)
        out_path = f"{OUT}/{t['out']}"
        subprocess.run(["python3", f"{RENDER}/assemble_video.py", json_path, out_path], check=True)
        print("DONE", out_path)

if __name__ == "__main__":
    main()
