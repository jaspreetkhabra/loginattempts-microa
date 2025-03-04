# Login Attempts Microservice (Microservice A)

## Overview
This microservice is designed to log and monitor failed login attempts. It records login events, including timestamps, IP addresses, and device information. If a login attempt fails, an alert is generated.

## Features
- Accepts JSON requests to log login attempts.
- Stores failed attempts in memory.
- Sends alerts for failed logins.
- Provides an API endpoint to retrieve logged attempts.

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/jaspreetkhabra/loginattempts-microa.git
cd loginattempts-microa
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Microservice
```sh
python microservice.py
```

## API Usage
### 1. Log a Login Attempt
**Endpoint:** `POST /log_attempt`

**Request Body:**
```json
{
  "user_id": "12345",
  "status": "failed",
  "ip_address": "192.168.1.1",
  "device_info": "Windows 10, Chrome Browser"
}
```

**Response:**
```json
{
  "message": "Warning: Incorrect password entered for user 12345",
  "data": { ... }
}
```

### 2. Retrieve Logged Attempts (Future Enhancement)
**Endpoint:** `GET /get_attempts`

## Troubleshooting
- If `requirements.txt` is missing, ensure you pull the latest repository updates:
  ```sh
  git pull origin main
  ```
- If the virtual environment doesn’t activate, check your Python installation.
- If dependencies fail to install, ensure `pip` is updated:
  ```sh
  pip install --upgrade pip
  ```

