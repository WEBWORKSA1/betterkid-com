# BetterKid.com

**The parent's toolkit for ages 3–12** — a fully static, monetization-ready website: 8 interactive tools, evidence-based guides, a daily Wonder question, gated printables, video hub, gift guides, and complete operations pages (support/donate, sponsor/advertise, contests, careers). Built to run on the **free GitHub Pages plan** with zero backend.

Live: `https://webworksa1.github.io/betterkid-com/` (custom domain: add a `CNAME` file containing `betterkid.com` and point DNS).

## Structure
```
index.html, ages/, guides/, tools/, wonder/, videos/, printables/, gift-guides/,
join/, support/, sponsor/, contests/, careers/, about/, contact/, search/, legal/
assets/css/style.css      design system (light + dark)
assets/js/config.js       ← ALL settings: contact (base64), AdSense ID, YouTube IDs, donation links, Amazon tag, GA4
assets/js/app.js          shared runtime (forms, personalisation, ads, video, search, wonder)
assets/js/tools.js        the 8 interactive tools
data/wonders.json         Wonder-of-the-day dataset (42 entries; add more)
build/                    Python generator — edit pages here, then `python3 build/build.py`
docs/RESEARCH.md          39-site competitive research + concept decision
docs/BUILD-PROMPT-PHASES.md  phase-wise build prompt / roadmap
```

## Editing
* Change settings → `assets/js/config.js` (no rebuild needed).
* Change page content → edit `build/pages_*.py`, run `python3 build/build.py`, commit the regenerated HTML.
* Add a guide → add an `article(...)` call in `build/pages_guides.py` and a row in `GUIDES` in `build/pages_core.py`.
* Add a tool → add logic in `assets/js/tools.js` and a `tool_page(...)` in `build/pages_tools.py`.

## Contact & forms
The single contact address is stored base64-encoded in `config.js` and injected at runtime; it never appears in plain text. Forms relay via FormSubmit.co — the **first submission triggers a one-time activation email** to that inbox; click the link once and all forms go live.

## Monetization switches (`config.js`)
`adsenseClient` (also update `ads.txt`), `youtube.featured[].id`, `support.*` donation links, `amazonTag`, `analytics.ga4`.

## Deploy
Pushing to `main` runs `.github/workflows/pages.yml` which enables and deploys GitHub Pages. If the first run reports Pages is not enabled, open **Settings → Pages → Source: GitHub Actions** once and re-run.

## Legal
See `legal/trademark.html` for the trademark & copyright notice. "BetterKid" is used descriptively; no affiliation with any other organisation using a similar name.
