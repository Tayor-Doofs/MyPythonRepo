#let's call the three friend's: A, B, & C

A_share = int(input("A, How many sweets do you have?"))        #A_share is the number of sweets A gets every morning before going to school

B_share = int(input("B, How many sweets do you have?"))        #B_share is the number of sweets B gets every morning before going to school

C_share = int(input("C, How many sweets do you have?"))        #C_share is the number of sweets C gets every morning before going to school

print("The three of you get", (A_share + B_share + C_share)//3, "sweets each.")         #prints the number of sweets each get

if (A_share + B_share + C_share)%3 == 0:
    print("No available sweets to be crushed.")                #prints this if the remaining sweets after sharing equally is zero
else:
    print("The remaining", (A_share + B_share + C_share)%3, "sweets would be crushed.") #prints this if there is a remainder