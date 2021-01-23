# names = ["sule", "kunle", "saheed"]

# mapped = map(lambda name: "Mr. "+name, names)
# print(list(mapped))

# MAP REDUCE FILTER

# MAP USAGE
# MAP DOES NOT NEED TO BE IMPORTED

# names = ["sule", "kunle", "saheed"]
# mapped = map(lambda name: "Mr. " + name, names)
# print(list(mapped))

# names = ["sule", "kunle", "saheed"]
# empty_list = []

# for name in names:
#     empty_list.append("Mr. " + name)


# CLASS WORK
# numbers = [23, 54, 31, 90, 34]
# max = 97

# function_pt = lambda n: f"{round((n/max)*100, 2)}%"

# numbers_pt = map(function_pt, numbers)
# print(list(numbers_pt))

# REDUCE
# from functools import reduce

# print(reduce(lambda x, y: x+y, numbers))

# FILTER

daily_sales = [23, 54, 31, 90, 34]
results = filter(lambda x: x < 10, daily_sales)
print(list(results))

