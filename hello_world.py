from flask import Flask

app = Flask(__name__)


def greet() -> str:
    """Return greeting message for the CI/CD lab."""
    return "Welcome to CI/CD 101 using GitHub Actions!"


def generate_html(message: str) -> str:
    """Generate a simple HTML page for the given message."""
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Greeting</title>
      </head>
      <body>
        <h1>{}</h1>
      </body>
    </html>
    """.format(message)


@app.route("/greeting")
def greeting() -> str:
    """Flask view that returns the greeting HTML."""
    message = greet()
    return generate_html(message)


if __name__ == "__main__":
    app.run(port=4049)
