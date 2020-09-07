from sys import argv 
import pandas as pd


def load(data, object, save):
    type = ''
    print(object)
    if object == 'player_data':
        type = 'players'
    elif object == 'team_data':
        type = 'teams'
    elif object == 'league_data':
        type = 'leagues'
    print(type)
    new = pd.DataFrame(data)
    if save == 'true' :
        new.to_csv(f'data/{type}.csv')
    else:
        existing = pd.read_csv(f'data/{type}.csv')
        appended = existing.append(new)
        appended.drop('Unnamed: 0', axis = 1, inplace = True)
        appended.to_csv(f'data/{type}.csv')