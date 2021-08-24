from os import pardir
from urllib.request import urlretrieve
from numpy import positive
from numpy.lib.function_base import cov
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


# Retrieve data with row wise unig loc

print(covid_df.loc[1])

print(type(covid_df.loc[1]))

print(covid_df.loc[1:10])


# retrieve data from top to bottom using head

print(covid_df.head(10))


# retrieve data from bottom to top using tail

print(covid_df.tail(10))


# retrieve a data sample using sample

print(covid_df.sample(10))


# Analyzing data from data frames

total_cases = covid_df.new_cases.sum()
print(total_cases)

total_deaths = covid_df.new_deaths.sum()
print(total_deaths)

total_tests = covid_df.new_tests.sum()
print(total_tests)


test_per_day = total_tests / 248
print('test per day in italy: {:.2f}'.format(test_per_day))


death_rate = total_deaths / total_cases
print('death rate in italy: {:.2f} %'.format(death_rate*100))

initial_tests = 935310
total_tests = initial_tests + total_tests
print('total test in italy: ', total_tests)


positive_rate = total_cases / total_tests
print('positive rate in italy: {:.2f} %'.format(positive_rate*100))


# Querying and sorting rows

# one way
new_data = covid_df.new_cases > 1000
print(new_data)
high_cases_df = covid_df[new_data]
print(high_cases_df)


# another way
high_cases_df = covid_df[covid_df.new_cases > 1000]
print(high_cases_df)


# find high positive ratio data frame
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
print(high_ratio_df)
