# ###################################################################################################################################################
# ##########    From the finance file, deduce month by month, the difference. 1. Determine the monthly income 2. Determine the monthly change in income
# ##########    3. Determine the month with the highest and lowest income 4. Write each of the company data into different excel sheets7

# ## Monthly Collections
# #1. loop through all transactions
# #2. Check date of each transaction
# #3. Check amount on each transaction
# #4. Convert month from numeric to text value
# #5. Dump value in dictionary.

# import datetime
# file = open("financials.csv", "r")                                          # OPENFILEINREADMODE

# data = file.readlines()                                                     # READ FILE LINES
# data.pop(0)                                                                 # REMOVE THE FIRST LINE WHICH IS THE HEADER

# month_names = ["January",
# "February",
# "March",
# "April",
# "May",
# "June",
# "July",
# "August",
# "September",
# "October",
# "November",
# "December"]


# result_dict = dict.fromkeys(month_names, 0)                                  # empty dictionary to contain the values on collection

# #####    THIS PART ONLY RECORDS THE FINAL VALUES FOR EACH 
# # for transaction in data:

# #     split_transactions = transaction.split(",")                             # split individual transactions in individual values

# #     date = datetime.datetime.strptime(split_transactions[3], "%m/%d/%Y")    # convert string date to python object

# #     month_name = date.strftime("%B")                                        # get actual month name in text format

# #     transaction_amount = split_transactions[6]
# #     transaction_amount_as_number = float(transaction_amount)                # convert transaction amount to decimal number

# #     result_dict[month_name] = transaction_amount_as_number                  # APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME

# # print(result_dict)            

# for transaction in data:

#     split_transactions = transaction.split(",")                             # split individual transactions in individual values

#     date = datetime.datetime.strptime(split_transactions[3], "%m/%d/%Y")    # convert string date to python object

#     month_name = date.strftime("%B")                                        # get actual month name in text format

#     transaction_amount = split_transactions[6]
#     transaction_amount_as_number = float(transaction_amount)                # convert transaction amount to decimal number

#     if month_name in result_dict.keys():
#         result_dict[month_name] += transaction_amount_as_number             # APPEND THE AMOUNT TO THE DICTIONARY WITH CORRESPONDING MONTH NAME
#     else:
#         result_dict[month_name] = transaction_amount_as_number

# #print(result_dict)

# #     GET HIGHEST AND LOWEST MONTHS TRANSACTIONS

# #     print(result_dict.items())
# values_list = list(result_dict.items())
# #     print(values_list)
# values_list.sort(key = lambda val: val[1])
# #print(values_list[0])                                                       # LOWEST MONTH
# #print(values_list[-1])                                                      # HIGHEST MONTH


# # GET MONTHLY DIFFERENCE
# previous_month_name = "Non"
# previous_month_amount = 0

# for month, amount in result_dict.items():
#     #print(month, amount)

#     print(previous_month_name, month, amount - previous_month_amount)
#     previous_month_name = month
#     previous_month_amount = amount
  

########################################################################################################
###################### WRITE EACH COMPANY's TAXES INTO INDIVIDUAL FILES ################################

file = open("financials.csv", "r")                                          # OPENFILEINREADMODE

data = file.readlines()                                                     # READ FILE LINES
data.pop(0) 
destination_path = "C:/Users/tbuai/Desktop/UNIVEL_DATA_SCIENCE/PROGRAMS/company_data"

for transaction in data:

    split_transactions = transaction.split(",")                             # split individual transactions in individual values
    company_name = split_transactions[5]
    #print(split_transactions[5])

    company_file = open(f"{destination_path}/{company_name.replace('/','-')}.csv", "a")
    company_file.write(transaction)
    company_file.close()