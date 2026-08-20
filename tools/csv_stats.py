import argparse
import csv
from pathlib import Path
from typing import Dict, List


def load_csv(file_path: str) -> List[Dict[str, str]]:
    with open(Path(file_path), newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def summarize_numeric(rows: List[Dict[str, str]], column: str) -> Dict[str, float]:
    values = [float(row[column]) for row in rows]

    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
    }


def top_n(rows: List[Dict[str, str]], column: str, n: int) -> List[Dict[str, str]]:
    return sorted(rows, key=lambda row: float(row[column]), reverse=True)[:n]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--metric", required=True)

    args = parser.parse_args()

    rows = load_csv(args.file)

    if not rows:
        print("Error: csv file is empty.")
        return

    if args.metric not in rows[0]:
        print(f"error: column '{args.metric}' not found")
        return

    summary = summarize_numeric(rows, args.metric)

    print(f"Row count: {len(rows)}")
    print(f"\n{args.metric} statistics:")
    print(f"min: {summary['min']}")
    print(f"max: {summary['max']}")
    print(f"mean: {summary['mean']}")

    top_rows = top_n(rows, args.metric, args.top)
    print(f"\nTop {args.top} rows by {args.metric}:")

    for row in top_rows:
        print(row)


if __name__ == "__main__":
    main()
