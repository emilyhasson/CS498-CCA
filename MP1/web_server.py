from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial seed value
seed_value = 0

@app.route("/", methods=["POST"])
def update_seed():
    global seed_value
    try:
        data = request.get_json()
        new_seed = int(data["num"])
        seed_value = new_seed
        return "Seed value updated successfully", 200
    except Exception as e:
        return str(e), 400

@app.route("/", methods=["GET"])
def get_seed():
    global seed_value
    return str(seed_value)

if __name__ == "__main__":
    # Run the application on a specific port (e.g., 5000)
    app.run(host="0.0.0.0", port=5000)
