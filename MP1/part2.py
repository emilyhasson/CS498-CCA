from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run the stress_cpu.py script in a separate process
    subprocess.Popen(['python', 'stress_cpu.py'])
    return "CPU stress test started", 202

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
