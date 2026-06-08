from flask import Flask
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5252)
