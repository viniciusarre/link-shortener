from flask import Flask
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["link_shortener"]


@app.route('/', methods=["GET"])
def index():
    return 'This should be the homepage'


@app.route('/set_url', methods=["GET"])
def set_url():
    return 'A GUI in which the user can shorten a URL'


@app.route('/shorten', methods=["POST"])
def shorten_url():
    return 'The url should be shortened here'


@app.route('/s', methods=["GET"])
def redirect():
    return 'The link where the URL will be redirect to its original. The access counter for it will also be incremented'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
