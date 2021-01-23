# ### ASSINGMENT 
# OF UNIQUE COMPANIES IN THE FILE AND HOW MUCH THEY PAID IN TAX EACH AND PLACE IN A DICTIONARY

file = open("financials.csv", "r")
file_lines = file.readlines()
file_lines.pop(0)

cash_transactions = []

target_company = "CHI LIMITED"
total = 0


for line in file_lines:

    company_name = line.split(",")[5]
    amount_paid = float(line.split(",")[6])

    if company_name == target_company:

        total += amount_paid
        print(line.split(",")[5], line.split(",")[8])

#print(target_company, " : \nTotal ==> ", total)


file.close()

#### GET UNIQUE COMPANY NAMES ########

all_company_names = []

for line in file_lines:

    comapany_name = line.split(",")[5]
    all_company_names.append(comapany_name)

my_list = all_company_names
my_set = set(my_list)
# print(my_set)

cash_transactions = []

target_company = "CHI LIMITED"
total = 0

amount_paid_by_company = []
amount_paid_by_companies = []

for target_company in my_set:

    total = 0
    for line in file_lines:

        company_name = line.split(",")[5]
        amount_paid = float(line.split(",")[6])

        if company_name == target_company:

            total += amount_paid

    #print(target_company, " : \nTotal ==> ", total)
    
    amount_paid_by_companies.append([target_company, total])
amount_paid_by_companies.sort(key = lambda amount: amount[1], reverse = True)
dict = dict(amount_paid_by_companies[:10])
print(dict)
    
# amount_paid_by_companies.append()

    
    


