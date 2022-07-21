import requests
from bs4 import BeautifulSoup


response = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')

html_text = response.text
soup = BeautifulSoup(html_text, 'lxml')

job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_='joblist-comp-name').text