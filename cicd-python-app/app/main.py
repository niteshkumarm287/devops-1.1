from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crazy Page</title>
        <style>
            body {
                background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
                animation: gradient 6s infinite alternate;
                color: white;
                font-family: 'Comic Sans MS', cursive, sans-serif;
                text-align: center;
                padding: 2rem;
            }
            h1 {
                font-size: 5rem;
                text-shadow: 3px 3px #000;
                animation: wobble 1s infinite;
            }
            p {
                font-size: 2rem;
                animation: fadeIn 3s infinite alternate;
            }
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                100% { background-position: 100% 50%; }
            }
            @keyframes wobble {
                0%, 100% { transform: rotate(-5deg); }
                50% { transform: rotate(5deg); }
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            button {
                margin-top: 2rem;
                padding: 1rem 2rem;
                font-size: 1.5rem;
                color: white;
                background-color: #ff5722;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                animation: bounce 1s infinite alternate;
            }
            button:hover {
                background-color: #e64a19;
            }
            @keyframes bounce {
                0% { transform: translateY(0); }
                100% { transform: translateY(-10px); }
            }
        </style>
    </head>
    <body>
        <h1>🎉 Welcome to Crazy FastAPI 🎉</h1>
        <p>This page is full of colors, animations, and chaos!</p>
        <button onclick="alert('You clicked the Crazy Button!')">Click Me!</button>
    </body>
    </html>
    """
