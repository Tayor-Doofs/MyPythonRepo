PersonName = input("What is your name?")      
Age = int(input("How old are you?"))
YearOfBirth = 2020 - Age

print(PersonName, "was born in", YearOfBirth)

print("Was", PersonName, "born after 1989?")
print(YearOfBirth > 1989)