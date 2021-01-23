name =input('Enter your Name')
age =int(input('Enter your age'))
years_of_experience = int(input("please enter your years of experience:"))

current_year = 2020
year_of_birth = current_year - age

min_allowable_year_of_birth = 1989
max_allowable_year_of_birth = 2001
years_of_experience_for_exception = 3


response = year_of_birth > min_allowable_year_of_birth and \
          year_of_birth < max_allowable_year_of_birth or \
          years_of_experience >= years_of_experience_for_exception and \
          not (years_of_experience > age)


print("Thank you for applying",name)
print("You met all criteria : ",response)