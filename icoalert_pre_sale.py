from bs4 import BeautifulSoup
import urllib3
import requests
import time
from selenium import webdriver

import pprint
pp = pprint.PrettyPrinter(indent=4)

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
def get_icos():
	options = webdriver.ChromeOptions()    
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	browser = webdriver.Chrome(chrome_options=options)
	url = 'http://www.icoalert.com/?q=&is_v=1'
	browser.get(url)

	for i in range (10):
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight)');
		time.sleep(1)

	soup = BeautifulSoup(browser.page_source, 'html.parser')

	pre_sale_active = soup.find(id="presale-active-listed-ico")
	pre_sale_listings = pre_sale_active.find("div", "listings presale")
	pre_sale_icos = pre_sale_listings.find_all("div", "ico-wrap")

	pre_sale_active = []

	for ico in pre_sale_icos:

		name = ico.find("div", "about").h3.text.split("—")[0]
		description = ico.find("div", "about").h3.text.split("—")[1]
		date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
		website = ico.find("div", "website").a['href']
		

		temp = {}
		temp["name"] = name
		temp["description"]= description
		temp["category"]= ""
		temp["website"]= website
		temp["whitepaper"]= ""
		temp["twitter"]=""
		temp["telegram"]= ""
		temp["slack"]= ""
		temp["team"]=[]
		temp["amt_raised"]=""
		temp["soft_cap"]=""
		temp["hard_cap"]=""
		temp["pre_sale_date"]=date
		temp["token_sale_date"]=""
		temp["total_supply"]=""
		temp["country"] =""

		pre_sale_active.append(temp)

	pre_sale_upcoming = soup.find(id="presale-upcoming-listed-ico")
	pre_sale_upcoming_listings = pre_sale_upcoming.find("div", "not-tbd listings presale")
	pre_sale_upcoming_icos = pre_sale_upcoming_listings.find_all("div", "ico-wrap")

	pre_sale_upcoming = []
	for ico in pre_sale_upcoming_icos:

		name = ico.find("div", "about").h3.text.split("—")[0]

		description = ico.find("div", "about").h3.text.split("—")[1]
		date = ico.find("div", "date").p.text
		website = ico.find("div", "website").a['href']

		temp ={}
		temp["name"] = name
		temp["description"]= description
		temp["category"]= ""
		temp["website"]= website
		temp["whitepaper"]= ""
		temp["twitter"]=""
		temp["telegram"]= ""
		temp["slack"]= ""
		temp["team"]=[]
		temp["amt_raised"]=""
		temp["soft_cap"]=""
		temp["hard_cap"]=""
		temp["pre_sale_date"]=date
		temp["token_sale_date"]=""
		temp["total_supply"]=""
		temp["country"] =""
		pre_sale_upcoming.append(temp)

	# We treat all pre-sales as upcoming.
	pre_sale_upcoming.extend(pre_sale_active)

	browser.quit()

	return [], pre_sale_upcoming
