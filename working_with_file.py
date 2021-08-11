import os
from urllib.request import urlretrieve
import math

# path = os.getcwd()
# print(path)

# files = os.listdir('.')

# print(files)


# # os.makedirs('./data', exist_ok=True)


# url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
# url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
# url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'


# urlretrieve(url1, './data/loan1.txt')
# urlretrieve(url2, './data/loan2.txt')
# urlretrieve(url3, './data/loan3.txt')


# # how to open and close files
# loan_file1 = open('./data/loan1.txt', mode='r')
# loan_file1_content = loan_file1.read()
# print(loan_file1_content)
# loan_file1.close()

# print('******************************')

# #closing file automatically using (with)
# with open('./data/loan2.txt') as loan_file2:
#     loan_file2_content = loan_file2.read()
#     print(loan_file2_content)

# print("*******************************")

# # read lines in files
# with open('./data/loan3.txt', 'r') as loan_file3:
#     loan_file3_content = loan_file3.readlines()
#     print(loan_file3_content)



with open('./data/loan1.txt', 'r' ) as loan_file:
    file_data = loan_file.readlines()


def parse_header(file_line):
    return file_line.strip().split(',')

header = parse_header(file_data[0])
# print(header)


def parse_value(file_line):
    values = []
    for item in file_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except:
                values.append(item)
    return values

float_num = parse_value(file_data[3])
print(float_num)


def create_dict(values, headers):
    item_dict = {}
    for value, header in zip(values, headers):
        item_dict[header] = value
    return item_dict

show_dict = create_dict(float_num, header)
# print(show_dict)


def read_csv(path):
    result = []
    with open(path, 'r') as file:
        line = file.readlines()
    
    headers = parse_header(line[0])

    for item in line[1:]:
        values = parse_value(item)

        item_dict = create_dict(values, headers)
        result.append(item_dict)
    return result

loans = read_csv('./data/loan1.txt')

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal montly installment (EMI) for a loan.
    
    Arguments:
        amount - Total amount to be spent (loan + down payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    rate = (rate/100)*12
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1 + rate)** duration) / (((1 + rate)**duration) - 1)
    except:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi

def compute_emi(loans):
    for loan in loans:
        loan['emi'] = loan_emi(loan['amount'],
                                loan['duration'],
                                loan['rate']/12,
                                loan['down_payment'])


compute_emi(loans)
# print(loans)

# with open('./data/emi1.txt', 'w') as f:
#     for loan in loans:
#         f.write('{},{},{},{},\n'.format(loan['amount'],
#                                         loan['duration'],
#                                         loan['rate'],
#                                         loan['down_payment'],
#                                         loan['emi']))

# with open('./data/emi1.txt', 'r') as f:
#     print(f.read())


def write_csv(items, path):
    with open(path, 'w') as f:
        if len(items) == 0:
            return
        
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')


        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + '\n')


write_csv(loans, './data/emi1.txt')


# for i in range(1,4):
#     loan = read_csv('./data/loan{}.txt'.format(i))
#     compute_emi(loan)
#     write_csv(loan, './data/emi{}.txt'.format(i))