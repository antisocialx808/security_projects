# Security Projects

A collection of Python security tools built and run entirely on Android using Termux and Pydroid 3. No laptop. Just consistency.

---

## Tools

### password_checker.py
Checks password strength based on length, character variety, and verifies against known data breaches using the HaveIBeenPwned API.

**Usage:**
python password_checker.py

---

### port_scanner.py
Scans a target IP or hostname for open ports within a specified range using multithreading.

**Usage:**
python port_scanner.py

---

### caesar_cipher.py
Encrypts or decrypts text using the Caesar cipher — a classic substitution cipher that shifts letters by a fixed value.

**Usage:**
python caesar_cipher.py

---

### zip_cracker.py
Attempts to crack a password-protected ZIP file using a wordlist (dictionary attack).

**Usage:**
python zip_cracker.py

---

### keylogger.py
Captures and logs keystrokes within a terminal session. Demonstrates how credential-stealing malware operates.

**Usage:**
python keylogger.py
(Press 'q' to stop)

---

### clipboard_monitor.py
Monitors and logs clipboard content in real time. Demonstrates how clipboard-hijacking malware intercepts copied data such as passwords and crypto wallet addresses.

**Requires:** Termux:API app installed
**Usage:**
python clipboard_monitor.py

---

### ddos_tool.py
Simulates a Distributed Denial of Service attack using multithreaded UDP flooding. For educational use against localhost only — never use against systems you don't own.

**Usage:**
python ddos_tool.py

---

### vulnerability_scanner.py
Scans a target for open ports and running services, then checks service versions against a manually maintained CVE database to flag known vulnerabilities.

**Usage:**
python vulnerability_scanner.py

---

### packet_sniffer.py
Simulates network packet capture, logging protocol, source, and destination data. Built as a simulation due to raw socket restrictions on unrooted Android devices.

**Usage:**
python packet_sniffer.py

---

## Incident Response Reports

Practical SOC analyst work — log analysis and incident documentation.

### cybersec/reports/2026-06-30_ssh_bruteforce_recon.md
SSH brute force and web reconnaissance investigation. Covers log correlation across SSH, Apache access, and ModSecurity error logs, with escalation recommendations for an unresolved internal-host anomaly.
## Requirements
pip install requests paramiko python-nmap

---

## Author

Built by Esema Samuel Udemeabasi
Developed on Android using Termux and Pydroid 3. No laptop. Just consistency.
