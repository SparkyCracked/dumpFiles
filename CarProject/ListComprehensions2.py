# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------

student = []
amount_students = int(input("Amount of Students in your class: "))
n = 0
student_mark = []

while n < amount_students:
    student.append(input("Student name: "))
    student_mark.append(int(input("Enter " + student[n] + "'s mark for the test: ")))
    n = n + 1

passed_students = [i if i < 60 else "Fail" for i in student_mark]

x = 0
while x < n:
    print(str(student[x]) + " scored: " + str(passed_students[x]), end="\n")
    x = x+1



# students = [100, 90, 80, 70, 60, 40, 30, 0]
#
# passed_students = [i if i > 60 else "Failed" for i in students]
#
# print(passed_students)

# --------------------------------------------------------------
