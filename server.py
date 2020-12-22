from flask import Flask, send_from_directory, request, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/linkshortener"
mongo = PyMongo(app)


def shorten_from_form(_form):
    _link = _form["url"]
    if not("http" in _link or "https" in _link):
        _link = "https://" + _link
    _count = 0
    _id = uuid.uuid4()
    mongo.db.urls.insert_one(
        {
            'link': _link,
            'endpoint': str(_id),
            'count': _count
        })
    resp = {
        'message': 'Id successfully inserted!',
        'endpoint': str(_id), 
        'url': 'http://localhost:5000',
        'status_code': 200
        }
    return resp


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/shorten', methods=["GET"])
def shorten():
    return render_template('form.html')


@app.route('/api/list', methods=["GET"])
def list_urls():
    return mongo.db.urls.find()


@app.route('/api/shorten', methods=["POST"])
def shorten_url():
    result = shorten_from_form(request.form)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@app.route('/result', methods=["POST"])
def result():
    result = shorten_from_form(request.form)
    return render_template('result.html', result=result)


@app.route('/s/<handler>', methods=["GET"])
def handle_redirecting(handler):
    url = mongo.db.urls.find_one({'endpoint': handler})
    mongo.db.urls.find_one_and_update(
        {'endpoint': handler},
        {'$inc': {'count': 1}}
    )
    return redirect(url['link'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
