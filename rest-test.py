from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
#app.config['APPLICATION_ROOT'] = 'abcabc'


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/get/book1')
def getBook1():
    try:
        return send_file('issues/coloringbook_1-23-2014.pdf', as_attachment=True)
    except Exception as e:
        print(e)


@app.route('/get/book2')
def getBook2():
    try:
        return send_file('issues/coloringbook_9-17-2012.pdf', as_attachment=True)
    except Exception as e:
        print(e)


@app.route('/post', methods=['POST'])
def post():
    return jsonify({'data': repr(request.data)})


if __name__ == "__main__":
    app.run()
