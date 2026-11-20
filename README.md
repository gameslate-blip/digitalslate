# Digital Slate Database website

Static site for the GameSlate, BookSlate and StringSlate Android apps. English at `/`, Brazilian Portuguese at `/pt/`.
Live: https://gameslate-blip.github.io/digitalslate/

## Pages
- `/` and `/pt/`: studio home with the app chooser (cards with screenshots)
- `/<app>/` and `/pt/<app>/`: app page (hero, screenshots, features)
- `/<app>/privacy/` and `/<app>/terms/`: legal pages, English only (the Portuguese app pages link to them and say so)
- `app-ads.txt`: AdMob seller file; must be served from the root of the developer-website domain (currently served from the old repo gameslate-blip/gameslate-blip.github.io; keep it there)
- `sitemap.xml`, `404.html`, `assets/style.css`, `assets/img/` (icons + screenshots, webp)

## How to change it
The HTML is generated. Edit `tools/build_site.py` (texts for every app in EN and PT, layout) or `content/legal/*.html`
(the legal text), then run `python3 tools/build_site.py` and commit the generated files. Do not edit the generated HTML by hand.

- New app: add it to `APPS` and `ORDER` in the script, put its icon and screenshots in `assets/img/`, add `content/legal/<app>-privacy.html` and `-terms.html`.
- Google Play button: there is a comment `Add the Google Play button here` in `app_page()`; add the link when an app is published.
- Screenshots: 450x800 webp, made from the apps' `play-store/screenshots/`.

All page links are relative, so the site works on a project URL and on a custom domain.
Custom domain: add a `CNAME` file containing the domain and change `SITE` in the script. `404.html` uses the `/digitalslate/` prefix; change it when the domain changes.

Play Store privacy URLs (must not change): `<site>/gameslate/privacy/`, `<site>/bookslate/privacy/`, `<site>/stringslate/privacy/`.
