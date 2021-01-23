# ### LISTS - COMMA SEPERATED VALUES INSIDE SQUARE BRACES

# fruits = ["apples", "potatoes", "yams"]

# print(fruits)
# print("Variable fruits is of type -: ", type(fruits))

# ### ADD TO THE FRUITS LIST USING APPEND METHOD

# # fruit_to_add = "fish"

# print()
# fruits.append("fish")
# print("## AFTERAPPENDING")
# print(fruits)

# print()
# fruits.append([1,2,3,4])
# print("## AFTERAPPENDING")
# print(fruits)

# ### REMOVE FROM THE FRUITS LIST USING REMOVE METHOD

# print()
# print("## AFTER REMOVE")
# fruits.remove("yams")
# print(fruits)

# ### COUNT FROM THE FRUITS LIST USING .COUNT METHOD

# print()
# fruits.append("apples")
# number_of_times_apples_occures_in_list = fruits.count("apples")
# print("apples occurs: ", number_of_times_apples_occures_in_list)

# ### .EXTEND METHOD

# print()
# new_list = ["pineapples", "avocado", "pear", "oranges"]
# fruits.extend(new_list)
# print(fruits)

# ### .INSERT METHOD

# print()
# fruits.insert(0, "cashew")
# print(fruits)

# ### .POP METHOD

# print()
# fruits.pop(0)
# print(fruits)


# #INDEXING AND SLICING

# print(fruits[0])

# for i in range(4):
#     print(fruits[i], " - at position ", i)

# i = 0
# while i < 4:
#     print(fruits[i], " - at position ", i)
#     i += 1


# ### SLICING LIST
# print()
# data_list = ["ali", "benky", "sule", 2, 3, 12, 14, True, False, True, False]

# strings = data_list[0:3]
# numbers = data_list[3:7]
# booleans = data_list[8:11]
# jumping_steps = data_list[0:12:2]  #start stop step
# slice_out_becky_3 = data_list[1:5]

# print("Strings List -->", strings)
# print("Numebr list -->", numbers)
# print("Booleans list -->", booleans)
# print("jumping list -->", jumping_steps)
# print("slice_out_example -->", slice_out_becky_3)

# # i = 0
# # while i < 4:
# #     print(slice_out_becky_3[i], i)
# #     i += 1

# i = 0
# while i < len(data_list):
#     print(data_list[i], i)
#     i += 1


financials = open("financials.csv", "r")

print(financials.readline()[12:20]) #GET TAX TYPE VIA SLICING 

headling_list = financials.readline().split(",")

# print(headling_list)
# print(headling_list[5])

# for line in financials.readlines():
#     print(line.split(",")[7])

# cash_transactions = []

for line in financials.readlines():
    transactions_type = line.split(",")[7]
    print(transaction_type)

    if transactions_type== "Own Bank Che...":
        print(line.split(",")[5], line.split(",")[8])


# ### ASSINGMENT 
# OF UNIQUE COMPANIES IN THE FILE AND HOW MUCH THEY PAID IN TAX EACH AND PLACE IN A DICTIONARY

