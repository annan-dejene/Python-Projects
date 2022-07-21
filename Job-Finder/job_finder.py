import requests
from bs4 import BeautifulSoup


job_search = input('In What area are you searching a Job for: ')
response = requests.get(
    f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_search}&txtLocation=')

if response.status_code != 200:
    print('Error: ', response.status_code)
    exit()

input(
    f'\nWe will scrape this site\n{response.url}\nPress Enter to Continue...')

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

    if 'few' in posted_time:
        print(f'''
        Company Name --------> {company_name}
        Skills Required -----> {skills}
        Experience ----------> {experience}

            {posted_time}
        ''')

    break
