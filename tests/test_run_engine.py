import importlib.util
import json
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "run_engine.py"
SPEC = importlib.util.spec_from_file_location("run_engine", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def write_profile(tmp_path, data):
    path = tmp_path / "profile.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_profile_requires_location_and_timezone(tmp_path):
    path = write_profile(tmp_path, {"year": 1990, "month": 1, "day": 1})
    try:
        module.load_profile(path)
    except ValueError as exc:
        assert "lat" in str(exc)
    else:
        raise AssertionError("Expected missing required fields to fail")


def test_unknown_birth_time_removes_hour_and_minute(tmp_path):
    path = write_profile(tmp_path, {
        "year": 1990, "month": 1, "day": 1,
        "hour": 12, "minute": 30,
        "lat": 1.3, "lng": 103.8, "tz": "Asia/Singapore",
        "time_known": False, "systems": ["western"]
    })
    profile = module.load_profile(path)
    assert "hour" not in profile
    assert "minute" not in profile


def test_non_western_system_is_rejected(tmp_path):
    path = write_profile(tmp_path, {
        "year": 1990, "month": 1, "day": 1,
        "lat": 1.3, "lng": 103.8, "tz": "Asia/Singapore",
        "systems": ["western", "vedic"]
    })
    try:
        module.load_profile(path)
    except ValueError as exc:
        assert "Western mode only" in str(exc)
    else:
        raise AssertionError("Expected unsupported system to fail")
