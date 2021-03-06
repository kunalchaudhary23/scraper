from bs4 import BeautifulSoup
import urllib3
import requests

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
# 	country ="",
# 	tokentype =""
# }

def get_icos():
	requests.packages.urllib3.disable_warnings()

	r = requests.get('https://icodrops.com/category/active-ico/', verify=False)

	soup = BeautifulSoup(r.text, 'html.parser')

	icos = soup.find_all("div", "ico-card")

	ico_links = []
	for tag in soup.find_all("div", "ico-card"):

		ico_links.append(tag.find("a")['href'])

	active_icos = []
	for link in ico_links:
		r2 = requests.get(link, verify=False)
		soup2 = BeautifulSoup(r2.text, 'html.parser')
		name = soup2.find("div", "ico-main-info").h3.text
		category = soup2.find("span", "ico-category-name").text
		description = soup2.find("div", "ico-description").text
		raised = soup2.find("div", "money-goal").text
		sale = soup2.find("div", "sale-date").text
		goal = soup2.find("h4").text
		webiste = ""

		for a in soup2.find_all('a'):
			try:
				if "source=icodrops" in a['href']:
					website = a['href']
			except:
				pass

		twitter = ""
		telegram = ""
		social_links = soup2.find("div", "soc_links").find_all('a')
		for social_link in social_links:
			if "twitter" in social_link['href']:
				twitter = social_link['href']
			if "t.me" in social_link['href']:
				telegram = social_link['href']

		tokentype = ""
		for item in soup2.find_all("li"):

			if item.span and "Token type: " in item.span.text:
				tokentype = item.text.split("Token type: ")[1]
				

		temp = {}
		temp["name"] = name
		temp["description"]= description
		temp["category"]= category
		temp["website"]= website
		temp["whitepaper"]= ""
		temp["twitter"]=twitter
		temp["telegram"]= telegram
		temp["slack"]= ""
		temp["team"]=[]
		temp["amt_raised"]=raised
		temp["soft_cap"]=""
		temp["hard_cap"]=goal
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=sale
		temp["total_supply"]=""
		temp["country"] =""
		temp["tokentype"] = tokentype

		active_icos.append(temp)

	r3 = requests.get('https://icodrops.com/category/upcoming-ico/', verify=False)


	soup_upcoming = BeautifulSoup(r3.text, 'html.parser')

	icos = soup_upcoming.find_all("div", "ico-card")


	ico_links = []
	for tag in soup_upcoming.find_all("div", "ico-card"):

		ico_links.append(tag.find("a")['href'])

	upcoming_icos = []
	for link in ico_links:

		r4 = requests.get(link, verify=False)
		soup3 = BeautifulSoup(r4.text, 'html.parser')
		name = soup3.find("div", "ico-main-info").h3.text
		category = soup3.find("span", "ico-category-name").text
		description = soup3.find("div", "ico-description").text
		raised = soup3.find("div", "money-goal").text
		sale = soup3.find("div", "sale-date").text
		goal = soup3.find("h4").text
		webiste = ""

		for a in soup3.find_all('a'):
			try:
				if "source=icodrops" in a['href']:
					website = a['href']
			except:
				pass

		twitter = ""
		telegram = ""
		social_links = soup3.find("div", "soc_links").find_all('a')
		for social_link in social_links:
			if "twitter" in social_link['href']:
				twitter = social_link['href']
			if "t.me" in social_link['href']:
				telegram = social_link['href']
		tokentype = ""
		for item in soup3.find_all("li"):

			if item.span and "Token type: " in item.span.text:
				tokentype = item.text.split("Token type: ")[1]
		temp = {}
		temp["name"] = name
		temp["description"]= description
		temp["category"]= category
		temp["website"]= website
		temp["whitepaper"]= ""
		temp["twitter"]= twitter
		temp["telegram"]= telegram
		temp["slack"]= ""
		temp["team"]=[]
		temp["amt_raised"]=raised
		temp["soft_cap"]=""
		temp["hard_cap"]=goal
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=sale
		temp["total_supply"]=""
		temp["country"] =""
		temp["tokentype"] = tokentype
			
		upcoming_icos.append(temp)



	return active_icos, upcoming_icos

