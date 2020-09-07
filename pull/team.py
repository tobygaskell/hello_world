import requests
import json 
import display.logo as logo 

def get_team_info(name):
    url = f"https://api-football-v1.p.rapidapi.com/v2/teams/search/{name}"
    headers = {'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key': "c353bf85damsh1032ad157d425a6p15acc8jsn697e609db7c1"}
    response = requests.request("GET", url, headers=headers)
    data2 = json.loads(response.text) 
    for i in range(len(data2['api']['teams'])):
        print(data2['api']['teams'][i]['name']) 
    wanted = input("please pick the team you want ")
    for i in range(len(data2['api']['teams'])):
        if wanted == data2['api']['teams'][i]['name'].lower():
            team_data = data2['api']['teams'][i]
            team_logo = team_data['logo']
    logo.display_logo(team_logo)
    print('hello')
    print(json.dumps(team_data, indent = 1))
    team_data = {k:[v] for (k,v) in team_data.items()}
    return team_data  
