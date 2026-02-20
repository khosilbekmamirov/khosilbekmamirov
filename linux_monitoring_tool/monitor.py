import psutil
import time
from datetime import datetime

LOG_FILE = "system_usage.log"

def log_usage():
    with open(LOG_FILE, "a") as f:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent
            net = psutil.net_io_counters()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"{timestamp} | CPU: {cpu}% | MEM: {mem}% | DISK: {disk}% | SENT: {net.bytes_sent} | RECV: {net.bytes_recv}\n"
            print(log_line, end="")
            f.write(log_line)
            time.sleep(5)

if __name__ == "__main__":
    log_usage()
