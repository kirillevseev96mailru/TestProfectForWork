import sys
import json
import pytest
from src.main import main


def test_cli_prints_table(tmp_path, capsys, monkeypatch):
    # Подготавливаем временный лог-файл
    log = tmp_path / "l.log"
    entries = [
        {"@timestamp":"2025-01-01T00:00:00+00:00","url":"/a","response_time":0.1},
        {"@timestamp":"2025-01-01T00:01:00+00:00","url":"/b","response_time":0.2},
    ]
    log.write_text("\n".join(json.dumps(e) for e in entries),
                   encoding="utf-8")

    # Симулируем запуск скрипта
    monkeypatch.setattr(sys, "argv",
                        ["main.py", "--file", str(log), "--report", "average"])
    main()

    out = capsys.readouterr().out
    assert "handler" in out
    assert "/a" in out and "/b" in out
