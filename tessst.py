# num = 0

# for i in range(2,14,3):
#     for j in range(3,5):
#         num += j

# print(num)


# def summation(n):
#     total = 0
#     for i in range(n):
#         total += i
#         return total
#         print(summation(n))
# print(summation(5))

n = int(input("please enter a number"))
print("the number has two digits")
if n > 0:
    print("the number is positive")
    if n%2 == 0:
        print("the number is even")

    elif n == 50:
        print("the number is 50")
else:
    print("the number is not even")