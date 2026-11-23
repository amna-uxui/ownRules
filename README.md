# Lived

A clickable prototype for adults with hypermobile Ehlers-Danlos syndrome (hEDS) to capture what happens in their body, made accessible for days with brain fog, dizziness and painful hands.

DXDS3 · My Own Rules: Building Tools.

**Open it on your phone:** https://amna-uxui.github.io/ownRules/

Tip: on iPhone, tap Share → Add to Home Screen to open it full screen, like an app.

## What it is now: your history + Your hEDS

The app opens on **Your last 8 weeks**: each column is a week (newest on the right), each day a small four-colour square. Drag to magnify, tap a day to see the days like it. **Fill in today** opens your map in Today mode: tap what you feel, then Save today.


The condition as a grid. Every common hEDS symptom is a square in one of four colours (energy and mind, dizziness and heart, pain, body reactions). Tap a square to make it yours; its card explains why it happens in hEDS and the squares it often comes with gather next to it. Add your own, tie squares together, switch to **Mine** to see only your map, and use **••• → Share my map** for a clean poster to show a doctor. The map is saved on the device (localStorage) and survives a reload.

The earlier tracker version is kept in `src/archive/lived-tracker.html`.

## Test routes

Add a hash to the address:

| Hash | Shows |
|---|---|
| `#splash` | Logo animation, then the intro |
| `#intro` | Intro screen |
| `#history` | Your last 8 weeks (main screen) |
| `#today` | Your map in Today mode |
| `#map` | Your hEDS (your saved map) |
| `#mine` | Mine view (sample map if yours is empty) |
| `#symptom-dz` | A sample map with the card for *Dizzy when standing* open (any id works, e.g. `#symptom-jp`) |
| `#add` | The "Add your own" sheet |
| `#share` | The poster (sample map if yours is empty) |
| `#demo` | A sample map with eight squares claimed |

Sample routes (`#demo`, `#symptom-…`, and `#mine` / `#share` when your map is empty) never overwrite your saved map.

## Build

Edit `src/lived.html`, then run `python3 build.py` to regenerate `index.html`.
