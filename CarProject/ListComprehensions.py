# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []  # create an empty list
for i in range(1, 11):  # create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print("This is the long way:\n" + squares)


squares = [i * i for i in range(1, 11)]  # create a list AND defines what each loop iteration should do
print("This is the shorter way:\n" + squares)
