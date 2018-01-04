from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient('127.0.0.1:27017')
db = client.analytics

@app.route('/api/messages/<ico>/<feed_type>')
def get_ico_messages(ico, feed_type):
    results = db.icos.find_one({'_id': ico})
    return jsonify(results[ico][feed_type])

@app.route('/api/pull_params/<ico>/<service>')
def get_ico_pull_params_for_service(ico, service):
	results = db.pull_params.find_one({'_id': ico})
	return jsonify(results['pull_params'][service + '_pull_params'])

@app.route('/api/pull_params/<ico>')
def get_ico_pull_params(ico):
	results = db.pull_params.find_one({'_id': ico})
	return jsonify(results['pull_params'])

@app.route('/api/icos')
def get_icos():
    results = list(db.coins.find())
    return jsonify(results)