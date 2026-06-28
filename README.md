# MassageChairsTested.com

An independent, premium, consumer-first **editorial buying guide** for massage chairs.
It does not sell chairs — it helps buyers compare comfort, body fit, showrooms, retailers,
reviews, warranty, service, delivery, medical-sounding claims and brands before they buy.

Static site, built with a tiny Python generator. Design system: **"The Quiet Field Guide."**

## Structure
| Path | What |
|---|---|
| `index.html` + `<section>/<slug>/index.html` | Built pages (18 total) |
| `assets/styles.css`, `assets/app.js` | Shared stylesheet + JS |
| `partials/` | Shared header, footer, icon sprite, home schema |
| `content/` | Per-page article HTML fragments (source) |
| `illustrations/` | Per-page inline-SVG hero illustrations (source) |
| `pages.json` | Page manifest (slug, title, meta description, h1, lead) |
| `build.py` | Static generator → pages + `sitemap.xml` + `404.html` |
| `image-briefs.md` | Photo production prompts (optional atmospheric images) |
| `homepage-plan.md`, `visual-direction.md` | Strategy & creative-direction docs |

## Build
```bash
python3 build.py        # regenerates all pages, sitemap.xml
python3 -m http.server 4599   # preview at http://localhost:4599/
```

## Notes
- Compliance: brand-neutral (no rankings/ratings), medically cautious (no treatment claims), no ecommerce/sales styling.
- SEO: one H1 per page, unique titles (≤60) & meta descriptions (≤155), canonical, BreadcrumbList + FAQPage (on guide pages, matching visible content), sitemap, robots.
