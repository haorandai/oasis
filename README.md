# OASIS paper website

Project page for **Attention Sinks and Outliers in Attention Residuals**, accepted at NeurIPS 2026 (poster).

- Paper: https://openreview.net/forum?id=yjVSLVS0Dh
- Research code: https://github.com/robinzixuan/OASIS

## Local preview

This is a static website with no build step or package dependencies.

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Editing

- `index.html`: title, authors, method, result table, citation, and metadata.
- `styles.css`: typography, layout, and mobile styles.
- `script.js`: copy-citation interaction, with a manual-copy fallback.
- `citation.bib`: downloadable citation; keep it synchronized with the HTML.
- `assets/method.png`: Figure 1, cropped from page 2 of the manuscript.

The displayed results are transcribed from Table 2 of the manuscript supplied for this page. They are reported experimental results, not an independent reproduction. The two highlights are a relative decrease in perplexity and an absolute percentage-point gain in accuracy, with their respective baselines identified.

Authors, order, title, year, and poster status were checked against the NeurIPS OpenReview record on September 26, 2026. Author affiliations and contribution marks are omitted because they were not verified for this version. The BibTeX author list follows the named OpenReview author block.

## Hosting

GitHub Pages serves the root of the `main` branch. `.nojekyll` enables direct static-file serving. All local asset paths are relative, so the site works under a project subdirectory as well as a custom domain. No changes to the research-code repository or personal-homepage repository are needed.

## Attribution

Paper content and Figure 1 belong to the paper authors. The linked OpenReview record specifies CC BY 4.0. This page summarizes the paper and reproduces the architecture figure with attribution. The page layout is custom static HTML/CSS, with visual references to OpenAI's research pages and QuiverAI's restrained typography and grid. It does not bundle their source code, logos, or a third-party website template. Geist is loaded through Google Fonts with local system fallbacks.
