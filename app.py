from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
 return "Welcome to Dummy Web Page"
if __name__ == '__main__':
 app.run(host="0.0.0.0", port=80)

