# OASIS paper website

Project page for **Attention Sinks and Outliers in Attention Residuals**, accepted at NeurIPS 2026 (poster).

- Paper: https://openreview.net/forum?id=yjVSLVS0Dh
- Research code: https://github.com/robinzixuan/OASIS

## Local preview

This is a static website with no build step or package installation. KaTeX and its fonts are bundled with the site.

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Editing

- `index.html`: title, authors, method, result table, citation, and metadata.
- `styles.css`: typography, layout, and mobile styles.
- `script.js`: LaTeX rendering, the copy-citation interaction with a manual-copy fallback, and the header paper menu. Shared by all pages.
- `citation.bib`: downloadable citation; keep it synchronized with the HTML.
- `assets/method.png`: Figure 1, cropped from page 2 of the manuscript.
- `assets/observation-sinks.png` and `assets/observation-outliers.png`: Figures 2 and 3, rendered directly from pages 3 and 4 of the supplied manuscript.
- `assets/quantization-*.svg`: selected FP16 and quantized means from Table 2; narrow-screen variants use horizontal bars. Regenerate with `python3 scripts/render-result-charts.py`.
- `assets/vendor/katex/`: KaTeX 0.18.9, its fonts, and MIT license.
- `assets/logos/`: institution marks shown in the Affiliations band, in brand color and unmodified. Sources: Wikimedia Commons for Northwestern, Rutgers, Michigan, UCLA, UC San Diego, and Texas A&M; the Illinois Tech seal was supplied by the authors; `quiver.ai` for QuiverAI. Each sits in a 48x44 box (`.aff-logo`) and is fitted with `object-fit: contain`, so marks of any aspect ratio or intrinsic size can be swapped in and still fill the box. The QuiverAI file is the site icon with its light backing plate removed and the viewBox tightened to the mark, so it reads at the same size as the seals.

Running text is justified with automatic hyphenation (`.prose p`, `.step-copy p`, `.subsection-heading p`, figure captions, and the table notes). The lead paragraphs and the narrow observation sidebar stay ragged-right: at that measure a single unbreakable term such as `beginning-of-text` opens a river across the column.

Write inline math with `\(...\)` and display math with `\[...\]`. The renderer produces HTML and accessible MathML. Long equations scroll within their own region on small screens. The three displayed equations follow Sections 4.2 and 4.3 of the paper; the null posterior uses the per-head notation introduced in Section 4.3.

After editing equations, run `node scripts/check-math.cjs`, then inspect the page in a browser.

The displayed results are transcribed from Tables 2 and 3 of the manuscript supplied for this page. They are reported experimental results, not an independent reproduction. The two highlights are a relative decrease in perplexity and an absolute percentage-point gain in accuracy, with their respective baselines identified. Motivation uses the original Figures 2 and 3; their original-Transformer comparison is distinct from the Vanilla AttnResidual baseline in the result tables. Performance protocol and limitations follow Sections 6 and Appendices E-F. Unlabeled Figure 4 panels are not republished as a named before/after comparison.

The content follows Motivation → Methodology → Results → Evaluation context → Citation. The explanation structure draws on the problem/mechanism/results progression of [StreamingLLM](https://hanlab.mit.edu/projects/streamingllm) and the case-based explanations in [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). These are presentation references, not sources for OASIS experimental claims.

Affiliations and the author-to-affiliation mapping follow the `\author` block of the manuscript; author emails are deliberately not published here. Corresponding authors are marked with a dagger. Title, year, and poster status were checked against the NeurIPS OpenReview record on September 26, 2026. Haozheng Luo, Haoran Dai, and Ching-Yuen Huang are marked as equal contributors, as confirmed by the authors; Ching-Yuen Huang is listed third, ahead of the remaining OpenReview order, at the authors' request. Affiliations are omitted because they were not verified for this version. The author list in `index.html`, the `citation_author` metadata, and the BibTeX entry all use this order.

## Previous work pages

The header's **Previous work** menu (hover or keyboard focus opens it; tap toggles it on touch; Escape closes it) links to four paper sub-pages and a toolkit page, built in the same style:

| Path | Paper | Venue |
|---|---|---|
| `frost/` | FROST: Filtering Reasoning Outliers with Attention for Efficient Reasoning ([arXiv 2601.19001](https://arxiv.org/abs/2601.19001)) | ICLR 2026 |
| `boost/` | Mind the Inconspicuous: Revealing the Hidden Weakness in Aligned LLMs' Refusal Boundaries ([arXiv 2405.20653](https://arxiv.org/abs/2405.20653)) | USENIX Security 2025 |
| `germ/` | Fast and Low-Cost Genomic Foundation Models via Outlier Removal ([arXiv 2505.00598](https://arxiv.org/abs/2505.00598)) | ICML 2025 |
| `outeffhop/` | Outlier-Efficient Hopfield Layers for Large Transformer-Based Models ([arXiv 2404.03828](https://arxiv.org/abs/2404.03828)) | ICML 2024 |
| `hf-attention-normalizers/` | Toolkit: [robinzixuan/hf-attention-normalizers](https://github.com/robinzixuan/hf-attention-normalizers) | PyPI 0.1.0 |

- Each sub-page loads the shared `../styles.css`, `../script.js`, and `../assets/vendor/katex/`, and has its own `citation.bib` and `assets/`. A short inline `<style>` in each page covers page-specific details (unlinked author names, table group headers, bold best values). On sub-pages the same menu is labelled **Related work** and also links back to OASIS; the current page is marked with `aria-current="page"`. The menu in every page is generated from one list: edit `PAPERS` / `TOOLKITS` in `scripts/update-menu.py` and run `python3 scripts/update-menu.py`. A new page needs a `<ul class="nav-menu-list" id="related-work"></ul>` placeholder inside its `.nav-menu`.
- Figures are rendered from each paper's arXiv source (PDF figures rasterized with PyMuPDF and trimmed): FROST Figs. 1, 3, 4, 5; GERM Figs. 1, 2 and the first pair of appendix Fig. 3; OutEffHop Fig. 1 (source PNG) and Figs. 2–4 (cropped from PDF page 7). Numbers are transcribed from the papers' tables; headline percentages are computed from those tables and identify their baselines.
- BibTeX for GERM and OutEffHop comes from PMLR (v267 `luo25g`, v235 `hu24a`). The FROST OpenReview forum id (`a9dngZLqGS`) is taken from ML Anthology because OpenReview blocks automated fetches; the page follows the arXiv camera-ready numbers, not the earlier workshop version.
- Author names on the sub-pages are unlinked because the OpenReview profile ids were not verified. The ICML templates list every author as a correspondence contact, so no dagger is shown on GERM and OutEffHop.
- `assets/logos/rtx.svg`, `iowa-state.svg`, and `mit.svg` (Commons `File:MIT 2023 red logo.svg`) are public-domain files from Wikimedia Commons, unmodified. `ntu.svg` (en.wikipedia `File:National_Taiwan_University_seal.svg`) is a non-free file used there under fair use, chosen by the authors.
- Sub-page affiliations list institutions only, as confirmed by the authors: OutEffHop merges the paper's two Northwestern departments into one entry, and GERM lists Chenghao Qiu under Texas A&M University and Zoe Mehta under MIT at the authors' request; this differs from the paper's author block.
- BOOST: numbers follow the published USENIX version (Tables 1, 2, 6; Sections 5, 6, 8), BibTeX from the USENIX page. Figures 2, 4, 7, 10 come from the arXiv source; figures containing harmful example prompts or responses (Figs. 1, 3, 5, 6) are deliberately left out, and the page gives no attack prompts. The `*` on Jiahao Yu and Haozheng Luo is rendered as equal contribution; the paper does not define it. The code link is MAGICS-LAB/XLLM. `assets/logos/ucsb.svg` is a public-domain file from Wikimedia Commons, unmodified.
- hf-attention-normalizers: content is transcribed from the GitHub repository source and the PyPI 0.1.0 wheel as of 2026-09-26; the BibTeX is the repository's own `@software` entry. The backend table follows the code, which supports `paged|*` backends, not the older README matrix. The repository LICENSE is Apache-2.0 while `pyproject.toml`/PyPI metadata say MIT; the page shows Apache-2.0. Prose on this page is ragged-right because inline code names cannot hyphenate.

## Hosting

Website repository: https://github.com/oasis-research/oasis-research.github.io (organization `oasis-research`). Public URL: https://oasis-research.github.io/

GitHub Pages serves the root of the `main` branch. `.nojekyll` enables direct static-file serving. All local asset paths are relative, so the site works under a project subdirectory as well as a custom domain. No changes to the research-code repository or personal-homepage repository are needed.

## Attribution

Paper content and Figure 1 belong to the paper authors. The linked OpenReview record specifies CC BY 4.0. This page summarizes the paper and reproduces the architecture figure with attribution. The page layout is custom static HTML/CSS, with visual references to OpenAI's research pages and QuiverAI's restrained typography and grid. It does not bundle their source code, logos, or a third-party website template. Geist is loaded through Google Fonts with local system fallbacks.
