# Private local birth profile

Create a JSON file outside this repository, for example
`~/.config/daily-astrology/profile.json`:

```json
{
  "year": 1990,
  "month": 6,
  "day": 15,
  "hour": 14,
  "minute": 30,
  "lat": 40.7128,
  "lng": -74.0060,
  "tz": "America/New_York",
  "time_known": true,
  "systems": ["western"]
}
```

The values above are fictional examples. Replace them with your own details.
Coordinates use decimal degrees (east/north positive). Use an IANA timezone.

If birth time is unknown, omit hour and minute and set `time_known` to false.
Do not provide a guessed time. A city-level birthplace is sufficient to look up
coordinates and timezone, but verify the result before use.

Do not put this file in the project directory. If you must store it nearby,
add it to `.git/info/exclude` or the repository's `.gitignore`.
