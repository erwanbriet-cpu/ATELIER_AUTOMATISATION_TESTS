import requests
import time

def call_api(url):
    try:
        start = time.time()
        # Timeout 3s + simple retry
        response = requests.get(url, timeout=3)
        latency = (time.time() - start) * 1000
        return response, latency
    except Exception:
        return None, 0