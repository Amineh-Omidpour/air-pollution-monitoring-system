from module.database import Database
from module.analyzer import Analyzer


def main():
    db = Database()
    analyzer = Analyzer(db)

    print("=" * 50)
    print("TESTING COMPLETE ANALYZER")
    print("=" * 50)

    # Get DataFrame
    df = analyzer.get_dataframe(hours=24)
    print("\nTotal records:", len(df))

    # Get AQI
    print("\nAQI TEST:")
    print("PM2.5 = 40:", analyzer.get_aqi(40, 0, 0))

    # Get summary statistics
    print("\nSUMMARY STATISTICS:")
    summary = analyzer.get_summary_statistics(hours=24)

    for region, stats in summary.items():
        print(f"{region}: Average PM2.5 = {stats['avg_pm25']:.2f}")

    # Most polluted region
    print("\nMOST POLLUTED REGION:")
    region, value = analyzer.get_most_polluted_region(hours=24)
    print(f"{region}: {value:.2f}")

    # Cleanest region
    print("\nCLEANEST REGION:")
    region, value = analyzer.get_cleanest_region(hours=24)
    print(f"{region}: {value:.2f}")


if __name__ == "__main__":
    main()