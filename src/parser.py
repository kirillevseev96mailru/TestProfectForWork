import argparse
import json
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Генерирует отчёт по JSON-логам"
    )
    parser.add_argument(
        "--file", "-f",
        nargs="+",
        required=True,
        help="Путь(и) к одному или нескольким лог-файлам"
    )
    parser.add_argument(
        "--report", "-r",
        choices=["average"],
        required=True,
        help="Тип отчёта (пока только 'average')"
    )
    parser.add_argument(
        "--date", "-d",
        help="Фильтр по дате YYYY-MM-DD (опционально)"
    )
    return parser.parse_args()


def read_logs(file_paths, date_filter=None):
    """
    Читает все JSON-строки из каждого файла в file_paths,
    по необходимости фильтрует по date_filter и возвращает список dict.
    """
    entries = []
    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if date_filter:
                    ts = datetime.fromisoformat(data["@timestamp"])
                    if ts.date().isoformat() != date_filter:
                        continue
                entries.append(data)
    return entries
