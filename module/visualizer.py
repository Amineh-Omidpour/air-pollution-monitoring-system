import os
from datetime import datetime
import matplotlib.pyplot as plt
from module.analyzer import Analyzer

class Visualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.output_dir = "plots"
        os.makedirs(self.output_dir , exist_ok = True)
    def plot_pm25_trend(self, hours = 24):
        df = self.analyzer.get_dataframe(hours)
        if df.empty:
            print(f"NO data is available for plotting.")
            return
        plt.figure(figsize=(12,6))
        for region in df["region"].unique():
            region_data = df[df["region"]==region]
            plt.plot(
                region_data["timestamp"],
                region_data["pm25"], 
                label = region, 
                marker = "o",
                )
        plt.axhline(
            y=35.4,
            color = "orange",
            linestyle = "--",
            label = "Moderate threshold"
        )
        plt.axhline(
            y = 55.4,
            color = "red",
            linestyle = "--",
            label = "Unhealthy for Sensitive Groups"
        )
        plt.title("PM2.5 Trend by Region")
        plt.xlabel("Time")
        plt.ylabel("PM2.5 Concentration")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation = 45)
        plt.tight_layout()
        
        filename = f"pm25_trend_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)

        plt.savefig(filepath)
        plt.close()
        print(f"PM2.5 trend plot saved: {filepath}")

    def plot_comparison(self, hours = 24):
        df = self.analyzer.get_dataframe(hours)    
        if df.empty:
            print("No data available for plotting.")
            return
        averages = df.groupby("region")[["pm25", "pm10", "no2"]].mean()
        plt.figure(figsize=(12,6))
        averages.plot( kind = "bar")
        plt.title("Average Pollutant Levels by Region")
        plt.xlabel("Region")
        plt.ylabel("Average Concentration")
        plt.legend(title="Pollutants")
        filename = f"pollutant_comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath)
        plt.close()
        print(f"Comparison plot saved: {filepath}")

    def plot_hourly_heatmap(self, hours = 24):
        df = self.analyzer.get_dataframe(hours)
        if df.empty:
            print("No data available for plotting.")
            return
        df["hour"] = df["timestamp"].dt.hour
        heatmap_data = df.pivot_table(
          index="region",
          columns="hour",
          values="pm25",
          aggfunc="mean"
        )
        plt.figure(figsize=(12,6))
        plt.imshow(heatmap_data, aspect="auto", cmap="YlOrRd")
        plt.xticks(
            range(len(heatmap_data.columns)),
            heatmap_data.columns
                            )
        plt.yticks(
            range(len(heatmap_data.index)),
            heatmap_data.index
        )
        plt.title("Hourly PM2.5 Heatmap by Region")
        plt.xlabel("Hour of Day")
        plt.ylabel("Region")
        plt.colorbar(label="PM2.5 Concentration")
        filename = f"Hourly_heat_map_{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
        filepath = os.path.join (self.output_dir, filename)
        plt.savefig(filepath)
        plt.close()
        print(f"Hourly heatmap saved: {filepath}")
        
        


        
    





