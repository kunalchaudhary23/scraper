from bs4 import BeautifulSoup
import urllib3
import requests
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

from selenium import webdriver
path_to_chromedriver = '/Users/kunalchaudhary/Documents/scraper/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
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
	# print (ico.find("div", "about").h3.text.split("—"))
	name = ico.find("div", "about").h3.text.split("—")[0]
	print (name)
	description = ico.find("div", "about").h3.text.split("—")[1]
	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
	website = ico.find("div", "website").a['href']
	# whitepaper = ico.find("div", "report").a['href']

	temp = [name, description, date, website]
	pre_sale_active.append(temp)




# pre_sale_upcoming = soup.find(id="presale-upcoming-listed-ico")
# pre_sale_upcoming_listings = pre_sale_upcoming.find("div", "not-tbd listings presale")
# pre_sale_upcoming_icos = pre_sale_upcoming_listings.find_all("div", "ico-wrap")


# pre_sale_upcoming = []
# for ico in pre_sale_upcoming_icos:
# 	# print (ico.find("div", "about").h3.text.split("—"))
# 	name = ico.find("div", "about").h3.text.split("—")[0]

# 	description = ico.find("div", "about").h3.text.split("—")[1]
# 	date = ico.find("div", "date").p.text
# 	website = ico.find("div", "website").a['href']
# 	# whitepaper = ico.find("div", "report").a['href']
# 	temp = [name, description, date, website]
# 	pre_sale_upcoming.append(temp)




browser2 = webdriver.Chrome(executable_path = path_to_chromedriver)
url2 = 'http://www.icoalert.com/?q=&is_v=1'

browser2.get(url)

element = browser2.find_elements_by_class_name("ui-tabs-tab")

element[1].click()

for i in range (10):
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight)');
	time.sleep(1)

soup = BeautifulSoup(browser2.page_source, 'html.parser')




active = soup.find(id="active-listed-ico")
active_listings = active.find("div", "listings normal")

active_icos = active_listings.find_all("div", "ico-wrap")

active_all = []
for ico in active_icos:
	# print (ico.find("div", "about").h3.text.split("—"))
	name = ico.find("div", "about").h3.text.split("—")[0]
	print (name)
	description = ico.find("div", "about").h3.text.split("—")[1]
	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
	website = ico.find("div", "website").a['href']
	# whitepaper = ico.find("div", "report").a['href']
	temp = [name, description, date, website]
	active_all.append(temp)





# upcoming = soup.find(id="upcoming-listed-ico")
# active_listings = active.find("div", "listings normal")

# active_icos = active_listings.find_all("div", "ico-wrap")

# active_all = []
# for ico in active_icos:
# 	# print (ico.find("div", "about").h3.text.split("—"))
# 	name = ico.find("div", "about").h3.text.split("—")[0]
# 	description = ico.find("div", "about").h3.text.split("—")[1]
# 	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
# 	website = ico.find("div", "website").a['href']
# 	# whitepaper = ico.find("div", "report").a['href']
# 	temp = [name, description, date, website]
# 	active_all.append(temp)


