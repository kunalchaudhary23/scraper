from bs4 import BeautifulSoup
import urllib3
import requests
import pprint
import time
from selenium import webdriver

# Data Structure:
# {
#   name: "ICO NAME",
#   description: "description",
#   category: "ico stuff"
#   website: "http.website.com",
#   whitepaper: ".pdf",
#   twitter: "twitter.com",
#   telegram: "t.me",
#   slack: "slack",
#   team: [],
#   amt_raised = "232323",
#   soft_cap ="2342",
#   hard_cap ="232323",
#   pre_sale_date ="234234",
#   token_sale_date="324242",
#   total_supply ="2342442",
#   country =""
# }

def scrape_telegram(data):
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	browser = webdriver.Chrome(chrome_options=options)
	print(data)

	for key in data:
		if data[key]['telegram'] and len(data[key]['telegram']) > 0:
			continue

		url = data[key]['website']

		try:
			browser.get(url)
			soup = BeautifulSoup(browser.page_source, 'html.parser')

			a_tags = soup.find_all("a")

			telegram = None

			for a_tag in a_tags:
				try:
					if a_tag and a_tag['href'] and "t.me" in a_tag['href']:
						telegram = a_tag['href']
						break
						
				except:
					pass

			print('Getting telegram for %s : %s' % (key, telegram))
			if telegram:
				data[key]['telegram'] = telegram
		except:
			pass

	browser.close()
	return data

def scrape_twitter(data):
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	browser = webdriver.Chrome(chrome_options=options)

	for key in data:
		if data[key]['twitter'] and len(data[key]['twitter']) > 0:
			continue

		url = data[key]['website']
		try:
			browser.get(url)
			soup = BeautifulSoup(browser.page_source, 'html.parser')

			a_tags = soup.find_all("a")

			twitter = None

			for a_tag in a_tags:

				try:
					if a_tag and a_tag['href'] and "twitter" in a_tag['href']:
						if key[:2].lower() in a_tag['href'].lower():
							# print (name[:2])
							# print ("THIS IS THE REAL ONE " + a_tag['href'])
							twitter = a_tag['href']
							break
						
				except:
					pass

			if twitter:
				data[key]['twitter'] = twitter
		except:
			pass

	browser.close()
	return data
