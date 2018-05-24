import urllib.request
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://www.weblancer.net/jobs/'

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def get_page_count(html):
	soup = BeautifulSoup(html, "lxml")
	table = soup.find('div', class_='page_content')
	rows = table.find_all('div', class_='row')
	pages = rows[-1].find_all('a')
	last_page = int(pages[-1]['href'][-3:])
	return last_page

def parse(html):
	soup = BeautifulSoup(html, "lxml")
	table = soup.find('div', class_='page_content')

	projects = []

	rows = table.find_all('div', class_='row')
	for row in rows[:-1]:
		projects.append({
			'title': row.find('a').text,
			'categories': [category.text for category in row.find_all('a', class_='text-muted')],
			'amount': '??' if row.find('div', class_='amount').text == '' else row.find('div', class_='amount').text,
			'applications': int(row.find('div', class_='text_field').text[-24:-20]) if row.find('div', class_='text_field').text[-24:-20] != '' else 0
			})

	return projects

def save(projects, path):
	with open(path, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(('Проект', 'Категории', 'Цена', 'Заявки'))

		for project in projects:
			writer.writerow((project['title'],', '.join(project['categories']), project['amount'], project['applications'])) 


def main():

	page_count = get_page_count(get_html(BASE_URL))
	print('Всего найдено страниц: {}'.format(page_count))

	projects = []

	for page in range(1, page_count):
		print('Парсинг {} стр.'.format(page))
		projects.extend(parse(get_html(BASE_URL + '?page={}'.format(page))))

	save(projects, 'weblancer_projects.csv')

	print('Парсинг завершён!')

if __name__ == '__main__':
	main()
