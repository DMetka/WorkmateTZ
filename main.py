import argparse
from parser import parse_log_file
from report import get_report_class
from tabulate import tabulate
import sys



def main():
    parser = argparse.ArgumentParser(description="Log report generator")
    parser.add_argument("--file", nargs='+', required=True)
    parser.add_argument("--report", required=True, choices=['average'])
    parser.add_argument("--date")
    args = parser.parse_args()

    try:
        entries = []
        for file_path in args.file:
            entries += parse_log_file(file_path, date_filter=args.date)

        report_class = get_report_class(args.report)
        report = report_class(entries)
        table = report.generate()

        print(tabulate(table, headers="keys"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
