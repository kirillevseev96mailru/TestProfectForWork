import pytest
from src.reports.average import AverageReport


def test_report_average_simple():
    entries = [
        {"url": "/a", "response_time": 0.1},
        {"url": "/a", "response_time": 0.3},
        {"url": "/b", "response_time": 0.2},
    ]
    rows = AverageReport(entries).generate()
    # Должно быть две строки, первая — /a
    assert rows[0][0] == "/a"
    assert rows[0][1] == 2
    assert pytest.approx(rows[0][2], rel=1e-3) == 0.2
    # Вторая — /b
    assert rows[1][0] == "/b"
    assert rows[1][1] == 1
    assert pytest.approx(rows[1][2], rel=1e-3) == 0.2
