"""Render frames of an animated SVG into one PNG, stacked top to bottom.

Usage: python3 scripts/preview-animation.py assets/header.svg [SECONDS ...] [-o OUT.png]

Each frame shows the animation paused at that many seconds. With no times given,
eight evenly spaced frames across --cycle seconds (default 24) are drawn. Needs a
Chromium or Chrome binary: set CHROME, or have one on PATH or in the Playwright cache.
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile

p = argparse.ArgumentParser()
p.add_argument("svg")
p.add_argument("times", nargs="*", type=float)
p.add_argument("-o", "--out")
p.add_argument("--cycle", type=float, default=24)
a = p.parse_args()

times = a.times or [a.cycle * i / 8 for i in range(8)]
svg = open(a.svg).read()
w, h = (int(float(re.search(rf'<svg[^>]*\s{k}="([\d.]+)"', svg).group(1))) for k in ("width", "height"))

names = ["chrome-headless-shell", "chromium", "chromium-browser", "google-chrome", "chrome"]
cache = os.path.expanduser("~/.cache/ms-playwright/chromium*/*/")
found = [os.environ.get("CHROME")] + [shutil.which(n) for n in names]
found += sorted(glob.glob(cache + "chrome-headless-shell") + glob.glob(cache + "chrome"), reverse=True)
browser = next((b for b in found if b), None)
if not browser:
    sys.exit("No Chromium found. Set CHROME to a Chromium or Chrome binary.")

label = "position:absolute;left:8px;top:6px;font:12px sans-serif;color:#fff;background:#0008;padding:1px 5px"
frames = "".join(
    f'<div style="position:relative;height:{h}px" data-t="{t * 1000}">{svg}<span style="{label}">{t:g} s</span></div>'
    for t in times)
script = ("document.getAnimations().forEach(a=>{a.pause();"
          "a.currentTime=+a.effect.target.closest('[data-t]').dataset.t})")
out = os.path.abspath(a.out or os.path.join(tempfile.gettempdir(), "animation-preview.png"))
with tempfile.TemporaryDirectory() as d:
    page = os.path.join(d, "frames.html")
    with open(page, "w") as f:
        f.write(f'<body style="margin:0;background:#000">{frames}<script>{script}</script></body>')
    subprocess.run([browser, "--headless", "--no-sandbox", "--hide-scrollbars",
                    f"--window-size={w},{h * len(times)}", f"--screenshot={out}", "file://" + page],
                   check=True, stderr=subprocess.DEVNULL)
print(out)
