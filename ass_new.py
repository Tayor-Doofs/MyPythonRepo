###################################################################################################################################################
##########    From the finance file, deduce month by month, the difference. 1. Determine the monthly income 2. Determine the monthly change in income
##########    3. Determine the month with the highest and lowest income 4. Write each of the company data into different excel sheets7


financials = open("financials.csv", "r")

#print(financials.readline()[12:20]) #GET TAX TYPE VIA SLICING 
 
# headling_list = financials.readline().split(",")

# print(headling_list)
# print(headling_list[5])

# for line in financials.readlines():
#     # print(line)
#     print(line.split(",")[7])

cash_transactions = []
months = []

i = 1
for line in financials.readlines():
    transactions_month_number = line.split(",")[4]
    transactions_month = line.split(",")[5]
    transactions_year = line.split(",")[6]
    # print(transactions_month_number, transactions_month, transactions_year)

    if transactions_month_number == "1":
        print(line.split(",")[5], line.split(",")[9])
    elif transactions_month_number == "2":
        print(line.split(",")[5], line.split(",")[9])
    elif transactions_month_number == "3":
        print(line.split(",")[5], line.split(",")[9])
        # months.append(line.split(",")[5])
        # print(months)
        #cash_transactions.append(line.split(",")[9])
        #cash_transactions = [int(i) for i in cash_transactions]
        #print(cash_transactions)
           