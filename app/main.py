from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Team 8! Python Flask App is Running from AWS EC2. Lets GOOOO!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
