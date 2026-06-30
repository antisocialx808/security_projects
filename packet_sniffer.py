import random
import time
import logging
import os
from datetime import datetime

log_file = os.path.join(os.path.dirname(__file__), "packets.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

packet_count = 0

def random_ip():
    return f"{random.randint(1,254)}.{random.randint(0,254)}.{random.randint(0,254)}.{random.randint(1,254)}"

def random_port():
    return random.randint(1024, 65535)

def generate_packet():
    protocols = ["TCP", "UDP", "ICMP"]
    protocol = random.choice(protocols)
    src = random_ip()
    dst = random_ip()

    if protocol == "TCP":
        sport = random_port()
        dport = random.choice([80, 443, 22, 21, 3306, 8080])
        return f"{protocol} | {src}:{sport} -> {dst}:{dport}"
    elif protocol == "UDP":
        sport = random_port()
        dport = random.choice([53, 67, 123, 161])
        return f"{protocol} | {src}:{sport} -> {dst}:{dport}"
    else:
        return f"{protocol} | {src} -> {dst}"

def main():
    global packet_count

    print("=== Network Packet Sniffer (Simulation) ===")
    print("Note: Running in simulation mode on Android.")
    print("Capturing simulated traffic... Press Ctrl+C to stop.\n")

    logging.info("--- Simulation session started ---")

    try:
        while True:
            packet = generate_packet()
            packet_count += 1
            print(f"[{packet_count}] {packet}")
            logging.info(packet)
            time.sleep(0.3)

    except KeyboardInterrupt:
        logging.info(f"--- Session ended | Total: {packet_count} packets ---")
        print(f"\nCapture complete. {packet_count} packets captured.")
        print(f"Log saved to: {log_file}")

main()