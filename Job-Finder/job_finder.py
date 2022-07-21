from cmath import exp
import requests
from bs4 import BeautifulSoup


response = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')

html_text = response.text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    skills = job.find('span', class_='srp-skills').text
    experience = job.find('ul', class_='top-jd-dtl clearfix').li.text
    posted_time = job.find('span', class_='sim-posted').span.text

    print(f'''
    Company Name --------> {company_name}
    Skills Required -----> {skills}
    Experience ----------> {experience}

        {posted_time}
    ''')
    break
