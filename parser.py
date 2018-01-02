from bs4 import BeautifulSoup
import urllib3
import requests


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
	# info = soup.find_all("div", "ico-desk")
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
			print ('error')
	
	temp = [name, category, description, raised, sale, goal, website]

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
	# info = soup.find_all("div", "ico-desk")
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
			print ('error')
	
	temp = [name, category, description, raised, sale, goal, website]
	# print (temp)
	upcoming_icos.append(temp)
	
print (len(active_icos))
print (len(upcoming_icos))
print ("***************************Active ICOS******************************")
print (active_icos)
print ("***************************Upcoming ICOS****************************")
print (upcoming_icos)

