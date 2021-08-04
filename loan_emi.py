def loan_emi(amount, duration, down_pyment=0):
    loan_amount = amount - down_pyment
    emi = loan_amount / duration
    return emi

eight_year_result = loan_emi(1260000, 8*12, 3e5)
print(eight_year_result)


ten_year_result = loan_emi(1260000, 10*12)
print(ten_year_result)