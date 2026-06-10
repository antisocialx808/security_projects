# Security Projects

A collection of Python security tools built and run on Android using Termux and Pydroid 3.

## Tools

### Password Checker
Checks a password's strength and verifies if it has appeared in known data breaches using the HaveIBeenPwned API.

**Features:**
- Rates password strength (Weak, Moderate, Strong)
- Checks against real breach databases
- Password never leaves your device

## Setup
pip install requests paramiko scapy python-nmap

## Run
python password_checker.py