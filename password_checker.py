import hashlib
import requests
import re

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short - use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = response.text.splitlines()

    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            return True, int(count)

    return False, 0

def main():
    print("=== Password Checker ===\n")
    password = input("Enter password to check: ")

    print("\n--- Strength ---")
    strength, feedback = check_strength(password)
    print(f"Rating: {strength}")
    if feedback:
        for tip in feedback:
            print(f"  - {tip}")

    print("\n--- Breach Check ---")
    breached, count = check_breach(password)
    if breached:
        print(f"WARNING: This password has been seen {count:,} times in data breaches.")
        print("Do not use this password.")
    else:
        print("Good news — this password hasn't shown up in any known breaches.")

main()