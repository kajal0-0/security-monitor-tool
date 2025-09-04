import psutil
import time
import re
from datetime import datetime

SUSPICIOUS_PORTS = [25, 465, 587, 1025]
SUSPICIOUS_KEYWORDS = ["nc", "ncat", "powershell", "python", "keylogger", "malware"]
PATHS_TO_WATCH = ["/tmp", "/Users/Shared", "/Users/kajal/Desktop/keylogger"]

def log_event(event_type, details):
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] [{event_type}] {details}")

def monitor_processes():
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            cmdline = " ".join(proc.info.get('cmdline') or [])
            for keyword in SUSPICIOUS_KEYWORDS:
                if re.search(keyword, cmdline, re.IGNORECASE):
                    log_event("PROCESS_ALERT", f"PID {proc.info['pid']} NAME {proc.info['name']} CMD {cmdline}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def monitor_network():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            for conn in proc.connections(kind='inet'):
                if conn.raddr and conn.raddr.port in SUSPICIOUS_PORTS:
                    log_event("NETWORK_ALERT", f"PID {proc.pid} NAME {proc.info['name']} Connected to {conn.raddr.ip}:{conn.raddr.port}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        except Exception:
            continue

def monitor_files():
    for proc in psutil.process_iter(attrs=['pid', 'open_files']):
        try:
            for f in proc.info.get('open_files') or []:
                for path in PATHS_TO_WATCH:
                    if f.path.startswith(path):
                        log_event("FILE_ALERT", f"PID {proc.pid} opened {f.path}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        except Exception:
            continue

if __name__ == "__main__":
    print("[INFO] Generic SIEM-like monitor running...")
    while True:
        monitor_processes()
        monitor_network()
        monitor_files()
        time.sleep(10)



