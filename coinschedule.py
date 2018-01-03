from bs4 import BeautifulSoup
import urllib3
import requests
import pprint

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)


pp = pprint.PrettyPrinter(indent=4)


requests.packages.urllib3.disable_warnings()

r = requests.get('https://www.coinschedule.com/', verify=False)


soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find("div", "upcoming")
body = table.find("tbody")
icos = body.find_all("a")
# pp.pprint(icos)
links =[]
for ico in icos:
	links.append(ico['href'])

upcoming =[]
for link in links:
	r2 = requests.get(link, verify=False)
	soup2 = BeautifulSoup(r2.text, 'html.parser')
	name = soup2.find("div", "project-heading").h1.text
	desc = soup2.find("div", "project-desc").text
	items = soup2.find("div","projectinfo").find_all("div", "infovalue")
	# item_links = soup2.find("div","projectinfo").find_all("infoitem")
	# for item_link in item_links:
	# pp.pprint (items)
	website = ""
	whitepaper = ""
	supply =""
	category = ""
	counter = 1;
	for item in items:
		# print (item)
		if item.a:
			# print (item.a)
			if counter == 1:
				website = item.a['href']
				
			if counter == 2:
				# print ('here')
				whitepaper = item.a['href']
				
				# print(whitepaper)
			counter += 1
		if hasNumbers(item.text[0]) or item.text == "TBD":
			supply = item.text

	for label in soup2.find("div","projectinfo").find_all("div", "infoitem"):
		if label.find("div", "infolabel"):
			if label.find("div","infolabel").text == "Category":
				category = label.find("div","infovalue").text
		

	date = soup2.find("div","crowdfund").find("div", "infovalue date inline").text
	print (name)
	social_links = []
	if soup2.find("div","project-links"):
		social_links = soup2.find("div","project-links").find_all("a")
	twitter = ""
	telegram = ""
	team =[]

	for social_link in social_links:
		if "twitter" in social_link['href']:
			twitter = social_link['href']
		if "t.me" in social_link['href']:
			telegram = social_link['href']
	if soup2.find("div","project-team"):
		for link in soup2.find("div","project-team").find_all("a"):
			team.append(link['href'])

	print (team)

	temp = [name, desc, website, category, supply, whitepaper, date, twitter, telegram, team]
	upcoming.append(temp)
print (upcoming)



	


