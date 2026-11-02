from datetime import datetime
from module.database import Database
db = Database()
#Test vaid input
print("Testing a valid input:")
rows = db.fetch_recent_data(hours=24)
print(f"Number of readings found:{len(rows)}")
#Test an invalid input
print("\nTesting invalid input:")
try:
    rows = db.fetch_recent_data(hours=-5)
except ValueError as error:
    print(f"Vlaidation worked: {error}")
