# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
print("Insert a integer to calculate sum of it's digits")
ii = int(input())

sum = 0
while ii != 0:
    sum += ii % 10
    ii /= 10
    ii = int(ii)

print(f'Sum of digits euqals {sum}')
