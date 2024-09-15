# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
print('Enter weight: (int of float)')
weight = float(input())
print('Enter height: (int of float)')
height = float(input())

print(f'Your BMI = {weight/(height**2)}')
#code here

