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
    lop = []
    for i in range(len(start)):
        if wanted.lower().title().strip() == start[i]['player_name']:
            player_data = start[i]
            lop.append(player_data)
    if len(lop) == 1:
        player_data = lop[0]
        datadisplay.display_data(player_data)
    elif len(lop) == 0:
        print("-- There are no players with that name!! --")
    else:
        print(lop)
        print([i['nationality'] for i in lop])
        nationality = input(f'Which country is your desired {wanted} from? ')
        for i in lop: 
            if nationality in [i['nationality'], i['nationality'].lower()]:
                player_data = i 
                datadisplay.display_data(i)
    try:
        player_data = {k:[v] for (k,v) in player_data.items()}
    except UnboundLocalError:
        player_data = 'False'
    return player_data
