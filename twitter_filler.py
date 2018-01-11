
from bs4 import BeautifulSoup
import urllib3
import requests
import pprint
import time
from selenium import webdriver
pp = pprint.PrettyPrinter(indent=4)


f = open('dump.txt', 'r')
requests.packages.urllib3.disable_warnings()

icos = []
for line in f:

	name = line.split(',')[0]
	url = line.split(',')[1]
	twitter = ""

	try:

		# r = requests.get("https://www.trevilabs.co/?utm_source=trackico", verify=False)

		# options = webdriver.ChromeOptions()
		# options.add_argument('--headless')
		# options.add_argument('--no-sandbox')
		# browser = webdriver.Chrome(chrome_options=options)

		path_to_chromedriver = '/Users/kunalchaudhary/Documents/scraper/chromedriver'
		browser = webdriver.Chrome(executable_path = path_to_chromedriver)

	
		browser.get(url)
		soup = BeautifulSoup(browser.page_source, 'html.parser')

		a_tags = soup.find_all("a")

		for a_tag in a_tags:

			try:
				if a_tag and a_tag['href'] and "twitter" in a_tag['href']:
					if name[:2].lower() in a_tag['href'].lower():
						# print (name[:2])
						# print ("THIS IS THE REAL ONE " + a_tag['href'])
						twitter = a_tag['href']
						break
					
			except:
				pass

		browser.close()
		print (name, twitter)
	except:
		pass
	temp = {}
	temp["name"] = name
	temp["url"] = url
	temp["twitter"] = twitter
	icos.append(temp)

pp.pprint(icos)

