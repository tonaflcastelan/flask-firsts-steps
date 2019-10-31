from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://localhost'
def home():
    return "Hello, Flask!"

app.run(port=5000)