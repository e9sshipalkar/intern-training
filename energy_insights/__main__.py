import argparse

def main():
    parser = argparse.ArgumentParser(description="Energy Insights CLI")

    parser.add_argument("--file", help="CSV file path")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--metric", help="column to analyze")

    args = parser.parse_args()

    print("Energy Insights CLI")
    print("File:" , args.file)
    print("Top:" , args.top)
    print("Metric:" , args.metric) 

if __name__ == "__main__":
    main()