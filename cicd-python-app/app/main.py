from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crazy Login Page</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
                font-family: 'Comic Sans MS', cursive, sans-serif;
                animation: gradient 6s infinite alternate;
            }
            @keyframes gradient {
                0% { background-position: 0% 50%; }
                100% { background-position: 100% 50%; }
            }
            .login-container {
                background: rgba(0, 0, 0, 0.7);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
                text-align: center;
                color: white;
            }
            .login-container h1 {
                font-size: 3rem;
                margin-bottom: 1.5rem;
                text-shadow: 3px 3px #ff5722;
            }
            .login-container input {
                width: 80%;
                padding: 1rem;
                margin: 0.5rem 0;
                font-size: 1.2rem;
                border: 2px solid #ff5722;
                border-radius: 10px;
                background: transparent;
                color: white;
                outline: none;
            }
            .login-container input::placeholder {
                color: #bbb;
            }
            .login-container button {
                margin-top: 1rem;
                padding: 1rem 2rem;
                font-size: 1.5rem;
                color: white;
                background-color: #ff5722;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .login-container button:hover {
                background-color: #e64a19;
            }
            .login-container p {
                margin-top: 1rem;
                font-size: 1rem;
            }
            .login-container p a {
                color: #ff9a9e;
                text-decoration: none;
            }
            .login-container p a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h1>Crazy Login</h1>
            <form>
                <input type="text" placeholder="Username" required><br>
                <input type="password" placeholder="Password" required><br>
                <button type="submit">Login</button>
            </form>
            <p>Don't have an account? <a href="#">Sign up</a></p>
        </div>
    </body>
    </html>
    """
