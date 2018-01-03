from bs4 import BeautifulSoup
import urllib3
import requests
import pprint

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

# Data Structure:
# This one takes a while to run
# {
# 	name: "ICO NAME",
# 	description: "description",
# 	category: "ico stuff"
# 	website: "http.website.com",
# 	whitepaper: ".pdf",
# 	twitter: "twitter.com",
# 	telegram: "t.me",
# 	slack: "slack",
# 	team: [],
# 	amt_raised = "232323",
# 	soft_cap ="2342",
# 	hard_cap ="232323",
# 	pre_sale_date ="234234",
# 	token_sale_date="324242",
# 	total_supply ="2342442",
# 	country =""
# }


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

	members_all = soup2.find(id = "team").find_all('div', 'box')
	members = []
	if members_all:
		members = members_all[0].find_all("a")
	if len(members_all) == 2:
		members = members_all[1].find_all("a")

	for member in members:
		if "linkedin" in member['href']:
			team.append(member['href'])
	
	temp = {}
	temp["name"] = name
	temp["description"]= desc
	temp["category"]= category
	temp["website"]= website
	temp["whitepaper"]= whitepaper
	temp["twitter"]=twitter
	temp["telegram"]=telegram
	temp["slack"]= slack
	temp["team"]=team
	temp["amt_raised"]=""
	temp["soft_cap"]=softcap
	temp["hard_cap"]=hardcap
	temp["pre_sale_date"]=""
	temp["token_sale_date"]=date
	temp["total_supply"]=""
	temp["country"] =country
	upcoming.append(temp)




pp.pprint(upcoming)




	


