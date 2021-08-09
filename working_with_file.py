import os
from urllib.request import urlretrieve

path = os.getcwd()
print(path)

files = os.listdir('.')

print(files)


# os.makedirs('./data', exist_ok=True)


url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# urlretrieve(url1, './data/loan1.txt')
# urlretrieve(url2, './data/loan2.txt')
# urlretrieve(url3, './data/loan6.txt')


# how to open and close files
loan_file1 = open('./data/loan1.txt', mode='r')
loan_file1_content = loan_file1.read()
print(loan_file1_content)
loan_file1.close()

print('******************************')

#closing file automatically using (with)
with open('./data/loan2.txt') as loan_file2:
    loan_file2_content = loan_file2.read()
    print(loan_file2_content)

print("*******************************")

# read lines in files
with open('./data/loan3.txt', 'r') as loan_file3:
    loan_file3_content = loan_file3.readlines()
    print(loan_file3_content)

