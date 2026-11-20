# Digital Slate Database website

Static site (no build step) for the GameSlate, BookSlate and StringSlate Android apps.

- `/` studio hub
- `/gameslate/`, `/gameslate/privacy/`, `/gameslate/terms/`
- `/bookslate/`, `/bookslate/privacy/`, `/bookslate/terms/`
- `/stringslate/`, `/stringslate/privacy/`, `/stringslate/terms/`
- `app-ads.txt` AdMob seller file; must be served from the root of the developer-website domain
- `assets/style.css` shared styles

All page links are relative, so the site works on a project URL and on a custom domain.
Custom domain: add a `CNAME` file containing the domain. 404.html uses root paths, so it only renders fully on a custom domain.

Play Store privacy URLs: `<domain>/gameslate/privacy/`, `<domain>/bookslate/privacy/` and `<domain>/stringslate/privacy/`.
