from datetime import datetime

def log_action(action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("lib/logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {action}\n")
