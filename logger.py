from datetime import datetime

def log_message(message):
    with open("system.log", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
