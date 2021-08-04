import math

def loan_emi(amount, duration, rate, down_payment=0):
    rate = (rate/100)*12
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1 + rate)** duration) / (((1 + rate)**duration) - 1)
    emi = math.ceil(emi)
    return emi

eight_year_result = loan_emi(1260000, 8*12, 10, 3e5)
print(eight_year_result)


ten_year_result = loan_emi(1260000, 10*12, 8)
print(ten_year_result)