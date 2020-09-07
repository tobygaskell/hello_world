import json 
from sys import argv
import pandas as pd 
import pull.team as team
import pull.player as player 
import pull.league as league 
import load.main as load 

def check(argv): 
    if argv[0] == "team_data":
        data = team.get_team_info(argv[1])
    if argv[0] == "player_data": 
        data = player.get_player_info_by_name(argv[1]) 
    if argv[0] == "league_data": 
        data = league.get_league_info(argv[1]) 
    load.load(data, argv[0], argv[-1])










def create_csv(data): 
    row = pd.DataFrame(data)
    row.to_csv('data/teams.csv')


def load_csv(data):
    existing = pd.read_csv('data/teams.csv')
    new = pd.DataFrame(data)
    appended = existing.append(new)
    appended.drop('Unnamed: 0', axis = 1, inplace = True)
    appended.to_csv('data/teams.csv')
    
    
