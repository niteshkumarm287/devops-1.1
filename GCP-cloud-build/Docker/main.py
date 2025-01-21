from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<div style="text-align: center;"><h1>Hello from Nitesh!</h1><p>Welcome to GCP DevOps Course.</p><p></p></div>'

if __name__ == "__main__":
    # Bind Flask to all interfaces (0.0.0.0)
    app.run(debug=True, host="0.0.0.0", port=8080)
