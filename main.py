import time
from monitor import get_system_usage
from logger import log_message
from alert import send_email_alert
import config

def check_thresholds(data):
    alerts = []

    if data["cpu"] > config.CPU_THRESHOLD:
        alerts.append(f"CPU high: {data['cpu']}%")
    if data["ram"] > config.RAM_THRESHOLD:
        alerts.append(f"RAM high: {data['ram']}%")
    if data["disk"] > config.DISK_THRESHOLD:
        alerts.append(f"Disk high: {data['disk']}%")

    return alerts

def main():
    print("Monitoring started...")

    while True:
        usage = get_system_usage()
        alerts = check_thresholds(usage)

        status = f"CPU: {usage['cpu']}%, RAM: {usage['ram']}%, DISK: {usage['disk']}%"
        print(status)
        log_message(status)

        if alerts:
            for alert in alerts:
                print("WARNING:", alert)
                log_message("WARNING: " + alert)

            if config.EMAIL_ALERT:
                send_email_alert("\n".join(alerts))

        time.sleep(config.CHECK_INTERVAL)

if __name__ == "__main__":
    main()
