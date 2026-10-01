"""Rewrite the header paper menu in every page from one list.

Run from anywhere: python3 scripts/update-menu.py
"""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

# (folder, name, title, venue); '' is the OASIS page at the site root.
PAPERS = [
    ('', 'OASIS', 'Attention Sinks and Outliers in Attention Residuals', 'NeurIPS 2026'),
    ('ember', 'EMBER', 'Predicting TCR–pMHC Binding Without a Docked Complex', 'Preprint 2026'),
    ('frost', 'FROST', 'Filtering Reasoning Outliers with Attention for Efficient Reasoning', 'ICLR 2026'),
    ('boost', 'BOOST', "Mind the Inconspicuous: Revealing the Hidden Weakness in Aligned LLMs' Refusal Boundaries", 'USENIX Security 2025'),
    ('germ', 'GERM', 'Fast and Low-Cost Genomic Foundation Models via Outlier Removal', 'ICML 2025'),
    ('outeffhop', 'OutEffHop', 'Outlier-Efficient Hopfield Layers for Large Transformer-Based Models', 'ICML 2024'),
]
TOOLKITS = [
    ('hf-attention-normalizers', 'hf-attention-normalizers', 'Softmax1, Sparsemax, and Entmax15 attention backends for Hugging Face Transformers', 'Python package'),
]


def href(page, target):
    if page == target:
        return './'
    up = '../' if page else ''
    return up + (target + '/' if target else '') or './'


def item(page, entry):
    folder, name, title, venue = entry
    current = ' aria-current="page"' if page == folder else ''
    return (f'<li><a href="{href(page, folder)}"{current}><span class="nav-menu-name">{escape(name)}</span>'
            f'<span class="nav-menu-title">{escape(title, quote=False)}</span>'
            f'<span class="nav-menu-venue">{escape(venue)}</span></a></li>')


def menu(page):
    # The OASIS page lists earlier work only; every other page also links back to OASIS.
    papers = [p for p in PAPERS if not (page == '' and p[0] == '')]
    rows = [item(page, p) for p in papers]
    rows.append('<li class="nav-menu-group">Toolkit</li>')
    rows += [item(page, t) for t in TOOLKITS]
    return '\n'.join('            ' + r for r in rows)


# The list body never contains a nested </ul>, so an empty placeholder list is safe too.
pattern = re.compile(r'(<ul class="nav-menu-list" id="[^"]+">)(.*?)(\n\s*</ul>)', re.S)
for folder in [p[0] for p in PAPERS] + [t[0] for t in TOOLKITS]:
    path = ROOT / folder / 'index.html'
    if not path.exists():
        print(f'skip {path.relative_to(ROOT)} (not built yet)')
        continue
    html = path.read_text()
    new, count = pattern.subn(lambda m: m.group(1) + '\n' + menu(folder) + m.group(3), html)
    if count != 1:
        raise SystemExit(f'{path}: expected one menu, found {count}')
    path.write_text(new)
    print(f'updated {path.relative_to(ROOT)}')
