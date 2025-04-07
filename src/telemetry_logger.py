import csv
import time
import random
from datetime import datetime
import os

TELEMETRY_FILE = "telemetry_data.csv"
ERROR_LOG_FILE = "error_log.csv"

def generate_telemetry():
    """Simulate telemetry data for temperature and pressure."""
    temperature = round(random.uniform(-50, 100), 2)
    pressure = round(random.uniform(900, 1100), 2)
    return temperature, pressure

def log_error(message):
    """Write an error message to the error log with timestamp."""
    try:
        with open(ERROR_LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp, message])
    except Exception as e:
        print(f"[LOGGER ERROR] Failed to write to error log: {e}")

def init_csv_file(file_path, headers):
    """Ensure the telemetry CSV file has headers."""
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

def main():
    print("[STARTED] Telemetry logger is running. Press Ctrl+C to stop.")
    init_csv_file(TELEMETRY_FILE, ['timestamp', 'temperature', 'pressure'])
    init_csv_file(ERROR_LOG_FILE, ['timestamp', 'error_message'])

    try:
        with open(TELEMETRY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            while True:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temperature, pressure = generate_telemetry()
                writer.writerow([timestamp, temperature, pressure])
                file.flush()  # Ensure immediate writing to disk
                print(f"{timestamp}, {temperature}°C, {pressure} hPa")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOPPED] Telemetry logging manually interrupted.")
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()


