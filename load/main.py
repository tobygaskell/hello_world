from sys import argv 
import pandas as pd


def load(data, object, save):
    new = pd.DataFrame(data)
    if save == 'true' :
        new.to_csv(f'data/{object}.csv', index = False)
    else:
        existing = pd.read_csv(f'data/{object}.csv' )
        output = check_row_exists(existing, new)
        output.to_csv(f'data/{object}.csv', index = False)





def check_row_exists(df, row): 
    loc = [key for key in row.columns if '_id' in key] 
    if len(loc) > 1: 
        print("!! Two ID columns identified!!", end ='\n')  
        print(loc, end ='\n')
        id_col = input('please pick the column you want to use as the ID! ')
        print(id_col)
    elif len(loc) == 1: 
        col = loc[0]
        new_id = row[col][0]
        if new_id not in list(df[col]): 
            df = df.append(row)
            df.drop('Unnamed: 0', axis = 1, inplace = True)
    return df 



