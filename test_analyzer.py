
from module.database import Database
from module.analyzer import Analyzer


def main():
    db = Database()
    analyzer = Analyzer(db)

    print("=" * 50)
    print("TESTING ANALYZER")
    print("=" * 50)

    df = analyzer.get_dataframe(hours=24)
    print("\nRecords per region:")
    print(df["region"].value_counts())

    print("\nDataFrame:")
    print(df.head())

    print("\nDataFrame information:")
    df.info()

    print(f"\nTotal records: {len(df)}")


if __name__ == "__main__":
    main()
