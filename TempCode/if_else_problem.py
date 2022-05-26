

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter number: ").strip(" "))

num1 = n%10
num2 = n
n = num1%2

print(n)

if n == 0 or 2<num2<5:
    print("Not Weird")

elif n == 1:
    print("Weird")


#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird