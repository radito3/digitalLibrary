from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/get/book2')
def test():
    with open('test.txt', 'rb') as f:
        return f.read()


@app.route('/post', methods=['POST'])
def post():
    return jsonify({'data': repr(request.data)})


if __name__ == "__main__":
    app.run(debug=True)
