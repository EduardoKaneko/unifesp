# DAY 02: Operators

import math
import os
import random
import re
import sys

mealCost = float(input())
tipPercent = (float(input())/100)
taxPercent = (float(input())/100)


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    totalCost = mealCost + (tipPercent*mealCost) + (taxPercent*mealCost)
    return round(totalCost)

print(solve(mealCost, tipPercent, taxPercent))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)