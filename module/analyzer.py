import pandas as pd
class Analyzer:
    def __init__(self, database):
        self.db = database
    def get_dataframe(self, hours=24):
        data = self.db.fetch_recent_data(hours)   
        if not data:
            return pd.DataFrame()
        df=pd.DataFrame(data,
                        columns=["region", "pm25" , "pm10" , "no2" , "co" , "timestamp"]
                        )
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    def get_aqi(self, pm25, pm10, no2):
        # Simplified AQI calculation (based on PM2.5 primarily)
         if pm25 <= 12:
            return "Good"
         elif pm25 <= 35.4:
            return "Moderate"
         elif pm25 <= 55.4:
            return "Unhealthy for Sensitive Groups"
         elif pm25 <= 150.4:
            return "Unhealthy"
         elif pm25 <= 250.4:
            return "Very Unhealthy"
         else:
            return "Hazardous"
    def get_summary_statistics(self, hours=24):
        df = self.get_dataframe(hours)
        if df.empty:
            return{}
        summary={}
        for region in df["region"].unique():
           region_data = df[df["region"]==region]
           summary[region] = {
                            "avg_pm25":region_data["pm25"].mean(),
                            "max_pm25":region_data["pm25"].max(),
                            "min_pm25":region_data["pm25"].min(),
                            "avg_pm10":region_data["pm10"].mean(),
                            "avg_no2":region_data["no2"].mean(),
                            "avg_co":region_data["co"].mean(),
                            "current_aqi":self.get_aqi(region_data["pm25"].iloc[0],
                                                       region_data["pm10"].iloc[0],
                                                       region_data["no2"].iloc[0],
                                                       ),
                             }
        return summary
    def get_most_polluted_region(self, hours=24):    
        df = self.get_dataframe(hours)
        if df.empty:
            return None, 0
        region_avg = df.groupby("region")["pm25"].mean()
        return region_avg.idxmax(), region_avg.max()
    def get_cleanest_region(self, hours=24):
        df = self.get_dataframe(hours)
        if df.empty:
            return None, 0
        else:
            region_avg = df.groupby("region")["pm25"].mean()
            return region_avg.idxmin(), region_avg.min()
    