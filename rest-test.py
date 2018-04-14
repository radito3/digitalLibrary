from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/test')
def test():
    with open('test.txt', 'rb') as f:
        return f.read()
    # return request.base_url


@app.route('/post', methods=['POST'])
def post():
    return jsonify({'data': repr(request.data)})


if __name__ == "__main__":
    app.run(debug=True)
