from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
from flask_cors import CORS

import random
import string

app = Flask(__name__)
REDIS_URL = "redis://:password@localhost:6379/0"

r = FlaskRedis(app)
from app import r
CORS(app)

@app.route("/test", methods=["GET"])
def test():
    return jsonify([ key.decode("utf-8") for key in r.keys("*")])

@app.route("/url/add", methods=["POST"])
def add_url():
    if request.content_type != "application/json":
        return jsonify("Error: Data must be sent as JSON")

    url = request.json.get("url")

    key = "".join([random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(20)])

    r.set(key, url)
    return jsonify(key)

@app.route("/url/get", methods=["GET"])[]
def get_all_keys():
    all_keys = r.keys("*")
    return jsonify([key.decode("utf-8") for key in all_keys])

@app.route("/url/get/<key>", methods=["GET"])
def get_key(key):
    returned_key = r.get(key)
    return jsonify(returned_key.decode("utf-8"))














# @app.route('/')
# def get_url():
#     raw_url = r.keys("url:*")
#     return [raw_url]














if __name__ == "__main__":
    app.run(debug=True)



# pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask cors gunicorn psycopg2

# r = redis.Redis(host='localhost', port=6379)

# r.mset({"Germany": "Berlin", "France": "Paris"})

# if (r.exists(input())):
#     print(r.get("Germany"))
# else:
#     print("Nope")
#     r.set()

# r.psetex("Germany", 1000, "Berlin")

# print(r.get("Germany"))

# Try get shortened url from redis

# inputUrl = "test.com"
# shortenedUrl = ""
# if r.exists(inputUrl):
#     shortenedUrl = r.get(inputUrl)
# else:
#     shortenedUrl = generateShortenedUrl()
#     r.psetex(inputUrl, 1000, shortenedUrl)

# return shortenedUrl

# If not in redis create new shortened url and set in redis

# return shortened url