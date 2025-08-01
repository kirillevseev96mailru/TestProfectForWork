from collections import defaultdict
from .base import Report


class AverageReport(Report):
    """
    Отчёт average: группирует по url, считает
    общее число запросов и среднее время ответа.
    """
    def generate(self):
        stats = defaultdict(lambda: {"count": 0, "total_time": 0.0})
        for rec in self.entries:
            url = rec["url"]
            rt  = rec["response_time"]
            stats[url]["count"] += 1
            stats[url]["total_time"] += rt

        rows = []
        for url, info in stats.items():
            avg = info["total_time"] / info["count"]
            rows.append([url, info["count"], round(avg, 3)])
        # сортируем по убыванию количества запросов
        rows.sort(key=lambda x: x[1], reverse=True)
        return rows
