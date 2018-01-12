import json


def print_data(infile):
	data = json.load(infile)
	for key in data:
		print('%s,%s' % (data[key]['name'], data[key]['website']))

with open('active.json') as infile:
   	print_data(infile)

with open('upcoming.json') as infile:
    print_data(infile)