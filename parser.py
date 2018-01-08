import json

from datetime import datetime, timedelta, timezone
import time

import numpy as np

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

def find_nearest(array, value):
    idx = (np.abs(array-value)).argmin()
    return idx

def get_datapoint_closest_to_datetime(datapoints, datetime):
    timestamp = time.mktime(datetime.timetuple())
    # Parse out 'N/A' values...
    cleaned_datapoints = [point for point in datapoints if point[1] != 'N/A']
    cleaned_datapoints = np.array(cleaned_datapoints, dtype='f')

    if len(cleaned_datapoints) > 0:
        index = find_nearest(cleaned_datapoints[:,0], timestamp)

        return list(cleaned_datapoints[index])

    return None

def get_top_growth(data, amount, min_size, social_type, start_datetime, end_datetime): # Returns an array of keys of length amount with the highest designated social type's growth %
    key_to_growth = {}
    for key in data:
        datapoints = data[key]['stats'][social_type]
        first_point = get_datapoint_closest_to_datetime(datapoints, start_datetime)
        last_point = get_datapoint_closest_to_datetime(datapoints, end_datetime)
        if first_point and last_point and first_point[1] >= min_size:
            key_to_growth[key] = [(last_point[1] - first_point[1])/first_point[1], first_point, last_point]

    top_keys = sorted(key_to_growth, key=key_to_growth.get)

    top_keys_with_growth = [[key, key_to_growth[key]] for key in top_keys]

    return reversed(top_keys_with_growth[-amount:])

def get_top(data, amount, social_type, start_datetime, end_datetime):
    key_to_size = {}
    for key in data:
        datapoints = data[key]['stats'][social_type]
        last_point = get_datapoint_closest_to_datetime(datapoints, end_datetime)
        if last_point:
            key_to_size[key] = [last_point[1]]

    top_keys = sorted(key_to_size, key=key_to_size.get)

    top_keys_with_size = [[key, key_to_size[key]] for key in top_keys]

    return reversed(top_keys_with_size[-amount:])

def get_keys_in_range(data, start_datetime, end_datetime):
    keys = []
    for key in data:
        start_time = time.mktime(start_datetime.timetuple())
        end_time = time.mktime(end_datetime.timetuple())

        if data[key]['timestamp'] >= start_time and data[key]['timestamp'] <= end_time:
            keys.append(key)

    return keys

# Data Structure:
# {
#   name: "ICO NAME",
#   description: "description",
#   category: "ico stuff"
#   website: "http.website.com",
#   whitepaper: ".pdf",
#   twitter: "twitter.com",
#   telegram: "t.me",
#   slack: "slack",
#   team: [],
#   amt_raised = "232323",
#   soft_cap ="2342",
#   hard_cap ="232323",
#   pre_sale_date ="234234",
#   token_sale_date="324242",
#   total_supply ="2342442",
#   country =""
# }

def get_ico_details(data, key):
    details = data[key]
    name = details['name']
    whitepaper = details['whitepaper'] if details['whitepaper'] else 'N/A'
    return 'Name: %s - Whitepaper: %s -' % (name, whitepaper)

def format_growth_keys(top_growth_keys):
    for info in top_growth_keys:
        key = info[0]
        stats = info[1]
        growth_percentage = stats[0] * 100
        first_point = stats[1]
        last_point = stats[2]
        details = get_ico_details(upcoming, key)
        format_tuple = (growth_percentage, first_point[1], last_point[1])
        print(details)
        print('Grew %.2f%% from %i followers to %i followers.' % format_tuple)
        print()

def format_keys(top_keys):
    for info in top_keys:
        key = info[0]
        stats = info[1]
        size = stats[0]
        details = get_ico_details(upcoming, key)
        format_tuple = (size)
        print(details) 
        print('%i Twitter followers.' % format_tuple)
        print()

with open('upcoming.json') as upcoming:
    upcoming = json.load(upcoming)
    with open('data.json') as data:
        data = json.load(data)

        # Merge the two for easier access
        for stats_dict in data:
            key = stats_dict['_id']
            if key in upcoming:
                upcoming[key]['stats'] = stats_dict['stats']

        start_datetime = datetime.now() - timedelta(days=7)
        end_datetime = datetime.now()

        top_twitter_growth_keys = get_top_growth(upcoming, 10, 100, 'twitter', start_datetime, end_datetime)
        print('Top 10 ICOs with greatest Twitter growth percentage over the last week')
        format_growth_keys(top_twitter_growth_keys)

        print('#####################')
        print('#####################')
        print('#####################')

        top_twitter_keys = get_top(upcoming, 10, 'twitter', start_datetime, end_datetime)
        print('Top 10 ICOs with the most Twitter followers')
        format_keys(top_twitter_keys)

        print('#####################')
        print('#####################')
        print('#####################')

        top_telegram_growth_keys = get_top_growth(upcoming, 10, 100, 'telegram', start_datetime, end_datetime)
        print('Top 10 ICOs with greatest Telegram growth percentage over the last week')
        format_growth_keys(top_telegram_growth_keys)

        print('#####################')
        print('#####################')
        print('#####################')

        top_telegram_keys = get_top(upcoming, 10, 'telegram', start_datetime, end_datetime)
        print('Top 10 ICOs with the most Telegram followers')
        format_keys(top_telegram_keys)

        recent_keys = get_keys_in_range(upcoming, datetime.now() - timedelta(days=3), datetime.now())