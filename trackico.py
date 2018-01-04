from bs4 import BeautifulSoup
import urllib3
import requests
import pprint



pp = pprint.PrettyPrinter(indent=4)


requests.packages.urllib3.disable_warnings()

r = requests.get('https://www.trackico.io/presale/', verify=False)


soup = BeautifulSoup(r.text, 'html.parser')

links =[]
names = soup.find_all("a", "card-body text-center pt-1 pb-10")

for name in names:
	links.append("https://www.trackico.io" + name['href'])


first_link = "https://www.trackico.io" + soup.find("a", "btn btn-w-sm btn-light")['href']
r = requests.get(first_link, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
names = soup.find_all("a", "card-body text-center pt-1 pb-10")
for name in names:
	links.append("https://www.trackico.io" + name['href'])

while len(soup.find_all("a", "btn btn-w-sm btn-light")) == 2:

	link = "https://www.trackico.io" + soup.find_all("a", "btn btn-w-sm btn-light")[1]['href']
	r = requests.get(link, verify=False)
	soup = BeautifulSoup(r.text, 'html.parser')
	names = soup.find_all("a", "card-body text-center pt-1 pb-10")
	for name in names:
		links.append("https://www.trackico.io" + name['href'])


pre_sale = []
for link in links:
	r2 = requests.get(link, verify=False)
	soup2 = BeautifulSoup(r2.text, 'html.parser')
	name = soup2.find("li", "breadcrumb-item active").text
	desc = soup2.find("small", "subtitle").p.text
	

	overview = soup2.find(id="tab-overview")
	dates = overview.find_all("div", "col-12 col-lg-6")
	pre_sale_date = dates[0].find("div", "flexbox mt-2").text
	token_sale_date = dates[1].find("div", "flexbox mt-2").text
	country =""
	tokentype=""
	boxes = soup2.find_all("div", "card card-body")
	for box in boxes:
		if box.h6 and "Country" in box.h6.text and box.find_all('span', 'fs-30'):
			country = box.find_all('span', 'fs-30')[1].text
		if box.h6 and "Platform" in box.h6.text and box.find_all('span', 'fs-30') and box.find_all('span', 'fs-30')[1].a:
			tokentype = box.find_all('span', 'fs-30')[1].a.text

	team = []
	members = soup2.find(id = "tab-team").find_all("a")

	for member in members:
		team.append(member['href'])

	twitter_telegram = soup2.find_all("a", "azm-twitter")
	twitter = ""
	telegram =""
	for link in twitter_telegram:
		if "t.me" in link['href']:
			telegram = link['href']
		if "twitter" in link['href']:
			twitter = link['href']
	website =""
	if soup2.find('a', 'azm-css3'):
		website = soup2.find('a', 'azm-css3')['href']
	whitepaper =""
	if soup2.find('a', 'azm-lastfm'):	
		whitepaper = soup2.find('a', 'azm-lastfm')['href']

	
	temp = {}
	temp["name"] = name
	temp["description"]= desc
	temp["category"]= ""
	temp["website"]= website
	temp["whitepaper"]= whitepaper
	temp["twitter"]=twitter
	temp["telegram"]=telegram
	temp["slack"]= ""
	temp["team"]= team
	temp["amt_raised"]=""
	temp["soft_cap"]=""
	temp["hard_cap"]=""
	temp["pre_sale_date"]=pre_sale_date
	temp["token_sale_date"]=token_sale_date
	temp["total_supply"]=""
	temp["country"] = country
	temp["tokentype"] = tokentype
	pre_sale.append(temp)
pp.pprint(pre_sale)



r = requests.get('https://www.trackico.io/upcoming/', verify=False)


soup = BeautifulSoup(r.text, 'html.parser')

links =[]
names = soup.find_all("a", "card-body text-center pt-1 pb-10")

for name in names:
	links.append("https://www.trackico.io" + name['href'])


first_link = "https://www.trackico.io" + soup.find("a", "btn btn-w-sm btn-light")['href']
r = requests.get(first_link, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
names = soup.find_all("a", "card-body text-center pt-1 pb-10")
for name in names:
	links.append("https://www.trackico.io" + name['href'])

while len(soup.find_all("a", "btn btn-w-sm btn-light")) == 2:

	link = "https://www.trackico.io" + soup.find_all("a", "btn btn-w-sm btn-light")[1]['href']
	r = requests.get(link, verify=False)
	soup = BeautifulSoup(r.text, 'html.parser')
	names = soup.find_all("a", "card-body text-center pt-1 pb-10")
	for name in names:
		links.append("https://www.trackico.io" + name['href'])




upcoming = []
for link in links:

	r2 = requests.get(link, verify=False)
	soup2 = BeautifulSoup(r2.text, 'html.parser')
	name = soup2.find("li", "breadcrumb-item active").text
	desc = soup2.find("small", "subtitle").p.text
	
	overview = soup2.find(id="tab-overview")
	dates = overview.find_all("div", "col-12 col-lg-6")
	pre_sale_date = dates[0].find("div", "flexbox mt-2").text
	token_sale_date = dates[1].find("div", "flexbox mt-2").text
	country =""
	tokentype =""
	boxes = soup2.find_all("div", "card card-body")
	for box in boxes:
		if box.h6 and "Country" in box.h6.text and box.find_all('span', 'fs-30'):
			country = box.find_all('span', 'fs-30')[1].text
		if box.h6 and "Platform" in box.h6.text and box.find_all('span', 'fs-30') and box.find_all('span', 'fs-30')[1].a:
			tokentype = box.find_all('span', 'fs-30')[1].a.text

	team = []
	members = soup2.find(id = "tab-team").find_all("a")
	for member in members:
		team.append(member['href'])

	twitter_telegram = soup2.find_all("a", "azm-twitter")
	twitter = ""
	telegram =""
	for link in twitter_telegram:
		if "t.me" in link['href']:
			telegram = link['href']
		if "twitter" in link['href']:
			twitter = link['href']
	website =""
	if soup2.find('a', 'azm-css3'):
		website = soup2.find('a', 'azm-css3')['href']
	whitepaper =""
	if soup2.find('a', 'azm-lastfm'):	
		whitepaper = soup2.find('a', 'azm-lastfm')['href']

	temp = {}
	temp["name"] = name
	temp["description"]= desc
	temp["category"]= ""
	temp["website"]= website
	temp["whitepaper"]= whitepaper
	temp["twitter"]=twitter
	temp["telegram"]=telegram
	temp["slack"]= ""
	temp["team"]= team
	temp["amt_raised"]=""
	temp["soft_cap"]=""
	temp["hard_cap"]=""
	temp["pre_sale_date"]=pre_sale_date
	temp["token_sale_date"]=token_sale_date
	temp["total_supply"]=""
	temp["country"] = country
	temp["tokentype"] = tokentype
	upcoming.append(temp)

pp.pprint(upcoming)




	


