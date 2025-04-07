import csv
from datetime import datetime

def get_latest_telemetry():
    try:
        with open('telemetry_log.csv', 'r') as file:
            lines = file.readlines()
            return lines[-1].strip() if len(lines) > 1 else "No telemetry data found."
    except FileNotFoundError:
        return "Telemetry log not found."

def reset_telemetry_log():
    with open('telemetry_log.csv', 'w') as file:
        file.write("timestamp,temperature,pressure\n")
    return "Telemetry log has been reset."

def handle_command(cmd):
    cmd = cmd.upper()
    if cmd == "STATUS":
        return get_latest_telemetry()
    elif cmd == "RESET":
        return reset_telemetry_log()
    elif cmd == "PING":
        return f"PONG - System is alive! ({datetime.now()})"
    elif cmd == "HELP":
        return "Available commands: STATUS, RESET, PING, HELP"
    else:
        return "Unknown command. Type HELP to see available commands."

if __name__ == "__main__":
    while True:
        user_input = input("Enter command: ")
        print(handle_command(user_input))
