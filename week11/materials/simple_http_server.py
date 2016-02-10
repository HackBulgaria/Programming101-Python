import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = {
        "headers": {h[0]: h[1] for h in request.headers},
        "post_data": {d: request.form[d] for d in request.form},
        "get_data": {d: request.args[d] for d in request.args},
        # "get_data": repr(request.args),
        "method": request.method
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
