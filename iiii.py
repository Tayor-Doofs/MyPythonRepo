# x = list(range(1,10))
# y = list(range(1,10))
# z = list(range(1,10))

# # print(x)

# for i in x:
#     for j in y:
#         for k in z:
#             if (100*i + 10*j + k)*3 == (100*k + 10*k + k):
#                 print(100*i + 10*j + k)


for i in range(100,999):
    number_multiplied_by_three = i * 3
    last_digit = str(i)[2]*3

    print(i, number_multiplied_by_three, last_digit, number_multiplied_by_three == int(last_digit))

    if number_multiplied_by_three == int(last_digit)
        break