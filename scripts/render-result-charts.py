"""Render selected Table 2 means as static SVG charts (Python standard library)."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
CHARTS = [
    ('quantization-llama.svg', 'Llama-3.2-1B', 'WikiText-2 perplexity (lower is better)', 'W8A8', 35, [0, 10, 20, 30], [('Vanilla', '8.981', '30.189'), ('OASIS', '8.005', '8.162')]),
    ('quantization-qwen.svg', 'Qwen3-0.6B', 'GSM8K Pass@1 (%) (higher is better)', 'W4A4', 70, [0, 20, 40, 60], [('Vanilla', '62.58', '45.67'), ('OASIS', '62.68', '58.88')]),
]

for filename, model, metric, precision, limit, ticks, rows in CHARTS:
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 350" role="img" aria-labelledby="title desc"><title id="title">{escape(model)}: before and after quantization</title><desc id="desc">{escape(metric)}. Means from Table 2. ' + ' '.join(f'{name}: FP16 {full}; {precision} {quant}.' for name, full, quant in rows) + '</desc><rect width="560" height="350" fill="#fcfcfc"/><g font-family="Arial, Helvetica, sans-serif" fill="#303030">']
    parts.append(f'<text x="36" y="30" font-size="16">{escape(model)}</text><text x="36" y="53" font-size="12" fill="#666">{escape(metric)}</text>')
    parts.append(f'<rect x="337" y="20" width="11" height="11" fill="#929292"/><text x="355" y="30" font-size="12">FP16</text><rect x="415" y="20" width="11" height="11" fill="#242424"/><text x="433" y="30" font-size="12">{precision}</text>')
    baseline, scale = 295, 190 / limit
    for tick in ticks:
        y = baseline - tick * scale
        parts.append(f'<line x1="65" x2="525" y1="{y}" y2="{y}" stroke="#e5e5e5"/><text x="51" y="{y+4}" font-size="12" text-anchor="end" fill="#666">{tick}</text>')
    for group, (name, full, quant) in enumerate(rows):
        x = 114 + group * 227
        for offset, raw, color in [(0, full, '#929292'), (62, quant, '#242424')]:
            height = float(raw) * scale
            y = baseline - height
            parts.append(f'<rect x="{x+offset}" y="{y}" width="43" height="{height}" fill="{color}"/><text x="{x+offset+21.5}" y="{y-10}" text-anchor="middle" font-size="14">{raw}</text>')
        parts.append(f'<text x="{x+52.5}" y="325" text-anchor="middle" font-size="14">{name}</text>')
    parts.append('</g></svg>')
    (ASSETS / filename).write_text('\n'.join(parts))
    print(filename)

    mobile = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 350" role="img" aria-labelledby="title desc"><title id="title">{escape(model)}: before and after quantization</title><desc id="desc">{escape(metric)}. ' + ' '.join(f'{name}: FP16 {full}; {precision} {quant}.' for name, full, quant in rows) + '</desc><rect width="320" height="350" fill="#fcfcfc"/><g font-family="Arial, Helvetica, sans-serif" fill="#303030">']
    mobile.append(f'<text x="16" y="30" font-size="18">{model}</text><text x="16" y="54" font-size="12">{escape(metric)}</text>')
    for group, (name, full, quant) in enumerate(rows):
        top = 98 + group * 113
        mobile.append(f'<text x="16" y="{top}" font-size="16">{name}</text>')
        for offset, label, raw, color in [(22, 'FP16', full, '#929292'), (57, precision, quant, '#242424')]:
            y = top + offset
            width = float(raw) / limit * 151
            mobile.append(f'<text x="16" y="{y+15}" font-size="13" fill="#666">{label}</text><rect x="70" y="{y}" width="{width}" height="20" fill="{color}"/><text x="247" y="{y+16}" font-size="16">{raw}</text>')
    mobile.append(f'<line x1="70" x2="221" y1="319" y2="319" stroke="#d5d5d5"/><text x="70" y="338" font-size="12" fill="#666">0</text><text x="221" y="338" text-anchor="end" font-size="12" fill="#666">{limit}</text></g></svg>')
    (ASSETS / filename.replace('.svg', '-mobile.svg')).write_text('\n'.join(mobile))
