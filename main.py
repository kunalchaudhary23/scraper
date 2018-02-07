### Import scrapers
import icoalert_pre_sale
import icoalert_normal
import coinschedule
import trackico
import icobench
import icodrops
import fillers

import json

from datetime import datetime, timedelta
import time

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

scraper_functions = [
    icoalert_pre_sale.get_icos,
    # icoalert_normal.get_icos,
    # coinschedule.get_icos,
    # trackico.get_icos,
    # icobench.get_icos,
    # icodrops.get_icos
]

active_data = {}
upcoming_data = {}

with open('active.json') as infile:
    active_data = json.load(infile)

with open('upcoming.json') as infile:
    upcoming_data = json.load(infile)

def add_to_data_without_duplicates(data, key, value):
    # Strip whitespace and make name all lowercase to find clashes
    key = "".join(key.split()).lower().replace('.', '')
    value['name'] = value['name'].strip()
    if key not in data:
        data[key] = value
        value['timestamp'] = time.mktime(datetime.now().timetuple())
    
    for k in value:
        if value[k]:
            data[key][k] = value[k]

for scraper_fn in scraper_functions:
    active, upcoming = scraper_fn()

    for ico in active:
        add_to_data_without_duplicates(active_data, ico['name'], ico)

    active_data = fillers.scrape_telegram(active_data)
    active_data = fillers.scrape_twitter(active_data)

    for ico in upcoming:
        add_to_data_without_duplicates(upcoming_data, ico['name'], ico)

    upcoming_data = fillers.scrape_telegram(upcoming_data)
    upcoming_data = fillers.scrape_twitter(upcoming_data)

with open('active.json', 'w') as outfile:  
    json.dump(active_data, outfile)

with open('upcoming.json', 'w') as outfile:  
    json.dump(upcoming_data, outfile)