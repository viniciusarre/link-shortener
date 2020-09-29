from flask import Flask, send_from_directory, request, jsonify, render_template
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/linkshortener"
mongo = PyMongo(app)


def shorten_from_form(form):
    _form = form
    _link = _form["url"]
    _count = 0
    _id = uuid.uuid4()
    id = mongo.db.urls.insert(
        {
            'link': _link,
            'endpoint': str(_id),
            'count': _count
        })
    resp = jsonify({'message': 'Id successfully inserted!'})
    resp.status_code = 200
    return resp


@app.route('/', methods=["GET"])
def index():
    return 'This should be the homepage'


@app.route('/shorten', methods=["GET"])
def shorten():
    return render_template('form.html')


@app.route('/api/shorten', methods=["POST"])
def shorten_url():
    return shorten_from_form(request.form)


@app.route('/result', methods=["POST"])
def result():
    result = shorten_from_form(request.form)
    return render_template('result.html', result=result)


@app.route('/s', methods=["GET"])
def redirect():
    return 'The link where the URL will be redirect to its original. The access counter for it will also be incremented'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
