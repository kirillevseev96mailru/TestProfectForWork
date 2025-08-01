#!/usr/bin/env python

from tabulate import tabulate
from parser import parse_args, read_logs
from reports.average import AverageReport


def main():
    args = parse_args()
    entries = read_logs(args.file, args.date)

    if args.report == "average":
        report = AverageReport(entries)
        rows = report.generate()
        print(tabulate(
            rows,
            headers=["handler", "total", "avg_response_time"],
            tablefmt="github"
        ))


if __name__ == "__main__":
    main()
