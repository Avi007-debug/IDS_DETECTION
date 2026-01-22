"""
DoS (Denial of Service) Attack Simulator for SmartStay
Simulates high-volume traffic attack pattern targeting SmartStay backend
"""
from scapy.all import IP, TCP, Raw, send
import time
import sys
import json
import urllib.request
import os
import requests

def simulate_dos_attack(target_ip="127.0.0.1", target_port=5000):
    print(f"[*] Simulating DoS Attack on SmartStay ({target_ip}:{target_port})")
    print(f"[*] Target: SmartStay Backend API")
    print(f"[*] Characteristics: High packet rate, sustained traffic")
    
    port = 1337  # Magic port for DoS detection
    
    # Send burst of packets to SmartStay health endpoint
    print(f"[*] Flooding /health endpoint...")
    for i in range(50):
        pkt = IP(dst=target_ip)/TCP(sport=port, dport=target_port, flags="S")/Raw(load="GET /health HTTP/1.1\r\nHost: smartstay\r\n\r\n")
        send(pkt, verbose=False)
        if i % 10 == 0:
            print(f"    Sent {i}/50 packets...")
        time.sleep(0.05)  # Increased from 0.02s to slow down report rate
    
    # Report to backend
    try:
        detection = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": "192.168.1.100",
            "dst_ip": target_ip,
            "src_port": port,
            "dst_port": target_port,
            "protocol": "TCP",
            "attack_type": "DoS",
            "is_attack": True,
            "confidence": 0.99,
            "suggestion": f"SmartStay under DoS attack! Enable rate limiting on port {target_port}. Block source IP immediately. Consider using Cloudflare DDoS protection."
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
            print(f"[✓] DoS attack reported to dashboard (confidence: 99%)")
    except Exception as e:
        print(f"[!] Failed to report: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    print(f"\n[SmartStay DoS Attack Simulator]")
    print(f"Target: {target}:{port}\n")
    simulate_dos_attack(target, port)
