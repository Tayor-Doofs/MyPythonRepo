# annual_interest = 0.1
# monthly_interest = annual_interest/12
# number_of_months = 3

# principal = 100000

# interest = monthly_interest * principal * number_of_months
# print (interest)


annual_interest = float(input('Please input the interest rate :'))/100
monthly_interest = annual_interest/12
number_of_months = 3

principal = float(input('Please input the loan amount :'))

interest = monthly_interest * principal * number_of_months
print ('',interest)

