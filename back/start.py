from flask import Flask
from interface import collect

# import read

app = Flask(__name__)

collect.collect(app)

@app.route('/index')
def index():
    print('Hello World')
    return 'Hello World'


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 9999, debug=True)