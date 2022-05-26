
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    pass

if __name__ == '__main__':
        meal_cost = float(input("Meal Cost: ").strip())

        tip_percent = int(input("Tip Percentage: ").strip())
        tip = (tip_percent / 100) * meal_cost

        tax_percent = int(input("Tax Percentage: ").strip())
        tax = (meal_cost / 100) * tax_percent

        total_cost = meal_cost + tip + tax

        solve(meal_cost, tip_percent, tax_percent)

        print(math.floor(total_cost))


#Task
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
#and tax percent (the percentage of the meal price being added as tax) for a meal,
#find and print the meal's total cost. Round the result to the nearest integer.