from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
client = MongoClient('127.0.0.1:27017')
db = client.data

def load_and_find_by_key(key):
    active = json.load(open('./active.json'))
    upcoming = json.load(open('./upcoming.json'))
    if key in active:
        return active[key]
    elif key in upcoming:
        return upcoming[key]
    else:
        return None

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

@app.route('/api/get_info_by_key/<key>')
def get_info_by_key(key):
    data = load_and_find_by_key(key)
    if data:
        results = db.data.find_one({'_id': key})
        return jsonify(merge_two_dicts(data, results))
    else:
        return jsonify({})

@app.route('/api/get_info_by_name/<name>')
def get_info_by_name(name):
    name = "".join(name.split()).lower().replace('.', '')
    return get_info_by_key(name)