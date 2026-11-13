# Calculation data contract

The upstream Astro engine accepts JSON through its CLI. The documented command
shape is:

```bash
python3 <engine-path>/astro_engine.py --json '<json-input>'
```

The upstream README documents required date fields, latitude, longitude and
IANA timezone; optional hour/minute; and transit mode with a transit date.
The exact returned schema may evolve, so consumers must inspect actual output.

## Required validation before interpretation

- Process exits successfully.
- Standard output parses as one JSON object.
- Output contains a meaningful chart/transit result, not only an error.
- Returned date corresponds to the requested local date.
- Timezone, coordinates, zodiac and house system are not silently substituted.
- Personal transit reading includes natal chart factors and transit-to-natal
  aspects, or the agent clearly narrows the scope.
- Unknown birth time is represented as unknown; no fabricated angles/houses.

## House-system caveat

The upstream documentation describes the built-in engine as using whole-sign
houses in its Western reference, and says Placidus may require the optional
Swiss Ephemeris backend. Therefore this project does not promise Placidus.
Report the actual engine metadata and returned house system. Do not infer that
installing a package succeeded or that Placidus was used without evidence.

## Precision caveat

Use the engine's `_meta.engine_backend` and `precision_note` if present.
Never describe the result as Swiss-Ephemeris precision unless the metadata
confirms that backend. Do not assume that a deterministic calculation is
equivalent to scientific validation of astrological interpretation.

## Local profile format

See `references/profile.md`. Keep the profile outside the repository. A
sample with fictional values may be used in tests, but never use real personal
data in committed examples.
