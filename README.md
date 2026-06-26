# Security Tools

A collection of beginner-friendly cybersecurity tools built with Python.

---

## Tools

### password_checker.py
Checks the strength of a password based on length, uppercase and lowercase letters, numbers, and special characters.

**Usage:**
python password_checker.py

Enter a password when prompted. The tool rates it as Weak, Moderate, or Strong.

---

### port_scanner.py
Scans a target IP address or hostname for open ports within a specified range.

**Usage:**
python port_scanner.py

Enter the target and port range when prompted. Open ports will be listed in the output.

---

### caesar_cipher.py
Encrypts or decrypts text using the Caesar cipher — a substitution cipher that shifts each letter by a fixed number of positions.

**Usage:**
python caesar_cipher.py

Choose to encrypt or decrypt, enter your message, then provide the shift value.

---

### zip_cracker.py
Attempts to crack a password-protected ZIP file using a wordlist (dictionary attack).

**Usage:**
python zip_cracker.py

Provide the path to the ZIP file and your wordlist. The tool tries each password until it finds a match or finishes the list.

---

### keylogger.py
Captures and logs keystrokes in real time using raw terminal input. Each key press is recorded with a timestamp to a local log file. Detects special keys including ENTER and BACKSPACE. Built using Python's tty and termios modules — no external libraries needed.

**Usage:**
python keylogger.py

Press any keys to log them. Press 'q' to end the session. Logs are saved to keylog.txt in the same directory.

---

### clipboard_monitor.py
Monitors the system clipboard at one-second intervals and logs any new content detected. Uses Termux's clipboard API, making it compatible with Android environments.

**Usage:**
python clipboard_monitor.py

The tool runs continuously and prints any new clipboard content to the terminal. Press Ctrl+C to stop. Logs are saved to clipboard_log.txt in the same directory.

---

## Requirements

- Python 3.x
- Standard libraries only — no external installs needed
- clipboard_monitor.py requires Termux with termux-api package installed

---

## Author

Built by Esema Samuel Udemeabasi
Developed on Android using Termux and Pydroid 3. No laptop. Just consistency.