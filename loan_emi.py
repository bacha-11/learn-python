import math

def loan_emi(amount, duration, rate, down_payment=0):
    rate = (rate/100)*12
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1 + rate)** duration) / (((1 + rate)**duration) - 1)
    emi = math.ceil(emi)
    return emi


total_amount = 1260000
no_of_year = 8*12
rate_of_interest = 10
pay_amount = 3e5
eight_year_result = loan_emi(amount=total_amount, 
                            duration=no_of_year, 
                            rate=rate_of_interest, 
                            down_payment=pay_amount)
print(eight_year_result)


ten_year_result = loan_emi(amount=1260000, duration=10*12, rate=8)
print(ten_year_result)