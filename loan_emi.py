def loan_emi(amount, duration):
    emi = amount / duration
    return emi

eight_year_result = loan_emi(1260000, 8*12)
print(eight_year_result)


ten_year_result = loan_emi(1260000, 10*12)
print(ten_year_result)