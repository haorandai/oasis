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
- `script.js`: LaTeX rendering and the copy-citation interaction, with a manual-copy fallback.
- `citation.bib`: downloadable citation; keep it synchronized with the HTML.
- `assets/method.png`: Figure 1, cropped from page 2 of the manuscript.
- `assets/observation-sinks.png` and `assets/observation-outliers.png`: Figures 2 and 3, rendered directly from pages 3 and 4 of the supplied manuscript.
- `assets/quantization-*.svg`: selected FP16 and quantized means from Table 2; narrow-screen variants use horizontal bars. Regenerate with `python3 scripts/render-result-charts.py`.
- `assets/vendor/katex/`: KaTeX 0.18.9, its fonts, and MIT license.

Write inline math with `\(...\)` and display math with `\[...\]`. The renderer produces HTML and accessible MathML. Long equations scroll within their own region on small screens. The three displayed equations follow Sections 4.2 and 4.3 of the paper; the null posterior uses the per-head notation introduced in Section 4.3.

After editing equations, run `node scripts/check-math.cjs`, then inspect the page in a browser.

The displayed results are transcribed from Tables 2 and 3 of the manuscript supplied for this page. They are reported experimental results, not an independent reproduction. The two highlights are a relative decrease in perplexity and an absolute percentage-point gain in accuracy, with their respective baselines identified. Motivation uses the original Figures 2 and 3; their original-Transformer comparison is distinct from the Vanilla AttnResidual baseline in the result tables. Performance protocol and limitations follow Sections 6 and Appendices E-F. Unlabeled Figure 4 panels are not republished as a named before/after comparison.

The content follows Motivation → Methodology → Results → Evaluation context → Citation. The explanation structure draws on the problem/mechanism/results progression of [StreamingLLM](https://hanlab.mit.edu/projects/streamingllm) and the case-based explanations in [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). These are presentation references, not sources for OASIS experimental claims.

Title, year, and poster status were checked against the NeurIPS OpenReview record on September 26, 2026. Haozheng Luo, Haoran Dai, and Ching-Yuen Huang are marked as equal contributors, as confirmed by the authors; Ching-Yuen Huang is listed third, ahead of the remaining OpenReview order, at the authors' request. Affiliations are omitted because they were not verified for this version. The author list in `index.html`, the `citation_author` metadata, and the BibTeX entry all use this order.

## Hosting

Website repository: https://github.com/oasis-research/oasis-research.github.io (organization `oasis-research`). Public URL: https://oasis-research.github.io/

GitHub Pages serves the root of the `main` branch. `.nojekyll` enables direct static-file serving. All local asset paths are relative, so the site works under a project subdirectory as well as a custom domain. No changes to the research-code repository or personal-homepage repository are needed.

## Attribution

Paper content and Figure 1 belong to the paper authors. The linked OpenReview record specifies CC BY 4.0. This page summarizes the paper and reproduces the architecture figure with attribution. The page layout is custom static HTML/CSS, with visual references to OpenAI's research pages and QuiverAI's restrained typography and grid. It does not bundle their source code, logos, or a third-party website template. Geist is loaded through Google Fonts with local system fallbacks.
