import requests
import json 

def pull(url):
    headers = {'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
               'x-rapidapi-key': "c353bf85damsh1032ad157d425a6p15acc8jsn697e609db7c1"}
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text) 
    return data 