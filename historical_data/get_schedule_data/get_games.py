import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import os

def get_games(year=2012):
    teams = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../get_teams/teams.csv'), sep="|")
    BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{0}/year/{1}/seasontype/2'

    match_id = []
    dates = []
    home_team = []
    home_team_score = []
    visit_team = []
    visit_team_score = []

    for index, row in teams.iterrows():
        _team, url = row['team'], row['url']
        url = BASE_URL.format(row['prefix_1'], year)
        r = requests.get(url)
        table = BeautifulSoup(r.text).table
        for row in table.find_all('tr')[1:]: # Remove header
            columns = row.find_all('td')
            if columns[1].text == 'OPPONENT' or columns[2].text == 'Canceled' or columns[2].text == 'Postponed':
                pass
            else:
                _home = True if columns[1].li.text == 'vs' else False
                _other_team = columns[1].find_all('a')[1].text
                _score = columns[2].a.text.split(' ')[0].split('-')
                _won = True if columns[2].span.text == 'W' else False
                match_id.append(columns[2].a['href'].split('id/')[1])
                home_team.append(_team if _home else _other_team)
                visit_team.append(_team if not _home else _other_team)
                d = datetime.strptime(columns[0].text + ' ' + str(year), '%a, %b %d %Y')
                dates.append(date(year, d.month, d.day))
                if _home:
                    if _won:
                        home_team_score.append(_score[0])
                        visit_team_score.append(_score[1])
                    else:
                        home_team_score.append(_score[1])
                        visit_team_score.append(_score[0])
                else:
                    if _won:
                        home_team_score.append(_score[1])
                        visit_team_score.append(_score[0])
                    else:
                        home_team_score.append(_score[0])
                        visit_team_score.append(_score[1])

    dic = {'id': match_id, 'date': dates, 'home_team': home_team, 'visit_team': visit_team,
            'home_team_score': home_team_score, 'visit_team_score': visit_team_score}

    games = pd.DataFrame(dic).drop_duplicates(subset='id').set_index('id')

    return games

if __name__ == '__main__':
    get_games()
