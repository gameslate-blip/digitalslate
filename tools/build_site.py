#!/usr/bin/env python3
"""Builds the static site (English at /, Portuguese at /pt/) from one template.

Run from the repo root:  python3 tools/build_site.py
Legal text lives in content/legal/<app>-<privacy|terms>.html (English only, kept as written).
Everything else is defined below. The generated HTML is committed; GitHub Pages serves it as is.
"""
import os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://gameslate-blip.github.io/digitalslate"
EMAIL = "gameslate@proton.me"

# --- apps -------------------------------------------------------------------------------
APPS = {
    "gameslate": dict(
        name=("Game", "Slate"), accent="#b7f36b", shots=["gameslate-1", "gameslate-3", "gameslate-4", "gameslate-5"],
        en=dict(kind="PC games", tagline="Find your next great game.",
                blurb="Discover PC games with player activity, reviews and Linux compatibility context, all in one place.",
                hero="Find your next<br><em>great game.</em>", eyebrow="A better way to explore PC games",
                lead="GameSlate brings useful game-discovery information together, helping you explore PC games, player activity, reviews and Linux compatibility.",
                feats=[("Discover", "Explore games", "Search games and browse featured categories, details and similar titles using Steam Store data."),
                       ("Community", "Player activity & reviews", "Player counts and review summaries from the Steam Web API, plus feeds and trends from SteamData.dev."),
                       ("Linux", "Compatibility context", "Linux compatibility summaries and community reports provided by ProtonDB.")],
                note="GameSlate does not require an account. Favorites are stored locally on your device. Developed by Digital Slate Database (Raphael Lira); not affiliated with Valve Corporation, ProtonDB or SteamData.dev. Steam is a trademark of Valve Corporation."),
        pt=dict(kind="Jogos de PC", tagline="Encontre seu próximo grande jogo.",
                blurb="Descubra jogos de PC com atividade de jogadores, avaliações e contexto de compatibilidade com Linux, tudo em um só lugar.",
                hero="Encontre seu próximo<br><em>grande jogo.</em>", eyebrow="Um jeito melhor de explorar jogos de PC",
                lead="O GameSlate reúne informações úteis para descobrir jogos, ajudando você a explorar jogos de PC, atividade de jogadores, avaliações e compatibilidade com Linux.",
                feats=[("Descobrir", "Explore jogos", "Pesquise jogos e navegue por categorias, detalhes e títulos parecidos, usando dados da loja Steam."),
                       ("Comunidade", "Atividade e avaliações", "Número de jogadores e resumos de avaliações da API web da Steam, além de tendências do SteamData.dev."),
                       ("Linux", "Contexto de compatibilidade", "Resumos de compatibilidade com Linux e relatos da comunidade, fornecidos pelo ProtonDB.")],
                note="O GameSlate não exige conta. Os favoritos ficam salvos no seu aparelho. Desenvolvido pela Digital Slate Database (Raphael Lira); sem afiliação com a Valve Corporation, o ProtonDB ou o SteamData.dev. Steam é marca da Valve Corporation."),
    ),
    "bookslate": dict(
        name=("Book", "Slate"), accent="#f3c46b", shots=["bookslate-1", "bookslate-3", "bookslate-4"],
        en=dict(kind="Books", tagline="Read 15. Get 3 great ones.",
                blurb="Tell it up to 15 books you've read and get 3 suggestions for what to read next. English and Portuguese.",
                hero="Read 15.<br>Get <em>3 great ones.</em>", eyebrow="Book suggestions, simplified",
                lead="Tell BookSlate up to 15 books you've read and it suggests 3 you'll probably love next. Available in English and Portuguese.",
                feats=[("1 · Add", "Your books", "Search and add up to 15 books you've read."),
                       ("2 · Match", "Smart suggestions", "BookSlate looks at the subjects and popularity of what you read to find books you haven't."),
                       ("3 · Discover", "3 picks", "Get three focused suggestions, plus a Home tab with categories, trending and new releases.")],
                note="BookSlate does not require an account. Book data and covers come from <a href=\"https://openlibrary.org\" target=\"_blank\" rel=\"noopener\">Open Library</a>. BookSlate is independent and not affiliated with Open Library or the Internet Archive."),
        pt=dict(kind="Livros", tagline="Leu 15? Receba 3 ótimos.",
                blurb="Diga até 15 livros que você leu e receba 3 sugestões do que ler em seguida. Em português e inglês.",
                hero="Leu 15.<br>Receba <em>3 ótimos.</em>", eyebrow="Sugestões de livros, sem complicação",
                lead="Diga ao BookSlate até 15 livros que você já leu e ele sugere 3 que você provavelmente vai adorar. Disponível em português e inglês.",
                feats=[("1 · Adicione", "Seus livros", "Pesquise e adicione até 15 livros que você leu."),
                       ("2 · Combine", "Sugestões inteligentes", "O BookSlate analisa os assuntos e a popularidade do que você leu para achar livros que você ainda não leu."),
                       ("3 · Descubra", "3 escolhas", "Receba três sugestões objetivas, além de uma aba Início com categorias, livros em alta e lançamentos.")],
                note="O BookSlate não exige conta. Os dados e as capas dos livros vêm do <a href=\"https://openlibrary.org\" target=\"_blank\" rel=\"noopener\">Open Library</a>. O BookSlate é independente e não é afiliado ao Open Library nem ao Internet Archive."),
    ),
    "stringslate": dict(
        name=("String", "Slate"), accent="#66c0f4", shots=["stringslate-1", "stringslate-2", "stringslate-3", "stringslate-4"],
        pt_shots=["stringslate-pt-1", "stringslate-pt-2", "stringslate-pt-3", "stringslate-pt-4"],
        en=dict(kind="Guitar", tagline="Tune it. Set it up. Play.",
                blurb="A guitar tuner and step-by-step setup guides for acoustic and electric guitar, with an intonation helper. English and Portuguese.",
                hero="Tune it.<br>Set it up. <em>Play.</em>", eyebrow="Guitar tuner and setup guides",
                lead="A tuner and step-by-step setup guides for acoustic and electric guitar. Available in English and Portuguese, in portrait and landscape.",
                feats=[("1 · Tune", "A tuner that listens", "Nine tunings, an adjustable A4 reference, automatic string detection and a note you can play to tune by ear."),
                       ("2 · Set up", "Illustrated guides", "Strings, neck relief, string action, nut, intonation and pickup height, with typical values, tools and safety warnings."),
                       ("3 · Check", "Intonation helper", "Play the open string, then the 12th fret. StringSlate tells you how many cents off you are and which way to move the saddle.")],
                note="StringSlate does not require an account. The microphone is used only while the tuner is on screen; the sound is analysed on your phone and is never recorded or sent anywhere. Setup values are typical references; follow your guitar maker's specifications and take the guitar to a technician if you are unsure."),
        pt=dict(kind="Guitarra e violão", tagline="Afine. Regule. Toque.",
                blurb="Afinador e guias de regulagem passo a passo para violão e guitarra, com assistente de oitavação. Em português e inglês.",
                hero="Afine.<br>Regule. <em>Toque.</em>", eyebrow="Afinador e guias de regulagem",
                lead="Um afinador e guias de regulagem passo a passo para violão e guitarra. Disponível em português e inglês, em retrato e em paisagem.",
                feats=[("1 · Afine", "Um afinador que escuta", "Nove afinações, referência de A4 ajustável, detecção automática da corda e uma nota para tocar e afinar de ouvido."),
                       ("2 · Regule", "Guias ilustrados", "Cordas, curvatura do braço, altura das cordas, pestana, oitavação e altura dos captadores, com valores típicos, ferramentas e avisos de segurança."),
                       ("3 · Confira", "Assistente de oitavação", "Toque a corda solta e depois o 12º traste. O StringSlate diz quantos cents você está fora e para que lado mover o selim.")],
                note="O StringSlate não exige conta. O microfone só é usado enquanto o afinador está na tela; o som é analisado no seu celular e nunca é gravado nem enviado. Os valores de regulagem são referências típicas; siga as especificações do fabricante e leve o instrumento a um técnico se tiver dúvida."),
    ),
}
ORDER = ["gameslate", "bookslate", "stringslate"]

# --- interface texts ----------------------------------------------------------------------
UI = {
    "en": dict(
        lang="en", home="Home", apps="Apps", about="About", contact="Contact", other="PT", other_label="Português",
        studio_eyebrow="Digital Slate Database", studio_h1="Small apps for<br><em>what's next.</em>",
        studio_lead="Independent Android apps for your next game, your next book and your next tune. No accounts, no clutter.",
        pick_eyebrow="Choose an app", pick_h2="Pick a slate.", details="See the app", privacy="Privacy", terms="Terms",
        shots_h="Screenshots", feats_eyebrow="What's inside", more_h="More from Digital Slate", more_eyebrow="Other apps",
        support="Support", legal_en="", policy="Privacy policy", termsfull="Terms of use", back="All apps",
        dev_eyebrow="About the developer", dev_h2="Made by one person.",
        dev_p="Digital Slate Database is Raphael Lira, an independent developer based in Cotia, São Paulo, Brazil.",
        dev_p2="Questions or privacy requests:", tagline="Small, useful apps for Android.", rights="© 2026 Digital Slate Database. All rights reserved.",
        site_desc="Digital Slate Database makes GameSlate, BookSlate and StringSlate: independent Android apps for games, books and guitars.",
        facts=["No accounts", "Free with ads", "Made in Brazil"],
    ),
    "pt": dict(
        lang="pt-BR", home="Início", apps="Apps", about="Sobre", contact="Contato", other="EN", other_label="English",
        studio_eyebrow="Digital Slate Database", studio_h1="Apps pequenos para<br><em>o que vem a seguir.</em>",
        studio_lead="Apps Android independentes para seu próximo jogo, seu próximo livro e sua próxima música. Sem contas, sem bagunça.",
        pick_eyebrow="Escolha um app", pick_h2="Escolha uma slate.", details="Ver o app", privacy="Privacidade", terms="Termos",
        shots_h="Capturas de tela", feats_eyebrow="O que tem dentro", more_h="Mais da Digital Slate", more_eyebrow="Outros apps",
        support="Suporte", legal_en=" (em inglês)", policy="Política de privacidade", termsfull="Termos de uso", back="Todos os apps",
        dev_eyebrow="Sobre o desenvolvedor", dev_h2="Feito por uma pessoa.",
        dev_p="A Digital Slate Database é Raphael Lira, desenvolvedor independente de Cotia, São Paulo, Brasil.",
        dev_p2="Dúvidas ou pedidos de privacidade:", tagline="Apps pequenos e úteis para Android.", rights="© 2026 Digital Slate Database. Todos os direitos reservados.",
        site_desc="A Digital Slate Database faz o GameSlate, o BookSlate e o StringSlate: apps Android independentes para jogos, livros e guitarra.",
        facts=["Sem contas", "Grátis com anúncios", "Feito no Brasil"],
    ),
}

FAVICON = ('<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E'
           '%3Crect width=%2764%27 height=%2764%27 rx=%2714%27 fill=%27%231b2838%27/%3E%3Cpath d=%27M14 40a18 18 0 0 1 36 0%27 fill=%27none%27 '
           'stroke=%27%2366c0f4%27 stroke-width=%278%27 stroke-linecap=%27round%27/%3E%3Cpath d=%27M32 40l8-18%27 stroke=%27%239bcb3b%27 '
           'stroke-width=%278%27 stroke-linecap=%27round%27/%3E%3C/svg%3E">')


def rel(frm: str, to: str) -> str:
    """Relative URL from page path `frm` ('' or 'gameslate/privacy/') to `to` (same style, from site root)."""
    f = [p for p in frm.split("/") if p]
    up = "../" * len(f)
    return (up + to) or "./"


def brand(app):
    a, b = APPS[app]["name"]
    return f'{a}<span>{b}</span>'


def page(path, lang, title, desc, body, accent=None, alt_path=None, extra_head=""):
    """path: page location from site root ('' for home, 'pt/bookslate/' ...)."""
    t = UI[lang]
    base_path = path[3:] if lang == "pt" else path          # path of the English twin
    en_path = base_path
    pt_path = "pt/" + base_path
    other_path = alt_path or (pt_path if lang == "en" else en_path)
    style = f' style="--accent:{accent}"' if accent else ""
    home = "pt/" if lang == "pt" else ""
    nav = (f'<a class="brand" href="{rel(path, home)}">Digital<span>Slate</span></a>'
           f'<nav aria-label="Main"><a href="{rel(path, home)}#apps">{t["apps"]}</a>'
           f'<a href="{rel(path, home)}#about">{t["about"]}</a><a href="{rel(path, home)}#contact">{t["contact"]}</a>'
           f'<a class="lang" href="{rel(path, other_path)}" hreflang="{"pt-BR" if lang=="en" else "en"}" lang="{"pt-BR" if lang=="en" else "en"}" title="{t["other_label"]}">{t["other"]}</a></nav>')
    footer_apps = " &nbsp;·&nbsp; ".join(f'<a href="{rel(path, home + a + "/")}">{"".join(APPS[a]["name"])}</a>' for a in ORDER)
    canon = f'{SITE}/{path}'
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e131a">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{SITE}/{en_path}">
<link rel="alternate" hreflang="pt-BR" href="{SITE}/{pt_path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}">
{FAVICON}
<link rel="stylesheet" href="{rel(path, "assets/style.css")}">
{extra_head}</head>
<body{style}>
<header><div class="wrap bar">{nav}</div></header>
<main>
{body}
</main>
<footer><div class="wrap foot">
<div><strong class="brand">Digital<span>Slate</span> Database</strong><br>{t["tagline"]}</div>
<div>{footer_apps}<br>{t["rights"]}</div>
</div></footer>
</body>
</html>
'''


def img(path_from, name, alt, w=450, h=800, lazy=True):
    lz = ' loading="lazy"' if lazy else ""
    return f'<img src="{rel(path_from, "assets/img/" + name + ".webp")}" alt="{alt}" width="{w}" height="{h}"{lz}>'


def app_card(path, lang, app):
    t, a = UI[lang], APPS[app]
    c = a[lang]
    home = "pt/" if lang == "pt" else ""
    shots = a["pt_shots"] if (lang == "pt" and "pt_shots" in a) else a["shots"]
    peeks = "".join(f'<span class="peek">{img(path, s, "")}</span>' for s in shots[:3])
    return f'''<article class="appcard" style="--accent:{a["accent"]}">
  <div class="top">{img(path, app + "-icon", "", 192, 192)}<div><div class="kind">{c["kind"]}</div><h3><a class="stretch" href="{rel(path, home + app + "/")}">{brand(app)}</a></h3></div></div>
  <p class="tg">{c["tagline"]}</p><p>{c["blurb"]}</p>
  <div class="peeks" aria-hidden="true">{peeks}</div>
  <div class="links"><span class="go">{t["details"]} →</span><span class="sub"><a href="{rel(path, app + "/privacy/")}">{t["privacy"]}</a> · <a href="{rel(path, app + "/terms/")}">{t["terms"]}</a>{t["legal_en"]}</span></div>
</article>'''


def home_page(lang):
    t = UI[lang]
    path = "pt/" if lang == "pt" else ""
    cards = "".join(app_card(path, lang, a) for a in ORDER)
    facts = "".join(f"<li>{f}</li>" for f in t["facts"])
    body = f'''<div class="wrap hero">
  <div class="eyebrow">{t["studio_eyebrow"]}</div>
  <h1>{t["studio_h1"]}</h1>
  <p class="lead">{t["studio_lead"]}</p>
  <ul class="facts">{facts}</ul>
</div>
<section id="apps"><div class="wrap">
  <div class="eyebrow">{t["pick_eyebrow"]}</div><h2>{t["pick_h2"]}</h2>
  <div class="apps">{cards}</div>
</div></section>
<section id="about"><div class="wrap two">
  <div><div class="eyebrow">{t["dev_eyebrow"]}</div><h2>{t["dev_h2"]}</h2></div>
  <div><p>{t["dev_p"]}</p><p id="contact">{t["dev_p2"]} <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
</div></section>'''
    return page(path, lang, "Digital Slate Database" + (" | Small apps for Android" if lang == "en" else " | Apps pequenos para Android"), t["site_desc"], body)


def app_page(lang, app):
    t, a = UI[lang], APPS[app]
    c = a[lang]
    home = "pt/" if lang == "pt" else ""
    path = home + app + "/"
    shots = a["pt_shots"] if (lang == "pt" and "pt_shots" in a) else a["shots"]
    gallery = "".join(f'<figure class="shot">{img(path, s, c["tagline"])}</figure>' for s in shots)
    feats = "".join(f'<article class="card"><div class="tag">{x}</div><h3>{y}</h3><p>{z}</p></article>' for x, y, z in c["feats"])
    more = "".join(app_card(path, lang, o) for o in ORDER if o != app)
    body = f'''<div class="wrap hero app">
  <div class="herotext">
    <a class="crumb" href="{rel(path, home)}#apps">← {t["back"]}</a>
    <div class="eyebrow">{c["eyebrow"]}</div>
    <h1>{c["hero"]}</h1>
    <p class="lead">{c["lead"]}</p>
    <div class="actions">
      <!-- Add the Google Play button here once the listing is published. -->
      <a class="btn secondary" href="{rel(path, app + "/privacy/")}">{t["policy"]}{t["legal_en"]}</a>
      <a class="btn secondary" href="{rel(path, app + "/terms/")}">{t["termsfull"]}{t["legal_en"]}</a>
    </div>
  </div>
  <div class="heroshot"><div class="icon">{img(path, app + "-icon", "", 192, 192, lazy=False)}</div></div>
</div>
<section><div class="wrap">
  <div class="eyebrow">{t["shots_h"]}</div>
  <div class="gallery">{gallery}</div>
</div></section>
<section><div class="wrap">
  <div class="eyebrow">{t["feats_eyebrow"]}</div>
  <div class="grid">{feats}</div>
  <p class="note">{c["note"]}</p>
  <p class="note">{t["support"]}: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
<section><div class="wrap">
  <div class="eyebrow">{t["more_eyebrow"]}</div><h2>{t["more_h"]}</h2>
  <div class="apps two">{more}</div>
</div></section>'''
    return page(path, lang, f'{"".join(a["name"])} | {c["tagline"]}', c["blurb"], body, accent=a["accent"])


def legal_page(app, kind):
    a = APPS[app]
    path = f"{app}/{kind}/"
    text = (ROOT / "content" / "legal" / f"{app}-{kind}.html").read_text()
    name = "".join(a["name"])
    title = f'{name} {"Privacy Policy" if kind == "privacy" else "Terms of use"}'
    desc = f'{"Privacy policy" if kind == "privacy" else "Terms of use"} for the {name} Android app.'
    body = f'''<section class="legal"><div class="wrap policy">
<a class="crumb" href="{rel(path, app + "/")}">← {name}</a>
{text}
</div></section>'''
    # No Portuguese legal pages (the legal text stays in English): the PT switch goes to the Portuguese app page.
    return page(path, "en", title, desc, body, accent=a["accent"], alt_path=f"pt/{app}/")


def write(path, html):
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def main():
    write("", home_page("en"))
    write("pt", home_page("pt"))
    for app in ORDER:
        write(app, app_page("en", app))
        write("pt/" + app, app_page("pt", app))
        for kind in ("privacy", "terms"):
            write(f"{app}/{kind}", legal_page(app, kind))
    urls = [""] + [f"{a}/" for a in ORDER] + [f"{a}/{k}/" for a in ORDER for k in ("privacy", "terms")]
    urls += ["pt/"] + [f"pt/{a}/" for a in ORDER]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"<url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    # 404 page: project sites are served under /digitalslate/, so it needs absolute paths.
    (ROOT / "404.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Digital Slate Database</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="/digitalslate/assets/style.css"></head>
<body><main><div class="wrap hero"><div class="eyebrow">404</div><h1>Page not found.</h1>
<p class="lead">That page does not exist. Pick an app instead.</p>
<div class="actions"><a class="btn primary" href="/digitalslate/">Digital Slate Database</a><a class="btn secondary" href="/digitalslate/pt/">Português</a></div></div></main></body></html>
''')
    print("built", len(urls), "pages")


if __name__ == "__main__":
    main()
