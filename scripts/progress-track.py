"""Draw assets/k8s-dr-progress.svg.

Usage: python3 scripts/progress-track.py COMPLETED
COMPLETED is how many milestones are done (0 to 8), matching plan.md in k8s-dr.
"""
import sys

LABELS = ["Contract", "Infrastructure", "Kubernetes", "Service",
          "Backups", "Cold recovery", "Drill", "Faster recovery"]
PRIMARY = range(0, 4)   # milestones drawn inside the primary region
RECOVERY = range(5, 8)  # milestones drawn inside the recovery region

done = int(sys.argv[1])
assert 0 <= done <= len(LABELS)
xs = [74 + i * 112 for i in range(len(LABELS))]
y = 84
font = 'font-family="Segoe UI,Arial,sans-serif"'
mid = f'text-anchor="middle" {font}'

finished = ", ".join(LABELS[:done]) or "None"
remaining = ", ".join(LABELS[done:]) or "none"
desc = f"Eight disaster recovery milestones. Complete: {finished}. Remaining: {remaining}."

left, right = xs[PRIMARY[0]] - 52, xs[RECOVERY[0]] - 62
out = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="170" viewBox="0 0 960 170" role="img" aria-labelledby="t d">',
    '  <title id="t">Kubernetes disaster recovery progress</title>',
    f'  <desc id="d">{desc}</desc>',
    '  <rect width="960" height="170" rx="10" fill="#101719"/>',
    f'  <rect x="{left}" y="22" width="{xs[PRIMARY[-1]] + 62 - left}" height="126" rx="10" fill="#15211d" stroke="#2f463d"/>',
    f'  <text x="{left + 18}" y="47" {font} font-size="13" fill="#9fb3ab">Primary region</text>',
    f'  <rect x="{right}" y="22" width="{938 - right}" height="126" rx="10" fill="none" stroke="#3e544b" stroke-dasharray="5 5"/>',
    f'  <text x="{right + 18}" y="47" {font} font-size="13" fill="#9fb3ab">Recovery region, cold until a drill</text>',
]
end = xs[min(done, len(xs) - 1)]
if done:
    out.append(f'  <path d="M{xs[0]} {y}H{end}" stroke="#a7f3c8" stroke-opacity=".7" stroke-width="2"/>')
if done < len(xs) - 1:
    out.append(f'  <path d="M{end} {y}H{xs[-1]}" stroke="#3e544b" stroke-width="2" stroke-dasharray="3 5"/>')

for i, (x, label) in enumerate(zip(xs, LABELS)):
    number = f'<text x="{x}" y="{y + 4.5}" {mid} font-size="12"'
    if i < done:
        out.append(f'  <circle cx="{x}" cy="{y}" r="12" fill="#a7f3c8"/>{number} font-weight="600" fill="#101719">{i}</text>')
        color = "#dfeae5"
    elif i == done:
        out.append(f'  <circle cx="{x}" cy="{y}" r="18" fill="none" stroke="#a7f3c8" stroke-opacity=".3"/>'
                   f'<circle cx="{x}" cy="{y}" r="12" fill="#101719" stroke="#a7f3c8" stroke-width="2"/>'
                   f'{number} font-weight="600" fill="#a7f3c8">{i}</text>')
        color = "#a7f3c8"
    else:
        out.append(f'  <circle cx="{x}" cy="{y}" r="12" fill="#101719" stroke="#4a6158"/>{number} fill="#8b9d96">{i}</text>')
        color = "#8b9d96"
    out.append(f'  <text x="{x}" y="{y + 40}" {mid} font-size="15" fill="{color}">{label}</text>')
out.append("</svg>")

with open("assets/k8s-dr-progress.svg", "w") as f:
    f.write("\n".join(out) + "\n")
