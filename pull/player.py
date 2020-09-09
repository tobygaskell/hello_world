import pull.pull_from_api as pull 
import json
import display.data as datadisplay

def get_player_info_by_name(lastname):
    url = f'https://api-football-v1.p.rapidapi.com/v2/players/search/{lastname}'
    data = pull.pull(url)
    start = data['api']['players']
    for i in range(len(start)):
        print(start[i]['player_name'], " country: ", start[i]['nationality']) 
    wanted = input("-- Please pick the player you want? ")
    for i in range(len(start)):
        lop = []
        if wanted in [start[i]['player_name'], start[i]['player_name'].lower()]:
            player_data = start[i]
            lop.append([player_data['player_name'], player_data['nationality']])
            if len(lop) == 1:
                player_data = start[i]
                datadisplay.display_data(player_data)
            else:
                print(lop)
    try:
        player_data = {k:[v] for (k,v) in player_data.items()}
    except UnboundLocalError:
        print("--ERROR-- No player with that name!")
        player_data = 'False'
    return player_data
