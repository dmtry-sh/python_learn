import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html, "lxml")
	table = soup.find('div', class_='page_content')

	projects = []

	rows = table.find_all('div', class_='row')[:-1]
	for row in rows:
		projects.append({
			'title': row.find('a').text,
			'categories': [category.text for category in row.find_all('a', class_='text-muted')],
			'amount': row.find('div', class_='amount').text,
			'applications': int(row.find('div', class_='text_field').text[-24:-20])
			})
	
	print(projects)

def main():
	parse(get_html('https://www.weblancer.net/jobs/'))

	


if __name__ == '__main__':
	main()

