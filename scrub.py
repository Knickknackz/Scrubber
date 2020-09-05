import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Developer&where=United%20States'

for i in range(2, 100):
    page = requests.get(URL+'&stpage=' + str(i-1) + '&page=' + str(i))

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')


    python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")