from urllib.request import urlretrieve
import pandas as pd

#italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

#urlretrieve(italy_covid_url, './data/italy-covid-daywise.csv')


# how to read csv file

covid_df = pd.read_csv('./data/italy-covid-daywise.csv')

print(type(covid_df))

print(covid_df)



