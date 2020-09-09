import pandas as pd 
dic = {1:"hello", 2:"goodbye"}
dic = {k:[v] for (k,v) in dic.items() }
print(pd.DataFrame(dic))
