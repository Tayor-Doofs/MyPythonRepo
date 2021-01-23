import math

value_list = []

while True:

    value = input("Please enter values to input: ")
    if value.lower() == 'q':
        break

    value_to_integer = int(value)

    value_list.append(value_to_integer)
    print("\nNumbers collected: ", len(value_list), "\n")

print(value_list)
number_of_samples = len(value_list)

mean_of_numbers = sum(value_list)/number_of_samples
print("MEAN: ", mean_of_numbers)

x_xbar_map = map(lambda sample: round(sample - mean_of_numbers, 2), value_list)
x_xbar_values = list(x_xbar_map)
print("\nX_XBAR: \n", x_xbar_values)

x_xbar_squared_map = map(lambda sample: round(sample**2), x_xbar_values)
x_xbar_squared_values = list(x_xbar_squared_map)
print("\nX_XBAR_SQUARED: \n", x_xbar_squared_values)

variance = round(math.sqrt(sum(x_xbar_squared_values)/(number_of_samples - 1)), 2)
print("\nVARIANCE: \n", variance)


file = open("assignment.csv", "w")
file.write("VALUE,X_XBAR,X_BAR_SQ")

print(f"{('VALUE').center(6)} | {('X_BAR').center(6)} | {('X_BAR_SQ').center(6)}")
print('-'*24)

for i in range(number_of_samples):

    print(f"{str(value_list[i]).center(6)} | {str(x_xbar_values[i]).center(6)} | {str(x_xbar_squared_values[i]).center(6)}")

    file.write(f"{value_list[i]}, {x_xbar_values[i]}, {x_xbar_squared_values[i]}\n")

