from module.database import Database
from module.analyzer import Analyzer


def main():
    db = Database()
    analyzer = Analyzer(db)

    print("=" * 50)
    print("TESTING AQI CALCULATION")
    print("=" * 50)

    test_values = [10, 20, 40, 100, 200, 300]

    for pm25 in test_values:
        result = analyzer.get_aqi(pm25, 0, 0)
        print(f"PM2.5: {pm25} -> AQI Category: {result}")


if __name__ == "__main__":
    main()