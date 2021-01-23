#Program to reverse a word

word = input("Enter word..")
reversed_word = reversed(word)

print("".join(reversed_word))


#To check if a word is a palindrome

if "".join(reversed_word) == word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
