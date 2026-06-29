#!/usr/bin/env python3
"""Static site generator for MassageChairsTested.com.
Reads shared partials + per-page content fragments and writes full HTML pages.
Run: python3 build.py
"""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://massagechairstested.com"
UPDATED = "June 2026"

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

SPRITE = read("partials/sprite.html").strip()
HEADER = read("partials/header.html").strip()
FOOTER = read("partials/footer.html").strip()
HOME_SCHEMA = read("partials/home_schema.html").strip()

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300..600&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">')

WEBSITE = {"@type":"WebSite","@id":SITE+"/#website","url":SITE+"/","name":"MassageChairsTested.com",
           "description":"Independent, consumer-first massage chair buying guide.","inLanguage":"en-US",
           "publisher":{"@id":SITE+"/#organization"}}
ORG = {"@type":"Organization","@id":SITE+"/#organization","name":"MassageChairsTested.com","url":SITE+"/",
       "description":"An independent editorial guide that helps consumers make safer, better-informed massage chair buying decisions. We do not sell massage chairs.",
       "publishingPrinciples":SITE+"/editorial-standards/"}

def page_schema(title, desc, url, crumbs):
    webpage = {"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,
               "isPartOf":{"@id":SITE+"/#website"},"about":{"@id":SITE+"/#organization"},
               "description":desc,"inLanguage":"en-US","dateModified":"2026-06-26",
               "breadcrumb":{"@id":url+"#breadcrumb"}}
    items=[]
    for i,(name,href) in enumerate(crumbs,1):
        it={"@type":"ListItem","position":i,"name":name}
        if href: it["item"]=SITE+href
        items.append(it)
    breadcrumb={"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":items}
    graph={"@context":"https://schema.org","@graph":[WEBSITE,ORG,webpage,breadcrumb]}
    return '<script type="application/ld+json">\n'+json.dumps(graph,indent=2)+'\n</script>'

PAGE = """<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-18J1NXB880"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-18J1NXB880');
</script>
<script>document.documentElement.classList.add('js')</script>
<title>{title}</title>
<meta name="description" content="{desc_attr}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="MassageChairsTested.com">
<meta property="og:title" content="{title_attr}">
<meta property="og:description" content="{desc_attr}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://massagechairstested.com/assets/og/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_attr}">
<meta name="twitter:description" content="{desc_attr}">
<meta name="twitter:image" content="https://massagechairstested.com/assets/og/og-default.png">
{schema}
{fonts}
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
{sprite}
{header}
<main id="main" tabindex="-1">
{body}
</main>
{footer}
<script src="/assets/app.js" defer></script>
</body>
</html>
"""

def render(*, slug, title, desc, body, schema, og_type="article"):
    canonical = SITE + "/" + (slug + "/" if slug else "")
    out = PAGE.format(
        title=title, title_attr=html.escape(title, quote=True),
        desc_attr=html.escape(desc, quote=True), canonical=canonical,
        og_type=og_type, schema=schema, fonts=FONTS, sprite=SPRITE,
        header=HEADER, footer=FOOTER, body=body)
    outdir = ROOT if not slug else os.path.join(ROOT, slug)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)
    return canonical

def breadcrumb_html(crumbs):
    parts=[]
    for i,(name,href) in enumerate(crumbs):
        last = i==len(crumbs)-1
        if last or not href:
            parts.append(f'<span aria-current="page">{html.escape(name)}</span>')
        else:
            parts.append(f'<a href="{href}">{html.escape(name)}</a>')
    return '<nav class="breadcrumb container" aria-label="Breadcrumb">'+'<span class="sep">/</span>'.join(parts)+'</nav>'

def inner_body(slug, title, eyebrow, h1, lead, content_html):
    url = SITE + "/" + slug + "/"
    # build crumb trail from slug segments
    segs = slug.split("/")
    crumbs=[("Home","/")]
    # human label for the section (first segment)
    section_labels={
        "buying-guide":"Buying Guide","showroom-guide":"Showroom Guide",
        "retailer-checklist":"Retailer Checklist","medical-claims":"Medical Claims",
        "warranty-service-delivery":"Warranty, Service & Delivery","online-vs-showroom":"Online vs Showroom",
        "reviews-comparisons":"Reviews & Comparisons","local":"Local Guides",
        "editorial-standards":"Editorial Standards","review-methodology":"Review Methodology",
        "showroom-verification-methodology":"Showroom Verification","disclosure":"Disclosure",
        "medical-disclaimer":"Medical Disclaimer","correction-policy":"Correction Policy"}
    if len(segs)>1:
        sec=segs[0]
        crumbs.append((section_labels.get(sec,sec.replace("-"," ").title()), "/"+sec+"/" if False else None))
    crumbs.append((h1, None))
    bc = breadcrumb_html(crumbs)
    illu_path = os.path.join("illustrations", slug.replace("/","__")+".svg")
    text_block = (f'<div class="page-hero-text"><p class="eyebrow">{html.escape(eyebrow)}</p>'
                  f'<h1>{html.escape(h1)}</h1>'
                  f'<p class="lead">{html.escape(lead)}</p></div>')
    if os.path.exists(os.path.join(ROOT, illu_path)):
        illu = read(illu_path).strip()
        hero = (f'<header class="page-hero"><div class="container page-hero-grid">'
                f'{text_block}'
                f'<figure class="page-hero-illu reveal">{illu}</figure>'
                f'</div></header>')
    else:
        hero = (f'<header class="page-hero"><div class="container">'
                f'<p class="eyebrow">{html.escape(eyebrow)}</p>'
                f'<h1>{html.escape(h1)}</h1>'
                f'<p class="lead">{html.escape(lead)}</p></div></header>')
    body = (bc + hero +
            '<div class="section" style="padding-top:0"><div class="container">'
            '<article class="prose">' + content_html +
            f'<p class="page-updated">Last updated: {UPDATED} · '
            f'<a href="/editorial-standards/">Editorial standards</a> · '
            f'<a href="/disclosure/">Disclosure</a></p>'
            '</article></div></div>')
    schema = page_schema(title, lead, url, crumbs_for_schema(slug, h1))
    return body, schema

def crumbs_for_schema(slug, h1):
    return [("Home","/"),(h1, "/"+slug+"/")]

# ---------------- BUILD ----------------
def build():
    man = json.loads(read("pages.json"))
    # home
    render(slug="", title=man["home"]["title"], desc=man["home"]["desc"],
           body=read("content/home.html").strip(), schema=HOME_SCHEMA, og_type="website")
    count=1
    for p in man["pages"]:
        slug=p["slug"]
        cpath=os.path.join("content", slug.replace("/","__")+".html")
        content = read(cpath).strip() if os.path.exists(os.path.join(ROOT,cpath)) else "<p>Coming soon.</p>"
        body, schema = inner_body(slug, p["title"], p["eyebrow"], p["h1"], p["lead"], content)
        render(slug=slug, title=p["title"], desc=p["desc"], body=body, schema=schema)
        count+=1
    # 404 page
    nf_body = ('<header class="page-hero"><div class="container">'
               '<p class="eyebrow">Page not found</p>'
               '<h1>We couldn\'t find that page</h1>'
               '<p class="lead">The page may have moved. Here are good places to pick up your massage chair research.</p>'
               '</div></header>'
               '<div class="section" style="padding-top:0"><div class="container"><article class="prose">'
               '<div class="cta-row"><a class="btn btn--primary" href="/buying-guide/massage-chair-buying-checklist/">Use the Buying Checklist</a> '
               '<a class="btn btn--ghost" href="/">Back to the home guide</a></div>'
               '<h2>Popular guides</h2><ul>'
               '<li><a class="textlink" href="/showroom-guide/should-you-try-a-massage-chair-before-buying/">Should you try a massage chair before buying? <span class="arrow" aria-hidden="true">&rarr;</span></a></li>'
               '<li><a class="textlink" href="/retailer-checklist/how-to-choose-a-massage-chair-retailer/">How to choose a massage chair retailer <span class="arrow" aria-hidden="true">&rarr;</span></a></li>'
               '<li><a class="textlink" href="/reviews-comparisons/how-to-read-massage-chair-reviews/">How to read massage chair reviews <span class="arrow" aria-hidden="true">&rarr;</span></a></li>'
               '<li><a class="textlink" href="/online-vs-showroom/should-you-buy-a-massage-chair-online-or-in-store/">Buying online vs. in a showroom <span class="arrow" aria-hidden="true">&rarr;</span></a></li>'
               '</ul></article></div></div>')
    nf_schema = '<script type="application/ld+json">\n'+json.dumps({"@context":"https://schema.org","@graph":[WEBSITE,ORG]},indent=2)+'\n</script>'
    out = PAGE.format(title="Page not found | MassageChairsTested.com", title_attr="Page not found",
        desc_attr="The page could not be found. Browse the massage chair buying guide, showroom and retailer checklists, reviews and more.",
        canonical=SITE+"/404.html", og_type="website", schema=nf_schema, fonts=FONTS, sprite=SPRITE,
        header=HEADER, footer=FOOTER, body=nf_body)
    with open(os.path.join(ROOT,"404.html"),"w",encoding="utf-8") as f:
        f.write(out)
    # sitemap
    urls=[SITE+"/"]+[SITE+"/"+p["slug"]+"/" for p in man["pages"]]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm+=f'  <url><loc>{u}</loc><changefreq>monthly</changefreq></url>\n'
    sm+='</urlset>\n'
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(sm)
    print(f"built {count} pages + sitemap ({len(urls)} urls)")

if __name__=="__main__":
    build()
