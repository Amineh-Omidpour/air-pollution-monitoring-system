from module.database import Database
from module.analyzer import Analyzer
def main():
    db = Database()
    analyzer = Analyzer(db)
    print("=" * 50)
    print("Testing summary statistics")
    print("=" * 50)
    summary = analyzer.get_summary_statistics(hours=24)
    
    if not summary:
        print("No data available")
        return
    print("Available regions:", list(summary.keys()))
    for region,stats in summary.items():
        print(f"\nRegion= {region}")
        for key, value in stats.items():
            if isinstance(value, (int,float)):
                print(f"{key}={value:.2f}")
            else:
                print(f"{key}={value}")


if __name__ == "__main__":
    main()