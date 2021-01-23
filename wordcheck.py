word = input("Please enter base word :")
other_word = input("Please enter word to check :")

print(other_word, "was found : ", other_word in word)

if "Mr" in word:
    print("Good day Sir")

elif "Mr" not in word:
    print("Baba how far...!!")