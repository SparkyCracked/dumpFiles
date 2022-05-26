

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

if n == 1:
    print("Weird")

elif n == 0 and 2 <= num2 <= 5:
    print("Not Weird")

elif n == 0 and 6 <= num2 <= 20:
    print("Weird")

elif n == 0 and num2 > 20:
    print("Not Weird")

else:
    print("not a number in range")

