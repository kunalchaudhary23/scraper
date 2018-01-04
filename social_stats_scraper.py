import json
from social_stats import get_telegram_size, get_twitter_size
from datetime import datetime, timedelta
import time
from pymongo import MongoClient

client = MongoClient('127.0.0.1:27017')
db = client.stats

def update_mongo(ico_name, stats):
    result = db.stats.replace_one({
        '_id': ico_name
    }, {
        ico_name: stats
    }, upsert=True)

def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

def save_social_stats(infile, outfile_name):
    data = json.load(infile)
    telegram_futures = {}
    twitter_futures = {}
    social_stats = {}

    timestamp = time.mktime(datetime.now().timetuple())
    for key in data:
        ico = data[key]
        existing_data = db.stats.find_one({'_id': key})
        if not existing_data:
            social_stats[ico['name']] = {
                'telegram': [],
                'twitter': []
            }
        else:
            social_stats[ico['name']] = results['stats']

        if len(ico['telegram']) > 0:
            telegram_futures[ico['name']] = get_telegram_size(ico['telegram'])

        if len(ico['twitter']) > 0:
            twitter_futures[ico['name']] = get_twitter_size(ico['twitter'])

    for key in telegram_futures:
        social_stats[key]['telegram'].append((timestamp, telegram_futures[key].result().data))
        
    for key in twitter_futures:
        social_stats[key]['twitter'].append((timestamp, twitter_futures[key].result().data))

    for key in social_stats:
        update_mongo(key, {'stats': social_stats[key]})

with open('active.json') as infile:
    save_social_stats(infile, 'active_social_stats')

with open('upcoming.json') as infile:
    save_social_stats(infile, 'upcoming_social_stats')
