from urllib.request import urlretrieve
import pandas as pd

#italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

#urlretrieve(italy_covid_url, './data/italy-covid-daywise.csv')


# how to read csv file

covid_df = pd.read_csv('./data/italy-covid-daywise.csv')

print(type(covid_df))

print(covid_df)


# how to get info about file

print(covid_df.info())


# use describe to view statistical information about numeric column

print(covid_df.describe())


# how to get the list of column names

print(covid_df.columns)


# find shape of the column and rows

print(covid_df.shape)


# Retrieve data from data frame

print(covid_df['new_cases'])


# Retrieve data with index

print(covid_df['new_cases'][247])


# retrieve data using 'at'

print(covid_df.at[247, 'new_cases'])


# retrieve a list of column data

print(covid_df[['new_cases', 'new_tests']])


# create a copy of dataframe

create_copy = covid_df.copy()
print(create_copy)




