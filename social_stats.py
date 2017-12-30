from bs4 import BeautifulSoup
import requests

telegram_invite_url = 'https://t.me/aidcoincommunity'
twitter_url = 'https://twitter.com/aid_coin'

def get_telegram_size(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	size = soup.find('div', 'tgme_page_extra').text
	size = size.replace(' ', '').replace('members', '')

	return int(size)

def get_twitter_size(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	size = soup.find('a', {'data-nav': 'followers'})['title']
	size = size.replace(',', '').replace(' ', '').replace('Followers', '')

	return int(size)

print(get_telegram_size(telegram_invite_url))
print(get_twitter_size(twitter_url))