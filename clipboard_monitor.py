import subprocess
import time
import logging
import os
from datetime import datetime

log_file = os.path.join(os.path.dirname(__file__), "clipboard_log.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def get_clipboard():
    try:
        result = subprocess.run(
            ["termux-clipboard-get"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return None

def main():
    print("=== Clipboard Monitor ===")
    print("Monitoring clipboard... Press Ctrl+C to stop.\n")

    logging.info("--- Session started ---")
    last_content = ""

    try:
        while True:
            current = get_clipboard()
            if current and current != last_content:
                print(f"New clipboard content detected: {current}")
                logging.info(f"Clipboard: {current}")
                last_content = current
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("--- Session ended ---")
        print(f"\nMonitoring stopped. Log saved to: {log_file}")

main()