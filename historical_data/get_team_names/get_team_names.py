import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

url = 'http://www.espn.com/nba/teams'
r = requests.get(url)

soup = BeautifulSoup(r.text)
divisions = soup.find_all('section', class_='ContentList mt4 ContentList--NoBorder')

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []

for division in divisions:
    for team in division.find_all('section', class_='ContentList__Item'):
        team_url = team.find('div').find('section').find('a')['href']
        team_name = team.find('div').find('section').find('div', class_='pl3').find('a').find('h2').text
        teams.append(team_name)
        teams_urls.append('www.espn.com' + team_url)
        prefix_1.append(team_url.split('/')[-2])
        prefix_2.append(team_url.split('/')[-1])


dic = {'url': teams_urls, 'prefix_2': prefix_2, 'prefix_1': prefix_1}
teams = pd.DataFrame(dic, index=teams)
teams.index.name = 'team'
teams.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'teams.csv'), index=True, sep="|")