import sys
import tty
import termios
import logging
import os
from datetime import datetime

log_file = os.path.join(os.path.dirname(__file__), "keylog.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def get_char():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

def main():
    print("=== Keylogger ===")
    print("Logging keystrokes... Press 'q' to stop.\n")

    logging.info("--- Session started ---")

    while True:
        char = get_char()
        if char == 'q':
            logging.info("--- Session ended ---")
            print(f"\nSession ended. Log saved to: {log_file}")
            break
        elif char == '\r':
            logging.info("Key pressed: ENTER")
        elif char == '\x7f':
            logging.info("Key pressed: BACKSPACE")
        else:
            logging.info(f"Key pressed: {char}")

main()