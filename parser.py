import json

from datetime import datetime, timedelta, timezone
import time

import numpy as np


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

def get_growth_percentage(datapoints, start_datetime, end_datetime):
    if len(datapoints) > 0:
        start_time = time.mktime(start_datetime.timetuple())
        end_time = time.mktime(end_datetime.timetuple())

        if datapoints[-1][1] != 'N/A':
            datapoints = np.array(datapoints, dtype='f')

            first_index = find_nearest(datapoints[:,0], start_time)
            last_index = find_nearest(datapoints[:,0], end_time)

            first_point = datapoints[first_index]
            last_point = datapoints[last_index]

            # utc_time = datetime.fromtimestamp(first_point[0], timezone.utc)
            # local_time = utc_time.astimezone()
            # first_time = local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")
            
            # utc_time = datetime.fromtimestamp(last_point[0], timezone.utc)
            # local_time = utc_time.astimezone()
            # second_time = local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)")
            return (last_point[1] - first_point[1])/(first_point[1])
    
    return 0

def get_top_growth(data, amount, social_type, start_datetime, end_datetime): # Returns an array of keys of length amount with the highest designated social type's growth %
    key_to_growth = {}
    for key in data:
        key_to_growth[key] = get_growth_percentage(data[key]['stats'][social_type], start_datetime, end_datetime)

    top_keys = sorted(key_to_growth, key=key_to_growth.get)

    top_keys_with_growth = [[key, key_to_growth[key]] for key in top_keys]

    return top_keys_with_growth

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

        top_twitter_growth_keys = get_top_growth(upcoming, 10, 'twitter', start_datetime, end_datetime)
        print(top_twitter_growth_keys)