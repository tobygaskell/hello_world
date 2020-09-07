import json 
import player
import pandas as pd 
import pull.team as team


def check(*args): 
    print(args[0])
    if args[0][0] == "team_data":
        data = team.get_team_info(args[0][1])
    if args[0] == "player_data": 
        id_ = player.get_player_id(args[1]) 
    #if args[0] == "league_data": 
        #id_ = league.get_league_id(args[1]) 
    #return id_ 
    if 'first' in args[0]: 
        create_csv(data)
        return 
    load_csv(data)

def create_csv(data): 
    row = pd.DataFrame(data)
    row.to_csv('data/teams.csv')


def load_csv(data):
    existing = pd.read_csv('data/teams.csv')
    new = pd.DataFrame(data)
    appended = existing.append(new)
    appended.drop('Unnamed: 0', axis = 1, inplace = True)
    appended.to_csv('data/teams.csv')
    
    
