from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Dockerized Flask + Jenkins!"


@app.route("/raju")
def test():
    return "Hello raju"

@app.route("/tata")
def test1():
    return "Hello tata"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
