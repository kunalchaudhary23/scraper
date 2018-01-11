from bs4 import BeautifulSoup
import urllib3
import requests
import pprint

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

# Data Structure:
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

def get_icos():
	requests.packages.urllib3.disable_warnings()

	r = requests.get('https://www.coinschedule.com/', verify=False)

	soup = BeautifulSoup(r.text, 'html.parser')

	table = soup.find("div", "upcoming")

	body = table.find("tbody")
	icos = body.find_all("a")
	links =[]
	for ico in icos:
		print (ico)
		links.append(ico['href'])


	upcoming =[]
	for link in links:

		r2 = requests.get(link, verify=False)
		soup2 = BeautifulSoup(r2.text, 'html.parser')
		name =""
		if soup2.find("div", "project-heading"):
			name = soup2.find("div", "project-heading").h1.text
		desc = ""
		if soup2.find("div", "project-desc"):
			desc = soup2.find("div", "project-desc").text

		items = ""
		if soup2.find("div","projectinfo") and soup2.find("div","projectinfo").find_all("div", "infovalue"):
			items = soup2.find("div","projectinfo").find_all("div", "infovalue")

		website = ""
		whitepaper = ""
		supply =""
		category = ""
		counter = 1;
		for item in items:

			if item.a:
		
				if counter == 1:
					website = item.a['href']
					
				if counter == 2:
					whitepaper = item.a['href']

				counter += 1
			if hasNumbers(item.text[0]) or item.text == "TBD":
				supply = item.text
		if soup2.find("div","projectinfo") and soup2.find("div","projectinfo").find_all("div", "infoitem"):
			for label in soup2.find("div","projectinfo").find_all("div", "infoitem"):
				if label.find("div", "infolabel"):
					if label.find("div","infolabel").text == "Category":
						category = label.find("div","infovalue").text
			

		date = ""
		if soup2.find("div","crowdfund") and soup2.find("div","crowdfund").find("div", "infovalue date inline"):
			date = soup2.find("div","crowdfund").find("div", "infovalue date inline").text
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

		temp = {}
		temp["name"] = name
		temp["description"]= desc
		temp["category"]= category
		temp["website"]= website
		temp["whitepaper"]= whitepaper
		temp["twitter"]=twitter
		temp["telegram"]=telegram
		temp["slack"]= ""
		temp["team"]=team
		temp["amt_raised"]=""
		temp["soft_cap"]=""
		temp["hard_cap"]=""
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=date
		temp["total_supply"]=supply
		temp["country"] =""
		upcoming.append(temp)

	return [], upcoming