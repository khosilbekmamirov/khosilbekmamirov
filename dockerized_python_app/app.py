from flask import Flask, jsonify
import socket
import os
import psutil

app = Flask(__name__)

@app.route("/")
def system_info():
    return jsonify({
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "cpu_count": os.cpu_count(),
        "memory_total_mb": round(psutil.virtual_memory().total / (1024 * 1024), 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
