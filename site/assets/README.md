# Brand assets

Use the **Sebastian Software** variant of the company brand system.
The checked-in vectors are unchanged assets from the `sebastian-software/`
directory in `sebastian-software/sebastian-brand`, revision
`4985cb83ee450e6bce08081ddd4e760a1f27dfdc`:

- `brand/software-on-light.svg` and `favicon.svg`: `icon-software-light-transparent.svg`
- `brand/software-on-dark.svg`: `icon-software-dark-transparent.svg`
- `brand/logo-software.svg`: `logo-software-transparent.svg`

The local names describe the background on which each icon is used. Keep the
original geometry, proportions, and colors. Use the existing wordmark or icon;
do not invent an initials mark for the Skills site.

The site palette uses Software's Midnight, Teal, Lagoon, Signal, and Frost
colors, with lighter and darker surface/text tones for accessible contrast.
The upstream brand system owns the brand definitions.

Generate the PNG and ICO fallbacks and the social preview with the existing
Playwright dependency and Chrome:

```sh
node scripts/render-site-assets.mjs
```

Run from the repository root after installing the development dependencies.
Set `CHROME_BIN` if Chrome is not at a known platform path. The social preview
uses the original wordmark and keeps inventory counts on the homepage.
