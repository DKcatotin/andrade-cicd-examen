from flask import Flask, render_template_string

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Proyecto Andrade</title>
</head>
<body>
    <h1>Bienvenido al Proyecto Andrade</h1>
    <p>Desplegado con CI/CD + Docker Swarm</p>
</body>
</html>
"""

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template_string(HTML)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

