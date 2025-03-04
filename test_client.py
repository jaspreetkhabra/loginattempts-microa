import requests

API_URL = "http://127.0.0.1:5000/log_attempt"

data = {
    "user_id": "12345",
    "attempt_time": "2025-02-11T14:30:00Z",
    "status": "failed",
    "ip_address": "192.168.1.1",
    "device_info": "Windows 10, Chrome Browser"
}

response = requests.post(API_URL, json=data)
print("Response from Microservice:", response.json())