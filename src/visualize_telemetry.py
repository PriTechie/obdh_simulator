import csv
from datetime import datetime
import matplotlib.pyplot as plt

def visualize_telemetry(file_path='telemetry_log.csv'):
    timestamps = []
    temperatures = []
    pressures = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamps.append(datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'))
            temperatures.append(float(row['temperature']))
            pressures.append(float(row['pressure']))

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(timestamps, temperatures, marker='o', color='tomato')
    plt.title('Telemetry Data Over Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(timestamps, pressures, marker='x', color='skyblue')
    plt.xlabel('Timestamp')
    plt.ylabel('Pressure (hPa)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_telemetry()
