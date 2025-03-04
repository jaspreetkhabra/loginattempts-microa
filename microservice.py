from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory storage for failed login attempts (for demo purposes)
failed_attempts = []

@app.route('/log_attempt', methods=['POST'])
def log_attempt():
    data = request.get_json()

    if not data or "user_id" not in data or "status" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    attempt = {
        "user_id": data["user_id"],
        "attempt_time": data.get("attempt_time", str(datetime.datetime.utcnow())),
        "status": data["status"],
        "ip_address": data.get("ip_address", "Unknown"),
        "device_info": data.get("device_info", "Unknown"),
    }

    failed_attempts.append(attempt)

    # If login failed, send alert
    if data["status"] == "failed":
        message = f"Warning: Incorrect password entered for user {data['user_id']}"
    else:
        message = f"Login successful for user {data['user_id']}"

    return jsonify({"message": message, "data": attempt})

if __name__ == '__main__':
    app.run(debug=True)