# @dailyfaktor – Produktionsplan Tag 4–10 (Stand: 2026-11-20, Fr. Abend)

## Charakter "Dr. Wissen"
- Pink/magenta Brain-Kopf-Maskottchen, runde schwarze Brille, Punktaugen, kleines Lächeln, weißer Arztkittel mit Kette/Anhänger, kleine pinke Arme/Beine. Flat-Vector-Illustrationsstil.
- Referenzbild neu generiert (ElevenLabs, bytedance-seedream-5.5, transparenter Hintergrund):
  flow_id=ny2IJBZnDKzbjZpk0l7x, node_id=M0Rpxi2Lh11Fj6Mf9NOJ, generation_id=YQ5BIc08idjGMVqsrUrB
  (Download blockiert, siehe unten – muss noch heruntergeladen werden)

## Stimme
- "Thomas - Warm German Explainer", voice_id = vv3bG6FrcGtmeOdRSriS, model eleven_v4

## Video-Template v1 (aus bestehenden geposteten Videos rekonstruiert, Tag1-3 + Tag4/5 Audio)
1080x1920, ~22-35s, 4 Audiosegmente pro Video:
  1. Hook-Frage (Badge "DR. WISSEN" oben, Charakter groß mittig, Frage unten, dunkel-lila Verlaufshintergrund)
  2. [curious] Antwort/Begriff (Charakter klein oben, Sprechblase mit Text mittig)
  3. [calm] Fortsetzung/Erklärung (gleiche Anordnung, Sprechblasenfarbe variiert leicht)
  4. [warm] Payoff/CTA (Charakter wieder groß mit Badge, Fazit-Text)
  + Outro-Overlay letzte ~1-2s: Hintergrund wird warm/orange, "FOLLOW @DAILYFAKTOR" / "New fact tomorrow."

## Nutzer-Feedback (2026-11-20 Abend) → Video-Template v2
Feedback: Aufbau insgesamt gut, aber visuell zu statisch. Gewünscht:
  - "Realistischer aufgebaut" = NICHT fotorealistische Personen, sondern ein dynamischerer, durchdachterer visueller Aufbau (wirkt weniger wie eine einzelne starre Folie pro Segment).
  - Mehr Szenenwechsel (nicht nur 4 fast identische Layouts, sondern klar unterscheidbare Schnitte).
  - Text sichtbar/deutlich in der Bildmitte (nicht unten am Rand wie bisher).
  - Szenen sollen inhaltlich "aufbauen", d.h. pro Thema eigene Illustrations-/Icon-Elemente statt immer nur des Maskottchens in derselben Pose.

### Template v2 – Szenenplan (5 Szenen statt 4, gleicher Stil: flat-vector, kein Fotorealismus)
1. **Hook (Intro)**: Dunkel-lila Verlauf mit thema-bezogenen Icon-Silhouetten im Hintergrund (z.B. Öltropfen, Blitzer-Symbol, Gehirn-Icons - je nach Kategorie ein Icon-Set), Badge "DR. WISSEN" oben, Charakter mittig-klein eingeblendet, **Hook-Frage groß und zentriert in der Bildmitte** (nicht unten), leichter Zoom-in (Ken-Burns) auf den Hintergrund für Bewegung.
2. **Begriff/Antwort**: Harter Schnitt. Charakter wandert in eine Ecke (z.B. unten links, klein), die Bildmitte zeigt eine **themenspezifische Flat-Icon-Illustration** (z.B. zwei Früchte nebeneinander, ein Tacho, zwei Gehirnhälften mit Pfeil), der Fachbegriff als großer zentrierter Text darüber/darunter.
3. **Erklärung/Mechanismus**: Harter Schnitt, andere Kamera-Perspektive (reingezoomt auf die Illustration aus Szene 2, ggf. mit Pfeilen/Kreisen als Annotation), Text weiterhin zentriert, Charakter kurz am Bildrand sichtbar für Kontinuität.
4. **Payoff/Fazit**: Harter Schnitt zurück auf Charakter groß+zentriert mit Badge, Hintergrundfarbe wechselt leicht (z.B. wärmerer Lila-Ton), zentrierter Fazit-Text, kurzer Pop-in-Effekt auf den Text.
5. **Outro**: Harter Schnitt auf warmen Orange-Verlauf, Charakter klein, "FOLGE @DAILYFAKTOR" + "Morgen: neuer Fakt" zentriert.
Zwischen Szenen: kein Crossfade, sondern bewusst harte Schnitte (Jump-Cuts) für den dynamischeren, "realistischeren" Social-Media-Schnitt-Rhythmus; optional ein dezenter Whip-Pan/Zoom-Blitz als Übergang alle 2 Szenen. Jede Szene bekommt einen leichten Kamera-Move (langsamer Zoom oder Pan) statt komplett statischem Bild, gemäß video-making Skill pro Szene eigene Render-Datei + concat demuxer.
Pro Thema wird vorab ein kleines Set an 2-3 Icon/Illustrations-Motiven festgelegt (passend zur Kategorie/zum Fakt), die in Szene 2+3 wiederverwendet werden.

Rendering gemäß video-making Skill: pro Szene eigene Datei rendern (loop=-1:1 + trim=duration=<audiolänge>, ggf. mit zoompan-Filter für Kamera-Move), dann concat demuxer, Audio pro Szene gemuxt.

## BLOCKER (wichtig!)
Das Sandbox-Netzwerk erlaubt keine Verbindung zu `elevenlabsusercontent.com` (403 "no rule or network setting allows this host") – weder per curl noch per WebFetch-Subagent (PROVENANCE_REQUIRED/Timeout). Dadurch können generierte Audio-Dateien (mp3) und das Charakterbild (png) nicht heruntergeladen werden, obwohl die Generierung in ElevenLabs selbst erfolgreich ist (Status "completed").
Folge: Video-Zusammenschnitt ist aktuell nicht möglich, obwohl Skripte+Audio vorbereitet sind.
Lösung (eine davon nötig):
  (a) Admin/Nutzer gibt `elevenlabsusercontent.com` in den Netzwerk-/Egress-Einstellungen des Workspace frei
  (b) Nutzer lädt die Dateien selbst herunter (Links s.u. bzw. ElevenLabs-App) und schickt sie in den Chat
  (c) Nutzer baut die Videos selbst (z.B. lokal) und übergibt fertige mp4s zum Posten

## Tag 4 (bereits in queue.json als "pending", Audio FERTIG generiert)
Flow: Hu3cZdIeL5UisObsZxeM ("dailyfaktor_day4"), 12/12 Segmente completed.
- Slot1 Sozialkompetenz "Mimicry: Warum Spiegeln sympathisch macht"
  1 Hook: "Warum wirkt jemand, der deine Gestik spiegelt, automatisch sympathischer?" (gen jPrSb2xExxkoSbexXLhd)
  2 [curious]: "Das nennt man Mimicry-Effekt..." (gen QeLUyDSdc1ldqr6Siq4h)
  3 [calm]: "...unbewusstes Spiegeln von Haltung und Tonfall signalisiert dem Gehirn: diese Person ist wie ich." (gen g3H0DRPmoGPoUO9207bO)
  4 [warm]: "Probier es bewusst aus, und beobachte, wie Gespräche leichter werden." (gen eFrBmEkwghBbO7mapbx1)
- Slot2 Ernährung "Welches Öl du nie zu stark erhitzen solltest"
  1 Hook: "Welches Öl solltest du niemals stark erhitzen?" (gen A8IOTGPAkngvhtInVaUs)
  2 [curious]: "Natives Olivenöl und Leinöl haben einen niedrigen Rauchpunkt..." (gen wM3FIO9HZ1sFWedVWzl2)
  3 [calm]: "...über dieser Temperatur zerfallen sie und bilden schädliche Stoffe." (gen kYli7zf78UnjzEXGOFJj)
  4 [warm]: "Zum scharfen Anbraten besser raffiniertes Öl oder Kokosöl nehmen." (gen WhNZUpgrQTL6Z1SPDDLb)
- Slot3 Wissenschaft "Warum Fallschirmspringer nicht ewig schneller werden"
  1 Hook: "Warum werden Fallschirmspringer im freien Fall nicht immer weiter schneller?" (gen pmx8wMaIlozCQWVApDZe)
  2 [curious]: "Ab einer bestimmten Geschwindigkeit gleicht der Luftwiderstand..." (gen aQ6LknKICHDeeVh9rYjM)
  3 [calm]: "...die Schwerkraft genau aus. Das nennt man Grenzgeschwindigkeit." (gen UzgAf5WHcZlyjamdBVTp)
  4 [warm]: "Bauchlage: etwa 200 Kilometer pro Stunde. Das ist die physikalische Grenze des freien Falls." (gen GD7tTjcjnvRstd7daOYJ)

## Tag 5 (in queue.json als "pending", Audio FERTIG generiert, je eigener Flow)
- Slot1 Psychologie "Der Zeigarnik-Effekt: Unfertiges lässt uns nicht los"
  1 Hook: "Warum lässt dich eine unfertige Aufgabe nicht los?" — flow Vn0BJ8s5spmcZuG95nCf / node T7HxH7Rhl09mDALexxVN / session LlBYEJb7DbUfQ2fFhM7f
  2 [curious]: "Das nennt man Zeigarnik-Effekt..." — flow Xd6KuRaky7HFeBnx17Vv / node cv3e4duRtiHkKqG43ViE / session Hek7DQOUFdGGTA9uO1Bp
  3 [calm]: "...unser Gehirn merkt sich Unerledigtes viel stärker als Abgeschlossenes, weil es wie eine offene Schleife wirkt." — flow E7wc0UZkuy1Y6RJC6dNb / node PMVWX4QKmBnhrVWhDw17 / session GA75aC3C6QlTB8KAlntL
  4 [warm]: "Teil große Aufgaben in kleine Schritte, dann beruhigt sich dein Kopf schneller." — flow fZe17sUd6vYJGDCJwgth / node 7Q426NAReXBact8bz9ul / session rfn4eC4x3ji8dztbvZst
- Slot2 Sport "Muskelkater hat nichts mit Milchsäure zu tun"
  1 Hook: "Ist Milchsäure wirklich schuld an deinem Muskelkater?" — flow bEG4gzZIzb5qpj9IPKSs / node IyAlTCA7cqnuj7TL5Wca / session MMOLKfFPAJkr4yLD1X8s
  2 [curious]: "Nein, das ist ein Mythos, der sich seit Jahrzehnten hält..." — flow SZmLJnYua0pa0u9uM5Jd / node Gb4f174ZmHnOh87TWK6j / session freH7DgYWyn17oX2TSOp
  3 [calm]: "...Milchsäure wird innerhalb weniger Stunden abgebaut. Muskelkater entsteht durch winzige Risse in den Muskelfasern nach ungewohnter Belastung." — flow BMWPKZn5aUgtMvN6Wg5t / node MgPcvyXqjyphDxq7OqoC / session OqLqWSVn01wBmKtNQ6TT
  4 [warm]: "Die gute Nachricht: leichte Bewegung und Dehnen helfen beim Regenerieren, nicht Stillstand." — flow M7aBoA5r7TwCKCtLbArH / node 4J22dvfLAcBQ2YJ5pJ3e / session dDz1ddQbQvunHtDWza86
- Slot3 Ernährung "Dunkle vs weiße Schokolade - was wirklich drin ist"
  1 Hook: "Welche Schokolade hat eigentlich mehr Zucker: dunkel oder weiß?" — flow C52MEwICPOcNJPon4B38 / node R1TVHnEyemIrdVVQrp2b / session rEmLxgCoVaxQfoABJ64W
  2 [curious]: "Weiße Schokolade enthält gar keinen Kakaoanteil, nur Kakaobutter, Milch und Zucker..." — flow TCoBhsj9V2c3ZIezgGp8 / node ndG5amGPfIPgtqVfy1d4 / session 8KIgCesKzSyga6NxArEw
  3 [calm]: "...dunkle Schokolade mit hohem Kakaoanteil hat dagegen weniger Zucker und mehr Antioxidantien." — flow wQ2qvmZMnnKYPZZx9uez / node 1v0mrIPnnWl0rJePay2b / session BklZv0cbYf6jg2MtZm9j
  4 [warm]: "Ab 70 Prozent Kakaoanteil triffst du die gesündere Wahl." — flow goDYdvnI3yDTfyHsVcUE / node LSHXfTOTfsX1f0ZjsLbM / session gv9B5RMY9n894CD0f4dj

## Tag 6 (Skripte fertig, Audio NOCH NICHT generiert)
- Slot1 Wissenschaft "Warum Katzen fast immer auf die Pfoten fallen"
  1 Hook: "Warum landen Katzen fast immer auf den Pfoten?"
  2 [curious]: "Das nennt man den Aufrichtereflex..."
  3 [calm]: "...ihr Innenohr erkennt in Sekundenbruchteilen, wo oben und unten ist, und ihre flexible Wirbelsäule dreht den Körper automatisch."
  4 [warm]: "Trotzdem: aus großer Höhe ist ein Sturz auch für Katzen gefährlich."
- Slot2 Sozialkompetenz "Die 2-Minuten-Regel gegen Aufschieben"
  1 Hook: "Wie schaffst du es, weniger aufzuschieben?"
  2 [curious]: "Die 2-Minuten-Regel sagt..."
  3 [calm]: "...dauert eine Aufgabe weniger als 2 Minuten, mach sie sofort, statt sie auf später zu schieben."
  4 [warm]: "Kleine erledigte Aufgaben geben dir Momentum für die großen."
- Slot3 Psychologie "Warum wir prokrastinieren, obwohl wir es besser wissen"
  1 Hook: "Warum schieben wir Dinge auf, obwohl wir wissen, dass es schlecht ist?"
  2 [curious]: "Prokrastination ist kein Zeitmanagement-Problem..."
  3 [calm]: "...sondern ein Emotionsmanagement-Problem: wir vermeiden das unangenehme Gefühl, das die Aufgabe auslöst."
  4 [warm]: "Der Trick: den ersten kleinen Schritt so einfach machen, dass er sich nicht unangenehm anfühlt."

## Tag 7 (Skripte fertig, Audio NOCH NICHT generiert)
- Slot1 Ernährung "Bananen-Reifung: warum und wie stoppen"
  1 Hook: "Warum werden Bananen so schnell braun?"
  2 [curious]: "Bananen produzieren das Reifegas Ethylen..."
  3 [calm]: "...das den Reifeprozess beschleunigt, besonders wenn sie mit anderen Früchten zusammenliegen."
  4 [warm]: "Trenn sie vom Rest und wickle den Stiel in Frischhaltefolie, dann halten sie länger."
- Slot2 Sport "Cardio vor oder nach Krafttraining?"
  1 Hook: "Solltest du vor oder nach dem Krafttraining Cardio machen?"
  2 [curious]: "Willst du vor allem Kraft und Muskeln aufbauen..."
  3 [calm]: "...mach Cardio danach, sonst sind deine Muskeln schon vorermüdet und du verlierst Kraft bei den Übungen."
  4 [warm]: "Geht es dir primär um Ausdauer, kannst du Cardio zuerst machen."
- Slot3 Wissenschaft "Warum man im Flugzeug Alkohol schneller spürt"
  1 Hook: "Warum spürst du Alkohol im Flugzeug schneller?"
  2 [curious]: "In der Kabine herrscht ein niedrigerer Luftdruck und weniger Sauerstoff im Blut..."
  3 [calm]: "...das verstärkt die Wirkung von Alkohol auf dein Gehirn zusätzlich zur Dehydrierung durch die trockene Kabinenluft."
  4 [warm]: "Trink während des Flugs lieber mehr Wasser und Alkohol in Maßen."

## Tag 8 (NEU, Skripte fertig, Audio NOCH NICHT generiert)
- Slot1 Ernährung "Warum aufgewärmter Spinat riskant werden kann"
  1 Hook: "Warum sollte man aufgewärmten Spinat nicht mehrfach erhitzen?"
  2 [curious]: "Spinat enthält Nitrat..."
  3 [calm]: "...beim wiederholten Erhitzen und Abkühlen wandelt es sich in Nitrit um, das in größeren Mengen gesundheitsschädlich sein kann."
  4 [warm]: "Spinat nur einmal erhitzen und Reste schnell kühl lagern."
- Slot2 Psychologie "Der Halo-Effekt: Warum schöne Menschen kompetenter wirken"
  1 Hook: "Warum wirken attraktive Menschen auf uns automatisch kompetenter?"
  2 [curious]: "Das nennt man Halo-Effekt..."
  3 [calm]: "...eine positive Eigenschaft wie Attraktivität färbt unbewusst auf unsere Einschätzung aller anderen Eigenschaften ab."
  4 [warm]: "Gegenmittel: bewusst auf Fakten statt auf den ersten Eindruck achten."
- Slot3 Sport "Kalt duschen direkt nach dem Krafttraining?"
  1 Hook: "Ist eine kalte Dusche direkt nach dem Krafttraining wirklich gut?"
  2 [curious]: "Kälte kann kurzfristig Schmerzen lindern..."
  3 [calm]: "...aber Studien zeigen, dass sie direkt nach dem Training die Muskelproteinsynthese und damit den Muskelaufbau bremsen kann."
  4 [warm]: "Für reinen Muskelaufbau: lieber ein paar Stunden warten, bevor es eiskalt wird."

## Tag 9 (NEU, Skripte fertig, Audio NOCH NICHT generiert)
- Slot1 Wissenschaft "Warum man im All kein Laserschwert hört"
  1 Hook: "Warum hört man im Weltall kein Laserschwert-Geräusch?"
  2 [curious]: "Schall braucht ein Medium wie Luft, um sich auszubreiten..."
  3 [calm]: "...im Vakuum des Weltalls gibt es keine Teilchen, die Schallwellen übertragen können."
  4 [warm]: "Im echten All wäre es also komplett lautlos - zum Glück nimmt sich Film-Science-Fiction diese Freiheit."
- Slot2 Sozialkompetenz "Die Pause-Technik: 2 Sekunden Schweigen wirken klüger"
  1 Hook: "Warum wirkst du klüger, wenn du 2 Sekunden länger schweigst, bevor du antwortest?"
  2 [curious]: "Eine kurze Pause signalisiert, dass du wirklich nachdenkst..."
  3 [calm]: "...statt automatisch zu reagieren, was Zuhörer unbewusst als überlegter und souveräner wahrnehmen."
  4 [warm]: "Übe es bewusst im nächsten Gespräch: kurz Luft holen, dann antworten."
- Slot3 Ernährung "Warum Honig nie schlecht wird"
  1 Hook: "Warum wird Honig eigentlich nie schlecht?"
  2 [curious]: "Honig hat einen sehr niedrigen Wassergehalt und einen hohen Säuregehalt..."
  3 [calm]: "...das macht es Bakterien und Pilzen fast unmöglich, darin zu überleben."
  4 [warm]: "Selbst Jahrtausende alter Honig aus ägyptischen Gräbern war noch essbar."

## Tag 10 (NEU, Skripte fertig, Audio NOCH NICHT generiert)
- Slot1 Psychologie "Der Pygmalion-Effekt: Erwartungen verändern Leistung"
  1 Hook: "Kann die Erwartung an eine Person wirklich ihre Leistung verändern?"
  2 [curious]: "Das zeigt der Pygmalion-Effekt..."
  3 [calm]: "...wenn Lehrer oder Chefs hohe Erwartungen an jemanden haben, verhalten sie sich unbewusst unterstützender, und die Person liefert tatsächlich bessere Leistungen."
  4 [warm]: "Erwarte das Beste von anderen, und du bringst oft das Beste aus ihnen heraus."
- Slot2 Sport "Wird man vom Krafttraining wirklich 'bulky'?"
  1 Hook: "Werden Frauen vom Krafttraining wirklich schnell 'bulky'?"
  2 [curious]: "Nein, dafür fehlt den meisten Frauen hormonell schlicht das Testosteron-Niveau..."
  3 [calm]: "...starkes Muskelwachstum wie bei Bodybuildern braucht Jahre an gezieltem Training und Ernährung."
  4 [warm]: "Krafttraining formt und strafft eher, als dass es dich 'bulky' macht."
- Slot3 Wissenschaft "Warum Flugzeugfenster rund sind"
  1 Hook: "Warum sind Flugzeugfenster eigentlich rund und nicht eckig?"
  2 [curious]: "Frühe Düsenflugzeuge hatten eckige Fenster..."
  3 [calm]: "...an den scharfen Ecken konzentrierte sich der Luftdruck so stark, dass dort Risse im Rumpf entstanden, die zu Abstürzen führten."
  4 [warm]: "Runde Fenster verteilen den Druck gleichmäßiger - heute Standard in der Luftfahrt."

## Tag 6-10 Audio: ALLES generiert (Stand 2026-11-20, Status lief auf "completed" wie bei Tag 4/5)
Plus 10 Kategorie-Icons + das Dr.-Wissen-Charakterbild. Da ich (Claude) die Dateien wegen des Netzwerk-Blockers nicht
herunterladen kann, aber der Nutzer das selbst kann: **Reihenfolge ist der Schlüssel zum Zuordnen.**

### So kommen die Dateien zu mir (für den Nutzer)
1. In der ElevenLabs-App: **Image/Video → History** öffnen, nach Erstellungsdatum **älteste zuerst** sortieren.
   Die ersten 11 Bilder (in dieser Reihenfolge) sind: 1) Dr.-Wissen-Charakter, 2) Ernährung-Icon A (Teller),
   3) Ernährung-Icon B (Öltropfen), 4) Sport-Icon A (Laufschuhe), 5) Sport-Icon B (Hantel+Puls),
   6) Psychologie-Icon A (Gehirn+Glühbirne), 7) Psychologie-Icon B (Sprechblasen gespiegelt),
   8) Wissenschaft-Icon A (Atom), 9) Wissenschaft-Icon B (Tacho), 10) Sozialkompetenz-Icon A (Herz+Sprechblasen),
   11) Sozialkompetenz-Icon B (Auge+Funkeln). Alle herunterladen (als PNG, mit Transparenz) und in den Chat hochladen,
   am besten in dieser Reihenfolge benannt (z.B. 01_charakter.png, 02_icon.png, ...).
2. In der ElevenLabs-App: **Speech Synthesis → History** öffnen, ebenfalls älteste zuerst sortieren.
   Die Tag-4/5-Audios sind schon einzeln nach generation_id oben im Dokument aufgeführt/bekannt.
   Die NEUEN 60 Audio-Dateien (Tag 6-10) kommen in exakt dieser Reihenfolge (so wurden sie generiert):
   Tag6-Slot1(4) → Tag6-Slot2(4) → Tag6-Slot3(4) → Tag7-Slot1(4) → Tag7-Slot2(4) → Tag7-Slot3(4) →
   Tag8-Slot1(4) → Tag8-Slot2(4) → Tag8-Slot3(4) → Tag9-Slot1(4) → Tag9-Slot2(4) → Tag9-Slot3(4) →
   Tag10-Slot1(4) → Tag10-Slot2(4) → Tag10-Slot3(4). Jeweils 4 Segmente pro Slot in der Reihenfolge
   Hook → [curious] → [calm] → [warm] (Text steht weiter oben in diesem Dokument bei jedem Tag/Slot).
   Am einfachsten: alle 60 als mp3 herunterladen, in chronologischer Reihenfolge durchnummerieren
   (z.B. 001.mp3 ... 060.mp3) und hochladen - ich ordne sie dann anhand der Reihenfolge den Themen zu.
3. Alternativ (am wenigsten fehleranfällig): einfach ALLES aus der History (Bilder + Audio) als ZIP/Batch
   herunterladen und mir hier hochladen, mit Hinweis "älteste zuerst sortiert". Ich matche dann selbst anhand
   Dateidatum/Reihenfolge in den Metadaten.

### Flow-IDs Tag 6-10 (zur Referenz, falls Einzelzugriff nötig ist)
Tag6: HFElYV8N40NcaxjBqOsq, qtlWmiDMYJ0okIRGI4v0, yEekQiIJSZJuHQdhq8Jq, NLwuy04aZ659yEpZDaO1 (Slot1 Hook..warm);
65GT6iRqIWUuLjz8UiWW, 4pNtWJE9iatQZQ2AD71G, ocLWvFnRvTedchnWhq30, EdoeCl9Xd05XZVSycipT (Slot2);
jSlP66p6QTO3ZpleGXCe, f0WH6SOpNfLSODtmMmzP, GYnZCWmShIGnUPESB87o, NEmVvTEiuDZyzYyW8aWL (Slot3)
Tag7: JOQ8SkcUdE2r4jIskFqN, fWMySmkdVpenSyO1U3Wl, WBxxWucu005nyBdv2ewE, wcOliEAyqB8ABRkdUljw (Slot1);
NtlRG0MtOVkkJsrf7Mm9, How2BH7lJe95NZH8t8eM, yKBYwRiO5q5J0BCK3Sik, 1zBYksMOIYCblfuRVP5n (Slot2);
3Tr89aK7H7ajMbnkBA7z, GU7Q6DnLTs0CH029tyiI, esdVlUCg5btA9W1ubOIh, NGjbXfLTkXP6KTXrkx4E (Slot3)
Tag8: 6iMJ82wDgEfZb7Z5V3Yy, ZWbWYPSMWDLHrubDA0pI, O4nC1beLvB8Z12XHeAQN, MCY2ZbTRjFhrpGj9LYxO (Slot1);
CewhIE9gORrHRNS41rsO, fJQeuc4bLGeykwQ1ieZE, aJRSdtNVLBpYuQpBFNT2, ewNQnXDcu5NoEYbVwWct (Slot2);
DpUQp8tFVDslwySUAbad, ejSFCXU6aNSeh8KoESpl, zh3hCjwarPDBXuTz2bo5, StKMzY2mbfn3T2cUMP5i (Slot3)
Tag9: MDNP29laJWViXJK1tnkT, xGug96wxQMKo3spbIgmx, pWRO0qKaCHCmcUTlhI7p, fREHJJfaoIaKNJaepXIX (Slot1);
QTa75BB1mepVSmoYxWtM, qDZxWfEGkoZ88nneUv1T, ltYRNO6AqWrXPjR7Peqv, x3BqcAj0V5iBHsyjJKSc (Slot2);
hQ9sSERY21mXI0SibOSP, WRlDg1harncpXrolgbhz, JuBRMKGcg7DQV43tarl5, 6jd6ktdFeCe7JySoAobX (Slot3)
Tag10: FS5AfOCgxVkYdj5N7TGe, rnGwRCBNQuxwuPjdP7lT, Om8ZVbJRhqrglwHVOnSA, eO5cW83Ts5Omt2PuP489 (Slot1);
88nAVo6rGcyKxvlHMTIF, FN7NEYS3SyKK2ijKdKRC, F2qcM0j3Ox4BucoAmM48, 868QPhHrFXLSMdhraPeE (Slot2);
BGXUek0Z5Bx5bqsvTt5v, oru7h3m1PRpjWeI6SAxd, Uf2eHJACVMlb18MGSBMM, Hxdf6SwxSsaL5we4rzVq (Slot3)

### Icon-Flow-IDs (zur Referenz)
Ernährung A (Teller): zcJmugwKTceXLyyZuGxe | Ernährung B (Öl): RfvGlAHkE5Ao6L6F4at8
Sport A (Laufschuhe): VwRcSvCHdNYbglmKFWev | Sport B (Hantel): WAevJkB7lczN0pVBf6ca
Psychologie A (Gehirn+Lampe): ybzbVMcPDXsJroZL1xlS | Psychologie B (Sprechblasen): VGgAjTHoaexUWNpGeRIS
Wissenschaft A (Atom): 8w5S320y9EjsyNTQSu69 | Wissenschaft B (Tacho): whLaPhTJHjxLANzMWZaE
Sozialkompetenz A (Herz+Blasen): rc2SdQI3RWWhRSmSVLZl | Sozialkompetenz B (Auge): KlJx0nc5GPoVb8Kzn6h5
(Banane-Icon zusätzlich generiert: zux1kLdVMW0jDH5TQ9YU - optional für Bananen-Thema Tag7)
Charakter: ny2IJBZnDKzbjZpk0l7x

## Instagram-Titelbild / Cover (2026-11-20)
Problem: Instagram zeigt für die Reels kein Titelbild und wirkt im Feed "schwarz" - lag daran, dass
`create_video_post` nie ein `cover_url` übergeben hat, also nutzt Instagram per Default das erste Frame
(bei uns ein dunkler Verlauf = wirkt fast schwarz).
Lösung: Festes Branding-Titelbild erstellt und ins Repo gelegt:
  https://raw.githubusercontent.com/furkanmercan-sys/dailyfaktor-media/main/covers/cover_dr_wissen.jpg
  (1080x1920 JPEG, Dr.-Wissen-Platzhalter-Charakter, Badge, Tagline "Täglich ein neuer Fakt", @dailyfaktor)
Ab sofort IMMER `cover_url` mit dieser URL an `create_video_post` übergeben (Windsor-Action unterstützt das:
params.cover_url = publicly accessible JPEG). Der tägliche Posting-Trigger (trig_015j1YodFZFshjX3DBnSRYxA)
muss entsprechend aktualisiert werden, damit auch automatische Posts das Cover mitschicken.
Sobald das echte ElevenLabs-Charakterbild (Download durch Nutzer) vorliegt, dieses Titelbild damit ersetzen
(gleicher Dateiname/Pfad beibehalten, dann ändert sich die URL nicht).

## Nächste Schritte sobald Blocker gelöst
1. Audio für Tag 6-10 generieren (gleiche Stimme vv3bG6FrcGtmeOdRSriS, Muster wie oben).
2. Alle Audiodateien + Charakterbild herunterladen.
3. Videos zusammenschneiden (siehe Template oben), 1080x1920, h264/aac, in videos/ ablegen.
4. queue.json: Status der jeweiligen Einträge auf "ready" setzen + video_url ergänzen.
5. Commit & Push ins Repo.
