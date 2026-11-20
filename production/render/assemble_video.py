#!/usr/bin/env python3
import json, subprocess, sys, os, tempfile, shutil

RENDER_DIR = os.path.dirname(os.path.abspath(__file__))
MAKE_SCENE = os.path.join(RENDER_DIR, "make_scene.py")

def ffprobe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True
    ).stdout.strip()
    return float(out)

def render_scene_video(scene_cfg, duration, audio_path, out_path, work):
    png = os.path.join(work, "scene.png")
    subprocess.run(["python3", MAKE_SCENE, json.dumps(scene_cfg), png], check=True)
    tmp_out = out_path + ".tmp.mp4"
    zoom_expr = f"min(1+0.055*on/(30*{duration:.3f}),1.15)"
    vf = f"zoompan=z='{zoom_expr}':d=1:s=1080x1920:fps=30,format=yuv420p"
    cmd = ["ffmpeg", "-y", "-loop", "1", "-framerate", "30", "-t", f"{duration:.3f}", "-i", png]
    if audio_path:
        cmd += ["-i", audio_path, "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a",
                "-c:a", "aac", "-b:a", "160k"]
    else:
        cmd += ["-f", "lavfi", "-t", f"{duration:.3f}", "-i", "anullsrc=r=44100:cl=mono",
                "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-map", "1:a", "-c:a", "aac", "-b:a", "160k"]
    cmd += ["-r", "30", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p",
            "-shortest", tmp_out]
    subprocess.run(cmd, check=True, capture_output=True)
    shutil.move(tmp_out, out_path)

def assemble(topic, out_path):
    with tempfile.TemporaryDirectory() as work:
        scene_files = []
        for i, seg in enumerate(topic["segments"]):
            dur = ffprobe_duration(seg["audio"]) if seg.get("audio") else seg["duration"]
            sp = os.path.join(work, f"scene{i}.mp4")
            render_scene_video(seg["cfg"], dur, seg.get("audio"), sp, work)
            scene_files.append(sp)

        concat_list = os.path.join(work, "concat.txt")
        with open(concat_list, "w") as f:
            for sf in scene_files:
                f.write(f"file '{sf}'\n")
        tmp_final = out_path + ".tmp.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c", "copy", tmp_final],
            check=True, capture_output=True
        )
        shutil.move(tmp_final, out_path)

if __name__ == "__main__":
    topic = json.load(open(sys.argv[1]))
    assemble(topic, sys.argv[2])
    print("OK", out_path if False else sys.argv[2])
