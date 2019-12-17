
import logging
from wrapper import get_tweets
from flask   import Flask,render_template, jsonify, request

app = Flask("__name__")
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/json')
def json():
    return get_tweets()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)