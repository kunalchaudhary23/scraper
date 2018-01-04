from bs4 import BeautifulSoup
import urllib3
import requests
import time
from selenium import webdriver
import pprint
from pyvirtualdisplay import Display
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
	display = Display(visible=0, size=(800, 600))
	display.start()
	options = webdriver.ChromeOptions()    
	options.add_argument('--headless')
	browser = webdriver.Chrome(chrome_options=options)
	url = 'http://www.icoalert.com/?q=&is_v=1'
	browser.get(url)

	element = browser.find_elements_by_class_name("ui-tabs-tab")

	element[1].click()

	for i in range (10):
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight)');
		time.sleep(1)

	soup = BeautifulSoup(browser.page_source, 'html.parser')

	active = soup.find(id="active-listed-ico")
	active_listings = active.find("div", "listings normal")

	active_icos = active_listings.find_all("div", "ico-wrap")

	active_all = []
	for ico in active_icos:

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
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=date
		temp["total_supply"]=""
		temp["country"] =""
		active_all.append(temp)

	upcoming = soup.find(id="upcoming-listed-ico")

	upcoming_listings = upcoming.find("div", "not-tbd listings normal")

	upcoming_icos = upcoming_listings.find_all("div", "ico-wrap")

	upcoming_all = []
	for ico in upcoming_icos:

		name = ico.find("div", "about").h3.text.split("—")[0]

		description = ico.find("div", "about").h3.text.split("—")[1]
		date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
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
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=date
		temp["total_supply"]=""
		temp["country"] =""
		upcoming_all.append(temp)

	upcoming_listings_tbd = upcoming.find("div", "all-tbd listings normal")

	upcoming_icos_tbd = upcoming_listings_tbd.find_all("div", "ico-wrap")

	for ico in upcoming_icos_tbd:
		
		name = ico.find("div", "about").h3.text.split("—")[0]

		description = ico.find("div", "about").h3.text.split("—")[1]
		date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
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
		temp["pre_sale_date"]=""
		temp["token_sale_date"]=date
		temp["total_supply"]=""
		temp["country"] =""
		upcoming_all.append(temp)

	browser.quit()

	return active_all, upcoming_all

