#!/usr/bin/env python3
import requests
import sys

def check_headers(url):
    try:
        r = requests.head(url, timeout=8, allow_redirects=True)
        print(f"Status: {r.status_code}")
        for h, v in r.headers.items():
            print(f"{h}: {v}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_headers.py https://example.com")
    else:
        check_headers(sys.argv[1])
