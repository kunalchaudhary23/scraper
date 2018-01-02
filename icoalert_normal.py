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



element = browser.find_elements_by_class_name("ui-tabs-tab")

element[1].click()

for i in range (10):
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight)');
	time.sleep(1)

soup = BeautifulSoup(browser.page_source, 'html.parser')




# active = soup.find(id="active-listed-ico")
# active_listings = active.find("div", "listings normal")

# active_icos = active_listings.find_all("div", "ico-wrap")

# active_all = []
# for ico in active_icos:

# 	name = ico.find("div", "about").h3.text.split("—")[0]
# 	print (name)
# 	description = ico.find("div", "about").h3.text.split("—")[1]
# 	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
# 	website = ico.find("div", "website").a['href']
	
# 	temp = [name, description, date, website]
# 	active_all.append(temp)





upcoming = soup.find(id="upcoming-listed-ico")

upcoming_listings = upcoming.find("div", "not-tbd listings normal")

upcoming_icos = upcoming_listings.find_all("div", "ico-wrap")

upcoming_all = []
for ico in upcoming_icos:
	# print (ico.find("div", "about").h3.text.split("—"))
	name = ico.find("div", "about").h3.text.split("—")[0]
	# print (name)
	description = ico.find("div", "about").h3.text.split("—")[1]
	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
	website = ico.find("div", "website").a['href']
	# whitepaper = ico.find("div", "report").a['href']
	temp = [name, description, date, website]
	upcoming_all.append(temp)



upcoming_listings_tbd = upcoming.find("div", "all-tbd listings normal")

upcoming_icos_tbd = upcoming_listings_tbd.find_all("div", "ico-wrap")

for ico in upcoming_icos_tbd:
	# print (ico.find("div", "about").h3.text.split("—"))
	name = ico.find("div", "about").h3.text.split("—")[0]
	# print (name)
	description = ico.find("div", "about").h3.text.split("—")[1]
	date = ico.find("div", "date").p.text.split("DAYS LEFT")[0]
	website = ico.find("div", "website").a['href']
	# whitepaper = ico.find("div", "report").a['href']
	temp = [name, description, date, website]
	upcoming_all.append(temp)

pp.pprint(upcoming_all)
# pp.pprint("UPCOMIG****************************************")
# pp.pprint(pre_sale_upcoming)

