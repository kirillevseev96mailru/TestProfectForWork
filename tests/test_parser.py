import sys
import json
import pytest
from log_parser import parse_args, read_logs


def test_parse_args_minimal(monkeypatch):
    monkeypatch.setattr(sys, "argv",
                        ["main.py", "--file", "a.log", "--report", "average"])
    args = parse_args()
    assert args.file == ["a.log"]
    assert args.report == "average"
    assert args.date is None


def test_read_logs_without_date(tmp_path):
    log = tmp_path / "l.log"
    data = [
        {"@timestamp":"2025-01-01T00:00:00+00:00", "url": "/x", "response_time": 0.1},
        {"@timestamp":"2025-01-01T00:01:00+00:00", "url": "/y", "response_time": 0.2}
    ]
    log.write_text("\n".join(json.dumps(e) for e in data),
                   encoding="utf-8")

    entries = read_logs([str(log)])
    assert len(entries) == 2
    assert entries[0]["url"] == "/x"
    assert pytest.approx(entries[1]["response_time"], rel=1e-6) == 0.2


def test_read_logs_with_date(tmp_path):
    log = tmp_path / "l2.log"
    data = [
        {"@timestamp":"2025-01-01T00:00:00+00:00", "url": "/x", "response_time": 0.1},
        {"@timestamp":"2025-01-02T00:00:00+00:00", "url": "/y", "response_time": 0.2}
    ]
    log.write_text("\n".join(json.dumps(e) for e in data),
                   encoding="utf-8")

    entries = read_logs([str(log)], date_filter="2025-01-01")
    assert len(entries) == 1
    assert entries[0]["url"] == "/x"
