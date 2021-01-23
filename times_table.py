import csv

value = int(input("What times-table do you want to see"))

time_table = open("time_table.csv", "w")

for i in range(1,13):

	time_table.write(f"{2} , {i} , {value * (i)} \n")

time_table.close()

# time_table = open("Twotimes1.csv", "r")

# print(time_table.read())
time_table.close()

