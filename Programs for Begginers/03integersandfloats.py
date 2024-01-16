# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:59:49 2020

@author: jayanth
"""
num0 = 3
num1 = 3.14
num2 = 2
# To know the class of a variable:
print(type(num0))
print(type(num1))
# Arithmetic Operators
print(num0 + num2)  # Addition
print(num0 - num2)  # Subtraction
print(num0 * num2)  # Multiplication
print(num0 / num2)  # Division (unavailable in v2.6)
print(num0 // num2) # Floor Division (Division after Round-off)
print(num0 ** num2) # Exponent
print(num0 % num2)  # Modulus (Reminder after division) Uselful in determining if a number is even or odd.
# BODMAS Rule
print(3 * 2 - 1)
print(3 * (2 - 1))
# Increment by 1.
num2 += 1
print(num2)
# Absolute Value
print(abs(1 - num2))
# Rounding Off a Value
print(round(3.75))
print(round(3.14))
# For specific number of round-off
print(round(3.75, 1))
print(round(3.14, 1))
# Comparison Operators
print(num0 == num2)  # Equal
print(num0 != num2)  # Not Equal
print(num0 > num2)  # Greater Than
print(num0 < num2)  # Less Than
print(num0 >= num2) # Greater or Equal
print(num0 <= num2) # Less or Equal
# Converting String type numbers to Integers
num_s = '100'
num_i = int(num_s)
print(num_i, type(num_i))
# Converting String type numbers to Hex based strings.
num_s = 'A5'
num_i = int(num_s, 16)
print(num_i, type(num_i))
num_h = hex(num_i)
print(num_h, type(num_h))