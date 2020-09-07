import pull.pull_from_api as pull 
import json


def get_player_info_by_name(lastname):
    url = f'https://api-football-v1.p.rapidapi.com/v2/players/search/{lastname}'
    data = pull.pull(url)
    for i in range(len(data['api']['players'])):
        print(data['api']['players'][i]['player_name']) 
    wanted = input("which player do you want? ")
    for i in range(len(data['api']['players'])):
        if wanted == data['api']['players'][i]['player_name']:
            player_data = data['api']['players'][i]
            print(json.dumps(player_data, indent = 1))
    player_data = {k:[v] for (k,v) in player_data.items()}
    return player_data
