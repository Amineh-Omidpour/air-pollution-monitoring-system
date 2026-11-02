from datetime import datetime, timedelta
import random

class DataSimulator:
    def __init__(self, database):
        self.db = database

        self.regions = ["North", "South", "East", "West", "Central"]

        # Base pollution levels for each region (µg/m³)
        self.base_levels = {
            "North": {"pm25": 55, "pm10": 100, "no2": 40, "co": 5},
            "South": {"pm25": 35, "pm10": 70, "no2": 30, "co": 3},
            "East": {"pm25": 70, "pm10": 120, "no2": 55, "co": 7},
            "West": {"pm25": 45, "pm10": 85, "no2": 35, "co": 4},
            "Central": {"pm25": 80, "pm10": 140, "no2": 60, "co": 8},
        }

    def simulate_hourly_data(self, hours=24):
        if not isinstance(hours, int) or isinstance(hours, bool) or hours <= 0:
            raise ValueError("hours must be a positive integer.")

        current_time = datetime.now()
        readings_batch = []

        for hour_offset in range(hours):
            timestamp = current_time - timedelta(hours=hour_offset)

            for region in self.regions:
                base = self.base_levels[region]

                hour_of_day = timestamp.hour

                # Rush-hour effect
                if (8 <= hour_of_day <= 10) or (18 <= hour_of_day <= 20):
                    time_factor = 1.3

                # Night-time effect
                elif hour_of_day >= 23 or hour_of_day <= 5:
                    time_factor = 0.7

                else:
                    time_factor = 1.0

                # Weekend effect
                is_weekend = timestamp.weekday() >= 5
                weekend_factor = 0.8 if is_weekend else 1.0

                pm25 = max(
                    0,
                    base["pm25"] * time_factor * weekend_factor
                    + random.uniform(-10, 15),
                )

                pm10 = max(
                    0,
                    base["pm10"] * time_factor * weekend_factor
                    + random.uniform(-15, 20),
                )

                no2 = max(
                    0,
                    base["no2"] * time_factor * weekend_factor
                    + random.uniform(-5, 10),
                )

                co = max(
                    0,
                    base["co"] * time_factor * weekend_factor
                    + random.uniform(-1, 2),
                )

                readings_batch.append(
                    (
                        region,
                        round(pm25, 2),
                        round(pm10, 2),
                        round(no2, 2),
                        round(co, 2),
                        timestamp,
                    )
                )

        inserted_count = self.db.insert_many_readings(readings_batch)

        print(
            f"Simulated {len(readings_batch)} readings "
            f"for the past {hours} hours."
        )

        return inserted_count
