import time
import subprocess
import os

LOG_FILE = "error.log"

def check_error():
    if not os.path.exists(LOG_FILE):
        return False

    with open(LOG_FILE, "r") as f:
        content = f.read().lower()

    return "zero" in content or "error" in content

def auto_fix():
    print("Error detected! Triggering fix process...")

    # Simulated AI fix step
    subprocess.run(["python", "mcp_server.py"])

while True:
    print("Monitoring logs...")

    if check_error():
        auto_fix()
        break

    time.sleep(3)