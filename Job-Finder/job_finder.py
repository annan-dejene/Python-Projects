import requests
from bs4 import BeautifulSoup


response = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')

html_text = response.text
soup = BeautifulSoup(html_text, 'lxml')


def skills_parser(skills_to_be_parsed):
    skills_parsed = []
    for s in skills_to_be_parsed:
        if len(s) > 2:
            skills_parsed.append(s.title())
        else:
            continue

    return ', '.join(map(str, skills_parsed))


def company_name_parser(comp_name_to_be_parsed):
    return ' '.join(map(str, comp_name_to_be_parsed))


jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name = company_name_parser(
        job.find('h3', class_='joblist-comp-name').text.split())
    skills = skills_parser(
        job.find('span', class_='srp-skills').text.split())
    experience = job.find(
        'ul', class_='top-jd-dtl clearfix').find('li').text.split('l')[-1]
    posted_time = job.find('span', class_='sim-posted').span.text

    print(f'''
    Company Name --------> {company_name}
    Skills Required -----> {skills}
    Experience ----------> {experience}

        {posted_time}
    ''')
    break
