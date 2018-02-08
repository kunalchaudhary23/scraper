from bs4 import BeautifulSoup
import urllib3
import requests
import pprint
import time
from selenium import webdriver

def fill_telegram(url):
	try:
		options = webdriver.ChromeOptions()    
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		browser = webdriver.Chrome(chrome_options=options)

		browser.get(url)
		soup = BeautifulSoup(browser.page_source, 'html.parser')

		a_tags = soup.find_all("a")

		telegram = ''

		for a_tag in a_tags:
			try:
				if a_tag and a_tag['href'] and "t.me" in a_tag['href']:
					telegram = a_tag['href']
					break
					
			except:
				pass

		browser.close()
		return telegram
	except:
		pass

print(fill_telegram('geekzcode.com'))

def fill_twitter(name, url):
	try:
		# r = requests.get("https://www.trevilabs.co/?utm_source=trackico", verify=False)

		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		browser = webdriver.Chrome(chrome_options=options)
	
		browser.get(url)
		soup = BeautifulSoup(browser.page_source, 'html.parser')

		a_tags = soup.find_all("a")

		twitter = ''

		for a_tag in a_tags:
			print(a_tag)
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
		return twitter
	except:
		pass
