import math

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


total_amount = 1260000
no_of_year = 8*12
rate_of_interest = 10
pay_amount = 3e5
emi1 = loan_emi(amount=total_amount, 
                            duration=no_of_year, 
                            rate=rate_of_interest, 
                            down_payment=pay_amount)
print(emi1)


emi2 = loan_emi(amount=1260000, duration=10*12, rate=0)
print(emi2)


if emi1 < emi2:
    print('option 1 is lower EMI s{}'.format(emi1))
else:
    print('option 2 is lower EMI s{}'.format(emi2))