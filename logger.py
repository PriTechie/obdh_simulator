import csv
import time
from sensor_simulation import collect_data

def log_data(filename="telemetry_log.csv", duration=5):
    # Open the CSV file in write mode and set up the CSV writer
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['timestamp', 'temperature', 'pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        print("Logging data to", filename)
        # Collect and log data for the specified duration (in seconds)
        for _ in range(duration):
            data = collect_data()
            writer.writerow(data)
            print("Logged:", data)
            time.sleep(1)

if __name__ == "__main__":
    log_data()
