from flask import Flask, render_template, make_response

DEBUG = True
HOST = '127.0.0.1'
PORT = 8080

app = Flask(__name__)


@app.route('/')
def home():
    return make_response("Hello there")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
