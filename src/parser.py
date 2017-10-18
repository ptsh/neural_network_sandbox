from lxml import html
import requests
import datetime

date = datetime.datetime(2010, 1, 1, 0, 0)


while start_date != '20171007':
    print(start_date)
    page = requests.get('http://www.espnfc.com/scores?date=' + start_date)
    tree = html.fromstring(page.content)
    matches = tree.xpath('//div[contains(@class, "score-box")]//@data-gameid')

    for match_id in matches:
        match = requests.get('http://www.espnfc.com/match?gameId=' + match_id)
        match_tree = html.fromstring(match.content)
        team_1_name = match_tree.xpath('//span[contains(@class, "long-name")]/text()')[0]
        team_2_name = match_tree.xpath('//span[contains(@class, "long-name")]/text()')[1]
        team_1_abb = match_tree.xpath('//span[contains(@class, "abbrev")]/text()')[0]
        team_2_abb = match_tree.xpath('//span[contains(@class, "abbrev")]/text()')[1]
        print(team_1_name + "(" + team_1_abb +")" + " VS " + team_2_name + "(" + team_2_abb +")")
    date = date + datetime.timedelta(days=1)
    start_date = date.strftime('%Y%m%d')
