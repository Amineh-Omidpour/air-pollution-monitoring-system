from module.database import Database
from module.analyzer import Analyzer
from module.visualizer import Visualizer

def main():
    db = Database()
    analyzer = Analyzer(db)
    visualyzer = Visualizer(analyzer)
    print("Testing pm25 trend plot...")
    visualyzer.plot_pm25_trend(hours = 24)
    print("Testing comparison plot...")
    visualyzer.plot_comparison(hours=24)
    print("Testing hourly heatmap...")
    visualyzer.plot_hourly_heatmap(hours=24)

if __name__=="__main__":
    main()

