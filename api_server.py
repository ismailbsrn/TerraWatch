from flask import Flask, jsonify, send_from_directory
from pymongo import MongoClient
from decouple import config

app = Flask(__name__)
client = MongoClient(config("MONGO_URI"))
collection = client.terrawatch.terrawatchcol


@app.route("/api/latest")
def latest():
    doc = collection.find_one(sort=[("timestamp", -1)])
    if doc:
        doc["_id"] = str(doc["_id"])
        return jsonify(doc)
    else:
        return jsonify({}), 200


@app.route("/api/all")
def all_data():
    docs = list(collection.find().sort("timestamp", -1).limit(50))
    for doc in docs:
        doc["_id"] = str(doc["_id"])
    return jsonify(docs)


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
