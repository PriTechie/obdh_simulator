import random
import time

def read_temperature():
    return round(random.uniform(-40, 85), 2)  # typical range for satellite sensors

def read_pressure():
    return round(random.uniform(950, 1050), 2)  # in hPa

def collect_data():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    temp = read_temperature()
    pressure = read_pressure()
    return {
        "timestamp": timestamp,
        "temperature": temp,
        "pressure": pressure
    }

if __name__ == "__main__":
    for _ in range(5):
        data = collect_data()
        print(data)
        time.sleep(1)
