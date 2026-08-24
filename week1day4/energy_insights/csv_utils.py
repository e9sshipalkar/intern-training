"""
    Module name: csv_utils.py
"""

import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List


def load_csv(file_path: str) -> List[Dict[str, str]]:
    """Load and validate rows from a CSV file."""
    rows = []
    with open(Path(file_path), newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00"))
                float(row["price"])
                rows.append(row)
            except (ValueError, TypeError, KeyError) as error:
                print("Invalid row:", row)
                print("Error:", error)
                continue
        return rows


def summarize_numeric(rows: List[Dict[str, str]], column: str) -> Dict[str, float]:
    """Return min, max and avg of values."""
    values = [float(row[column]) for row in rows]

    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
    }


def top_n(rows: List[Dict[str, str]], column: str, n: int) -> List[Dict[str, str]]:
    """Return top n records sorted by column passed."""
    return sorted(rows, key=lambda row: float(row[column]), reverse=True)[:n]


def compute_daily_averages(rows, ts_col, value_col):
    """calculates the average values for each date."""
    daily_values = {}
    for row in rows:  # get only the date part: YYYY-MM-DD
        date = row[ts_col][:10]

        value = float(row[value_col])  # covert the value from string to numbers

        if date not in daily_values:
            daily_values[date] = []

        daily_values[date].append(value)

    averages = {}
    for date, values in daily_values.items():
        averages[date] = sum(values) / len(values)

    return averages


def find_spikes(rows, value_col, top):
    """return the rows with highest vlues"""
    sorted_rows = sorted(
        rows,
        key=lambda row: float(row[value_col]),
        reverse=True,
    )
    return sorted_rows[:top]


def detect_anomalies(rows, value_col):
    """find value at or above the 95th percentile"""
    values = [float(row[value_col]) for row in rows]
    threshold = sorted(values)[int(len(values) * 0.95)]
    anomalies = [row for row in rows if float(row[value_col]) >= threshold]
    return anomalies, threshold
