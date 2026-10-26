from flask import Flask

app = Flask(__name__)


# Required for Lab 4 unit tests
def add(a, b):
    return a + b


@app.route("/")
def home():
    return "DevOps Lab 5 Automatic Deployment Successful"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
