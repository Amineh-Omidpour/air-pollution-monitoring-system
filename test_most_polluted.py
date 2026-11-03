from module.database import Database
from module.analyzer import Analyzer
def main():
    db = Database()
    analyzer = Analyzer(db)
    print("=" * 50)
    print("Testing most polluted region")
    print("=" * 50)
    region, avg_pm25 = analyzer.get_most_polluted_region(hours=24)
    if region is None:
        print("no data is available")
    else:
        print(f"most polluted region:{region}")
        print(f"Average PM2.5: {avg_pm25:.2f}")

if __name__=="__main__":
    main()      