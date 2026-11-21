# Digital Slate Database website

Static site for the GameSlate, BookSlate, StringSlate and JamSlate Android apps. English at `/`, Brazilian Portuguese at `/pt/`.
Live: https://gameslate-blip.github.io/digitalslate/

## Pages
- `/` and `/pt/`: studio home with the app chooser (cards with screenshots)
- `/<app>/` and `/pt/<app>/`: app page (hero, screenshots, features)
- `/<app>/privacy/` and `/<app>/terms/`: legal pages (and in Portuguese under `/pt/`, from `content/legal/pt/`)
- `app-ads.txt`: AdMob seller file; must be served from the root of the developer-website domain (currently served from the old repo gameslate-blip/gameslate-blip.github.io; keep it there)
- `sitemap.xml`, `404.html`, `assets/style.css`, `assets/img/` (icons + screenshots, webp)

## Where the site is published (two copies, same content)
- **Main site: https://gameslate-blip.github.io/** (repo gameslate-blip/gameslate-blip.github.io, cloned at ~/Projects/gameslate-blip.github.io). Canonical URLs point here.
- **Copy: https://gameslate-blip.github.io/digitalslate/** (this repo). It must stay: Google Play listings and the apps link to its privacy pages.
- Old GameSlate links `/#privacy` and `/#terms` on the main site jump to the GameSlate policy pages (small script on the home page).
- `app-ads.txt` lives in the root repo only (the domain root is where AdMob looks for it).

## How to change it
The HTML is generated. Edit `tools/build_site.py` (texts for every app in EN and PT, layout) or `content/legal/**` (the legal text), then run both builds and commit and push BOTH repos:

    python3 tools/build_site.py                                                  # this repo (the /digitalslate/ copy)
    python3 tools/build_site.py --root-site --out ../gameslate-blip.github.io   # the main site (writes sitemap.xml too)

Do not edit the generated HTML by hand.

- New app: add it to `APPS` and `ORDER` in the script, put its icon and screenshots in `assets/img/`, add `content/legal/<app>-privacy.html` and `-terms.html` (and the `pt/` versions).
- Google Play button: there is a comment `Add the Google Play button here` in `app_page()`; add the link when an app is published.
- Screenshots: 450x800 webp, made from the apps' `play-store/screenshots/`.
- Custom domain later: add a `CNAME` file to the root repo and change `SITE` in the script.

Play Store privacy URLs (must not change): `https://gameslate-blip.github.io/<app>/privacy/` (and the older `/digitalslate/<app>/privacy/` keep working).
