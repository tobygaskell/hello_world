import requests
import json 
import display.logo as logo 
import display.data as datadisplay
import pull.pull_from_api as pull 

def get_team_info(name):
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/search/{name}"
    data = pull.pull(url)
    start = data['api']['teams']
    for i in range(len(start)):
        print(start[i]['name'], "country: ", start[i]['country']) 
    wanted = input("-- Please pick the team you want? ")
    lot=[]
    for i in range(len(start)):
        if wanted.lower().title().strip() == start[i]['name']:
            team_data = start[i]
            lot.append(team_data)
    print(lot)
    if len(lot) == 1:
        team_data = lot[0]
        datadisplay.display_data(team_data)
    else:
        print([i['country'] for i in lot])
        country = input(f'Which country is your desired {wanted} based? ')
        for i in lot:
            if country in [i['country'], i['country'].lower()]:
                team_data = i 
                datadisplay.display_data(i)
    try:
        team_data = {k:[v] for (k,v) in team_data.items()}
        team_logo = team_data['logo'][0]
        logo.display_logo(team_logo)
    except UnboundLocalError:
        print("--ERROR-- No player with that name!")
        team_data = 'False'
    return team_data