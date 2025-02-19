from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return "Deploying Flask App at Vercel 🚀"

@app.route("/about")
def about():
    return "This is a simple Flask app deployed on Vercel."

@app.route("/api/data")
def get_data():
    data = {
        "message": "Hello from Flask API!",
        "status": "success",
        "version": "1.0"
    }
    return jsonify(data)

if _name_ == "_main_":
    app.run(host="0.0.0.0",port=5000)
