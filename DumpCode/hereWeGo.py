phrase = "Giraffes are so tall my guy."
print(phrase[0].lower() + "\tis the first character")
print("1st letter is uppercase: ")
print(phrase[0].isupper())

print("Last letter is special character: ")
print(phrase[-1].isascii())

length = len(phrase)
print("Length of phrase: " + str(length))
print(phrase.index("a"))
print(phrase.replace("Giraffe", "Elephant"))

lengthLast = length % 10
print(lengthLast)
print(phrase[length-1] + " is the " + str(length) + "th character")
