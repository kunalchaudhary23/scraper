from bs4 import BeautifulSoup
import urllib3
import requests
import pprint

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)


pp = pprint.PrettyPrinter(indent=4)


requests.packages.urllib3.disable_warnings()

r = requests.get('https://icobench.com/icos?status=upcoming', verify=False)


soup = BeautifulSoup(r.text, 'html.parser')

links =[]
names = soup.find_all("a", "name")
for name in names:
	links.append("https://icobench.com" + name['href'])


while soup.find("a", "next"):

	link = "https://icobench.com" + soup.find("a", "next")['href']
	r = requests.get(link, verify=False)
	soup = BeautifulSoup(r.text, 'html.parser')
	names = soup.find_all("a", "name")
	for name in names:
		links.append("https://icobench.com" + name['href'])



upcoming = []
for link in links:
	r2 = requests.get(link, verify=False)
	soup2 = BeautifulSoup(r2.text, 'html.parser')
	name = soup2.find("div", "name").h1.text
	desc = soup2.find("div", "ico_information").p.text
	category = ""
	categories = soup2.find('div', "categories").find_all("a")
	for categ in categories:
		category = category + categ.text + " "

	financial_data = soup2.find("div", "financial_data")
	date = ""
	if financial_data.find("small"):
		date = financial_data.find("small").text
	else:
		date = "TBD"

	softcap = ""
	hardcap = ""
	country = ""

	for item in financial_data.find_all("div", "data_row"):

		cols = item.find_all("div", "col_2")
		if  "Soft cap" in cols[0].text:
			softcap = cols[1].text
		if 	"Hard cap" in cols[0].text:
			hardcap = cols[1].text
		if  "Country" in cols[0].text:
			country = cols[1].text
	twitter =""
	if soup2.find("a", "twitter"):
		twitter = soup2.find("a", "twitter")['href']
	slack = ""
	if soup2.find("a", "slack"):
		slack = soup2.find("a", "slack")['href']
	website = ""
	if soup2.find("a", "www"):
		website = soup2.find("a", "www")['href']
	telegram = ""
	if soup2.find("a", "telegram"):
		website = soup2.find("a", "telegram")['href']

	whitepaper =""
	for tab in soup2.find("div", "tabs").find_all("a"):
		if "White paper" in tab.text:
			whitepaper = tab['href']

	team = []
	print (name)
	members_all = soup2.find(id = "team").find_all('div', 'box')
	members = []
	if members_all:
		members = members_all[0].find_all("a")
	if len(members_all) == 2:
		members = members_all[1].find_all("a")

	for member in members:
		if "linkedin" in member['href']:
			team.append(member['href'])
	temp = [name, desc, category, date, softcap, hardcap, country, twitter, slack, website, telegram, whitepaper, team]
	print (temp)
	upcoming.append(temp)



pp.pprint(upcoming)
# 	desc = soup2.find("div", "project-desc").text
# 	items = soup2.find("div","projectinfo").find_all("div", "infovalue")
# 	# item_links = soup2.find("div","projectinfo").find_all("infoitem")
# 	# for item_link in item_links:
# 	# pp.pprint (items)
# 	website = ""
# 	whitepaper = ""
# 	supply =""
# 	category = ""
# 	counter = 1;
# 	for item in items:
# 		# print (item)
# 		if item.a:
# 			# print (item.a)
# 			if counter == 1:
# 				website = item.a['href']
				
# 			if counter == 2:
# 				# print ('here')
# 				whitepaper = item.a['href']
				
# 				# print(whitepaper)
# 			counter += 1
# 		if hasNumbers(item.text[0]) or item.text == "TBD":
# 			supply = item.text

# 	for label in soup2.find("div","projectinfo").find_all("div", "infoitem"):
# 		if label.find("div", "infolabel"):
# 			if label.find("div","infolabel").text == "Category":
# 				category = label.find("div","infovalue").text
		

# 	date = soup2.find("div","crowdfund").find("div", "infovalue date inline").text
# 	print (name)
# 	social_links = []
# 	if soup2.find("div","project-links"):
# 		social_links = soup2.find("div","project-links").find_all("a")
# 	twitter = ""
# 	telegram = ""
# 	team =[]

# 	for social_link in social_links:
# 		if "twitter" in social_link['href']:
# 			twitter = social_link['href']
# 		if "t.me" in social_link['href']:
# 			telegram = social_link['href']
# 	if soup2.find("div","project-team"):
# 		for link in soup2.find("div","project-team").find_all("a"):
# 			team.append(link['href'])

# 	print (team)

# 	temp = [name, desc, website, category, supply, whitepaper, date, twitter, telegram, team]
# 	upcoming.append(temp)
# print (upcoming)



	


