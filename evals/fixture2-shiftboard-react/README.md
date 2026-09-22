# Shiftboard

Staff scheduling for a small cafe chain. React 18 + Tailwind, loaded from CDNs so there is no build step and nothing to install.

## Run

Babel cannot load JSX files over `file://`, so serve the folder over HTTP:

    python -m http.server 8137

Then open http://localhost:8137/#/schedule

## Routes

- `#/schedule` - this week's shifts for the current location
- `#/team` - staff list
- `#/shift/12` - shift detail / edit form (any shift id from `src/data.js`)
- `#/settings` - location and notification settings

## Layout

- `index.html` - loads React, ReactDOM, Babel standalone and the Tailwind Play CDN, plus the inline Tailwind theme
- `tailwind.config.js` - the same theme, kept for a future real build
- `src/data.js` - sample staff, shifts and helpers
- `src/components/` - shared layout and widgets
- `src/screens/` - one file per route
- `src/App.jsx` - hash router and mount
