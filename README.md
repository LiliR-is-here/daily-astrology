# Daily Astrology

A practical, evidence-aware daily Western astrology skill for AI agents.

**The engine computes; the agent interprets.** This project uses the open-source
[Astro engine](https://github.com/aryaminus/astro) as an optional calculation
backend and provides a focused daily-transit workflow, Chinese-language output,
interpretation guardrails, and concrete reflection prompts.

Astrology is a symbolic tradition, not a scientific forecasting method. This
project does not claim that planetary positions cause personal events or
predict outcomes.

## Current status

**v0.1 foundation** — skill instructions, data contract, calculation bootstrap,
and report conventions. The calculation backend is installed separately from
this repository so upstream code and its MIT license remain intact.

## Install

For an Agent Skills-compatible host:

```bash
npx skills add LiliR-is-here/daily-astrology
```

For a local checkout:

```bash
git clone https://github.com/LiliR-is-here/daily-astrology.git
cd daily-astrology
bash scripts/setup.sh
```

The setup script clones the upstream Astro project into `.deps/astro`. It does
not copy upstream source into this repository. Python 3.10+ and Git are required.

## Use

Ask your agent:

- “Generate my daily astrology report.”
- “What are the strongest transits to my natal chart today?”
- “Give me a short, practical reading for today.”

For a personalized reading, configure your birth date, birth time (if known),
birthplace, IANA timezone, and preferred house system in a **local-only** profile.
See [references/profile.md](references/profile.md). Never commit personal birth
data or generated private reports.

## Defaults

- Western tropical zodiac.
- Placidus houses when the calculation backend explicitly confirms support;
  otherwise report the actual house system returned and do not silently label it
  Placidus. The upstream built-in engine may use whole-sign houses.
- Psychological and practical interpretation, not deterministic prediction.
- One to three dominant themes, grounded in computed transit-to-natal factors.
- No arbitrary luck scores, percentages, lucky colors, or guaranteed events.

## Project map

- [SKILL.md](SKILL.md) — agent workflow and operating contract.
- [references/interpretation.md](references/interpretation.md) — weighting and
  synthesis rules.
- [references/report-format.md](references/report-format.md) — daily report
  format.
- [references/ethics.md](references/ethics.md) — scope and safety.
- [scripts/setup.sh](scripts/setup.sh) — install calculation backend.
- [scripts/run_engine.py](scripts/run_engine.py) — validated JSON bridge.

## Upstream acknowledgements

- [aryaminus/astro](https://github.com/aryaminus/astro), MIT License:
  optional deterministic chart/transit calculation backend. It is installed as
  a separate checkout; its copyright and license remain with its authors.
- [wvanderen/astrology-skill](https://github.com/wvanderen/astrology-skill),
  MIT License: informed the retrieval-first interpretation workflow. This
  project does not copy its source files or reference corpus.

See [NOTICE.md](NOTICE.md) for attribution and dependency boundaries.

## License

This repository's original material is licensed under the MIT License. See
[LICENSE](LICENSE). Third-party software retains its own license.
