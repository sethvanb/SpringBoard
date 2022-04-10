import mlbgame
# import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# month = mlbgame.games(2021, 6, home='Giants')
# games = mlbgame.combine_games(month)
# print(month[0])
# print((month[0]).game_id)
# stats = mlbgame.player_stats((month[0]).game_id)
# for player in stats.home_batting:
#     print(player)

month = mlbgame.games(2021, home='Giants', away='Giants')
games = mlbgame.combine_games(month)
for game in games:
    print(game)