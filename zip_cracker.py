import zipfile
import sys

def crack_zip(zip_file, wordlist):
    try:
        zf = zipfile.ZipFile(zip_file)
    except FileNotFoundError:
        print(f"Error: {zip_file} not found.")
        return

    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f"Error: {wordlist} not found.")
        return

    print(f"\nCracking {zip_file} using {len(passwords)} passwords...\n")

    for password in passwords:
        password = password.strip()
        try:
            zf.extractall(pwd=password.encode())
            print(f"Password found: {password}")
            return
        except:
            continue

    print("Password not found in wordlist.")

def main():
    print("=== Zip Cracker ===\n")
    zip_file = input("Enter zip file name: ")
    wordlist = input("Enter wordlist file name: ")
    crack_zip(zip_file, wordlist)

main()