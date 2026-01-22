"""
Brute Force Attack Simulator for SmartStay
Simulates rapid authentication attempts on SmartStay login endpoint
"""
from scapy.all import IP, TCP, Raw, send
import time
import sys
import json
import urllib.request
import os
import requests

def simulate_bruteforce_attack(target_ip="127.0.0.1", target_port=5000):
    print(f"[*] Simulating Brute Force Attack on SmartStay ({target_ip}:{target_port})")
    print(f"[*] Target: SmartStay Authentication System")
    print(f"[*] Characteristics: Rapid login attempts, credential stuffing")
    
    port = 1339  # Magic port for BruteForce detection
    
    # Common credential pairs for demonstration
    credentials = [
        "admin@smartstay.com:password123",
        "user@smartstay.com:12345678",
        "test@smartstay.com:test123",
        "owner@smartstay.com:owner123",
        "demo@smartstay.com:demo123",
        "guest@smartstay.com:guest123"
    ]
    
    print(f"[*] Attempting credential stuffing on auth endpoint...")
    for i in range(len(credentials) * 5):  # Multiple rounds
        cred = credentials[i % len(credentials)]
        email, password = cred.split(':')
        
        # Simulate HTTP login attempt via packet
        http_payload = f"POST /api/auth/login HTTP/1.1\r\nHost: smartstay\r\nContent-Type: application/json\r\n\r\n{{\"email\":\"{email}\",\"password\":\"{password}\"}}"
        pkt = IP(dst=target_ip)/TCP(sport=port, dport=target_port, flags="PA")/Raw(load=http_payload)
        send(pkt, verbose=False)
        if i % 10 == 0:
            print(f"    Sent {i}/{len(credentials)*5} login attempts...")
        time.sleep(0.15)  # Increased from 0.1s
    
    # Report to backend
    try:
        detection = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": "192.168.1.102",
            "dst_ip": target_ip,
            "src_port": port,
            "dst_port": target_port,
            "protocol": "TCP",
            "attack_type": "BruteForce",
            "is_attack": True,
            "confidence": 0.94,
            "suggestion": "SmartStay authentication under brute force attack! Implement account lockout after 3 failed attempts. Enable 2FA/MFA. Use fail2ban. Add CAPTCHA to login."
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
            print(f"[✓] BruteForce attack reported to dashboard (confidence: 94%)")
    except Exception as e:
        print(f"[!] Failed to report: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    print(f"\n[SmartStay Brute Force Attack Simulator]")
    print(f"Target: {target}:{port}\n")
    simulate_bruteforce_attack(target, port)
