
from module.database import Database
from module.data_simulator import DataSimulator


def main():
    print("=" * 50)
    print("TESTING DATA SIMULATOR")
    print("=" * 50)

    db = Database()

    # Test 1: Simulate one hour of data
    print("\nTest 1: Simulating one hour of data")

    simulator = DataSimulator(db)

    inserted_count = simulator.simulate_hourly_data(hours=1)

    print(f"Inserted records: {inserted_count}")
    print("Expected records: 5")

    # Test 2: Simulate 24 hours of data
    print("\nTest 2: Simulating 24 hours of data")

    inserted_count = simulator.simulate_hourly_data(hours=24)

    print(f"Inserted records: {inserted_count}")
    print("Expected records: 120")

    # Test 3: Test invalid input
    print("\nTest 3: Testing invalid input")

    try:
        simulator.simulate_hourly_data(hours=0)
    except ValueError as error:
        print(f"Validation successful: {error}")

    print("\nAll simulator tests completed.")


if __name__ == "__main__":
    main()
