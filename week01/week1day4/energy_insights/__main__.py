""" runs functions from csv utils file."""
import argparse

from csv_utils import (compute_daily_averages,
                                       detect_anomalies, find_spikes, load_csv)


def main():
    """this function is an entry point"""
    parser = argparse.ArgumentParser(description="Energy Insights CLI")

    parser.add_argument("--file", required=True, help="path to CSV file")
    parser.add_argument(
        "--top", type=int, default=10, help="number o spikes to show(default: 10)"
    )
    parser.add_argument(
        "--metric", default="price", help="column to analyze(default: price)"
    )

    args = parser.parse_args()

    rows = load_csv(args.file)
    if not rows:
        print("Error: csv file is empty.")
        return

    if args.metric not in rows[0]:
        print(f"error: column '{args.metric}' not found")
        return

    averages = compute_daily_averages(rows, "timestamp", args.metric)

    spikes = find_spikes(rows, args.metric, args.top)

    anomalies, threshold = detect_anomalies(rows, args.metric)
    

    # dispaly daily averages
    print("\nDaily Averages:")
    print("Date:         Avg Price:")
    for date, average in sorted(averages.items()):
        print(f"{date}    ${average:.2f}")

    # display top N spikes
    print(f"\nTop {args.top} Price Spikes:")

    for row in spikes:
        print(f"{row['timestamp']} " f"${float(row[args.metric]):.2f}")

    # Display anomalies
    
    print("\nAnamoly Detetction:")
    print(f"Anamolies detected: {len(anomalies)} hours")
    print(f"{row['timestamp']}" f"(95th percentile threshold): {threshold}")
  


if __name__ == "__main__":
    main()
