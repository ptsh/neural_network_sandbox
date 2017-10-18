from prettytable import PrettyTable
from lxml import html
import requests
import datetime

date = datetime.datetime(2010, 1, 1, 0, 0)
start_date = date.strftime('%Y%m%d')

while start_date != '20171007':
    print(start_date)
    page = requests.get('http://www.espnfc.com/scores?date=' + start_date)
    tree = html.fromstring(page.content)
    matches = tree.xpath('//div[contains(@class, "score-box")]//@data-gameid')
    t = PrettyTable(['team 1', 'abbr 1', 'score 1', 'score 2', 'abbr2', 'team 2'])


    for match_id in matches:
        match = requests.get('http://www.espnfc.com/match?gameId=' + match_id)
        match_tree = html.fromstring(match.content)
        team_1_name = match_tree.xpath('//span[contains(@class, "long-name")]/text()')[0]
        team_2_name = match_tree.xpath('//span[contains(@class, "long-name")]/text()')[1]
        team_1_abb = match_tree.xpath('//span[contains(@class, "abbrev")]/text()')[0]
        team_2_abb = match_tree.xpath('//span[contains(@class, "abbrev")]/text()')[1]
        team_1_score = match_tree.xpath('//span[contains(@class, "score")]/text()')[0].replace('\n', '').replace('	',
                                                                                                                 '')
        team_2_score = match_tree.xpath('//span[contains(@class, "score")]/text()')[1].replace('\n', '').replace('	',
                                                                                                                 '')

        if team_1_score == '':
            team_1_score = 'Null'
        if team_2_score == '':
            team_2_score = 'Null'

        t.add_row([team_1_name, team_1_abb, team_1_score, team_2_score, team_2_abb, team_2_name])
    date = date + datetime.timedelta(days=1)
    start_date = date.strftime('%Y%m%d')
    print (t)
