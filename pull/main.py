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
    if data != 'False':
        load.load(data, argv[0], argv[-1])
    return 