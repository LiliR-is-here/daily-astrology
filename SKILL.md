---
name: daily-astrology
description: Generate grounded, practical daily Western tropical astrology readings from calculated current transits and a user's natal chart. Use when the user asks for today's horoscope, daily astrology, current transits, or a practical reflection based on their birth chart.
---

# Daily Astrology Skill

## Purpose

Produce a concise, thoughtful daily reading by combining verified astronomical calculations with a restrained symbolic interpretation. The aim is reflection and agency, not prediction.

**Non-negotiable:** never invent planetary positions, natal placements, houses, aspects, or transit timing. If calculation is unavailable, say so and offer a clearly labelled general Sun-sign-level reflection only when the user wants one.

## Required inputs

For a personalized transit-to-natal reading, obtain:

- Birth date (YYYY-MM-DD).
- Birth time and confidence (exact / approximate / unknown).
- Birth city or latitude/longitude.
- IANA timezone for the birth location.
- House system preference (default Placidus only if the engine confirms it; otherwise use the engine's actual supported/default system and disclose it).

For today's sky-only reading, no birth data is required. Determine the user's intended local date and timezone; if unavailable, ask which date/timezone to use. Do not infer a timezone from language.

Keep birth details in a local, untracked profile. Never ask for sensitive details that are unnecessary for the requested reading.

## Calculation workflow

1. Read `references/data-contract.md`.
2. Check whether the upstream Astro engine is installed at `.deps/astro/skills/astrology/scripts/astro_engine.py`.
3. Run `python3 scripts/run_engine.py --profile /path/to/private-profile.json --date YYYY-MM-DD` for a natal transit report, or use `--sky-only` for a sky-only calculation.
4. Inspect the returned JSON. Confirm `_meta`, date, timezone, house system, backend and precision note.
5. If the engine fails, returns malformed data, omits required fields, or cannot support the requested house system, do not fill gaps by intuition. State the limitation and narrow the reading.

The bridge is a thin adapter. Its command-line interface is documented in `scripts/run_engine.py`. Upstream engine source is not vendored here.

## Interpretation workflow

1. Identify the user's explicit focus, if any.
2. Rank calculated factors using `references/interpretation.md`.
3. Select at most three dominant themes. Prefer repeated, tight, relevant transit-to-natal contacts over a long list of weak signals.
4. Distinguish long-duration background transits from short-lived triggers (especially the Moon and fast inner planets).
5. Translate symbolism into plausible areas of attention, choices, conversations, routines, or emotional tone. Do not claim a transit caused an event or symptom.
6. Offer one or two low-burden actions and one observation question.
7. Apply `references/ethics.md` and format with `references/report-format.md`.

## Weighting principles

- User's explicit question and relevant natal factors come first.
- Tight aspects to natal Sun, Moon, personal planets, Ascendant/MC (only if birth time is reliable) are usually more personally salient.
- Saturn, Jupiter, Uranus, Neptune and Pluto can describe longer background chapters; do not automatically treat every outer-planet contact as important.
- Mars, Venus and Mercury can describe shorter activation windows.
- Moon transits are brief and should not dominate a whole-day or weekly reading unless the user asks for a moment-specific reading.
- Consider applying/separating status, orb, duration, repetition and house-system reliability when those fields are actually supplied.
- Weighting is an editorial prioritization method, not a probability, severity, or scientific effect score.

## Output

Follow `references/report-format.md`. Default language is Chinese when the user speaks Chinese; otherwise match the user's language. Keep the reading direct, specific to the calculated data, and free of generic flattery.

## Missing data and uncertainty

- Unknown birth time: do not interpret Ascendant, MC, houses, or house-based topics as known.
- Approximate birth time: mark angle/house interpretations as uncertain.
- Missing location/timezone: do not calculate a personalized chart until clarified.
- Incomplete engine output: interpret only verified fields and state the scope.
- Never silently change zodiac, house system, coordinates, timezone, or date.
