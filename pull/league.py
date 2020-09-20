
import pull.pull_from_api as pull 
import display.data as datadisplay

def get_league_info(country):
    url = f"https://api-football-v1.p.rapidapi.com/v2/leagues/country/{country}"
    data = pull.pull(url)
    start = data['api']['leagues']
    names = [i for i in start if i['season'] == 2020]
    for i in names: 
        print(i['name'])
    league = input('which competition do you want info about? ')
    wanted = [i for i in names if league.lower().title().strip() == i['name']]
    if len(wanted) > 1: 
        print(wanted)
    elif len(wanted) == 1:
        league_data = {k:[v] for (k,v) in wanted[0].items()}
        datadisplay.display_data(wanted[0])
    else:
        print('!! there are no leagues of that name!')
    return league_data 





def get_all_teams_in_a_league(league_id):
    url = f'https://api-football-v1.p.rapidapi.com/v2/teams/league/{league_id}'
    data = pull.pull(url)
    datadisplay.display_data(data)



def get_all_rounds_from_league_id(league_id):
    url = f'https://api-football-v1.p.rapidapi.com/v2/fixtures/rounds/{league_id}'
    data = pull.pull(url)
    datadisplay.display_data(data)

def get_fixtures_by_leagueid_round(league_id, round):
    url = f'https://api-football-v1.p.rapidapi.com/v2/fixtures/league/{league_id}/{round}'
    data = pull.pull(url)
    datadisplay.display_data(data)


if __name__ == '__main__':
    get_all_teams_in_a_league(2790)


