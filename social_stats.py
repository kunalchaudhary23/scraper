from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession

def parse_telegram_background(session, response):
	try:
		soup = BeautifulSoup(response.text, 'html.parser')

		size = soup.find('div', 'tgme_page_extra').text
		size = size.replace(' ', '').replace('members', '')

		response.data = int(size)
	except:
		response.data = 'N/A'

def get_telegram_size(url):
	try:
		session = FuturesSession(max_workers=100)
		if url[0] == '/':
			url = 'http:' + url
		elif url[0] != 'h':
			return None
		future = session.get(url, background_callback=parse_telegram_background, verify=False)

		return future
	except:
		return None

def parse_twitter_background(session, response):
	try:
		soup = BeautifulSoup(response.text, 'html.parser')

		size = soup.find('a', {'data-nav': 'followers'})['title']
		size = size.replace(',', '').replace(' ', '').replace('Followers', '')

		response.data = int(size)
	except:
		response.data = 'N/A'

def get_twitter_size(url):
	try:
		session = FuturesSession(max_workers=100)
		if url[0] == '/':
			url = 'http:' + url
		elif url[0] != 'h':
			return None
		future = session.get(url, background_callback=parse_twitter_background, verify=False)

		return future
	except:
		return None