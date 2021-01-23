# #############################
# #####  DICTIONARIES  ########
# #############################

# ## CREATING DICTIONARIES ##

# # DIRECT CREATION

# MY_DICT = {
#     "john":["singing", "dancing"],
#     "ali":["jumping", "dancing"],
#     "simbi":["ten ten", "eating"]
# }
# print(MY_DICT)

# DICTIONARY = {
#     "happy": "a situation where someone is very excited",
#     "sad": "a situation where someone is not excited"
# }
# print(DICTIONARY["happy"])


# names = ["samuel", "lucas", "mary"]
# ages = [34, 21, 19]
# print(list(zip(names, ages)))

my_dict = dict() #empty dictionaries can be created using the dict builtin function

# new_dict = dict(zip(names, ages))

# print(new_dict)



### UPDATING DICTIONARIWS

# print(my_dict)

# my_dict["laptops"] = ["hp", "acer", "dell", "toshiba"]
# my_dict["phones"] = ["apple", "samsung", "nokia"]
# my_dict["sneakers"] = ["nike air", "jordans", "jeezy's", 12]
# my_dict[12] = "INVALID ... OOPS...!!!"

# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())



import datetime
# # print(datetime.date.today())
# # print(datetime.datetime.now())

# time_now = datetime.datetime.now()

# print("day :", time_now.day, "Day name :", time_now.strftime("%A"))
# print("month :", time_now.month)
# print("year :", time_now.year)
# print("hour :", time_now.hour)
# print("minute :", time_now.minute)
# print("second :", time_now.second)
# print("micro :", time_now.microsecond)

# print(time_now.strftime("%A"))
# print(time_now.strftime("%b %d, %Y, %I, %M%p"))

# sample_date = "20202012"

# print(datetime.datetime.strptime(sample_date, "%Y%d%m").strftime("%b %d, %Y %I:%M%p"))
import pprint

bio_dict = dict()

for i in range(10):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    Bio = input("Short Bio: ")

    time_created = datetime.datetime.now().strftime("%b %d, %Y %I:%M%p")

    bio_dict[name] = {
        "age": age,
        "Bio": Bio,
        "time_created": time_created
    }

    action= input("Print do you want to aa another ?? y/n : ")
    if action == "n":
        break

# print(name, age)
# print(Bio)
# print("created at : ", time_created)
pprint.pprint(bio_dict)