import time

def apply_config(config_file='config.txt'):
    config = {}
    try:
        with open(config_file, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=')
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        return "No configuration file found."

    # Simulate applying config
    print("Applying configuration...")
    time.sleep(1)
    for key, value in config.items():
        print(f"  - {key} set to {value}")
    return "Configuration applied successfully."

if __name__ == "__main__":
    result = apply_config()
    print(result)
