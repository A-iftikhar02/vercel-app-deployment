from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask App on Vercel</title>
        </head>
        <body>
            <h1>Deploying Flask App at Vercel 🚀</h1>
            <p>Welcome to the Flask app deployed on Vercel.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
