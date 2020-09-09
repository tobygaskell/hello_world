from sys import argv 
import pandas as pd


def load(data, object, save):
    type = ''
    if object == 'player_data':
        type = 'players'
    elif object == 'team_data':
        type = 'teams'
    elif object == 'league_data':
        type = 'leagues'
    new = pd.DataFrame(data)
    if save == 'true' :
        new.to_csv(f'data/{type}.csv')
    else:
        existing = pd.read_csv(f'data/{type}.csv')
        if new[f'{type[:-1]}_id'][0] not in list(existing[f'{type[:-1]}_id']):
            appended = existing.append(new, ignore_index = True)
            appended.drop('Unnamed: 0', axis = 1, inplace = True)
            appended.to_csv(f'data/{type}.csv')
