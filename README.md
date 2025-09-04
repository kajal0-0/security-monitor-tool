
# Security Monitoring Tool

## Notes
- This project is **for educational purposes only**.

## Overview
A Python-based SIEM-like tool to monitor system processes, network connections, and file access in real-time. Suspicious activity is detected based on predefined keywords, ports, and paths, with structured alerts logged for analysis. Tested using a safe sample keylogger script for educational purposes.

## Features
- Real-time monitoring of:
  - Processes for suspicious keywords
  - Network connections to suspicious ports
  - File access in sensitive directories
- Structured alert logging with timestamps
- Lightweight, educational, and extendable

## Setup
1. Clone the repository:
```bash
git clone https://github.com/<your-username>/security-monitor-tool.git
cd security-monitor-tool
```
2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the monitoring tool:
```bash
python monitor.py
```

## Testing
- Use the `test samples/` folder to run safe sample keylogger scripts for monitoring tests.
- Logs will display alerts for any matching suspicious activity.




