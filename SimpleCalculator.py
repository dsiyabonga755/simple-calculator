# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:32:32 2026

@author: admi
"""

# A Simple Calculator
print("Simple Calculator")

num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("\nEnter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
    
elif operator == "-":
    print("Result:", num1 - num2)
    
elif operator == "*":
    print("Result:", num1 * num2)
    
elif operator == "/":
    print("Result:", num1 / num2)
    
else:
    print("Invalid operator")
    

# Make it loop without restarting

print("\nSimple Calculator")
while True:
    num1 = float(input("\nEnter first number: "))
    operator = input("\nEnter operator (+, -, *, /): ")
    num2 = float(input("\nEnter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    
    elif operator == "-":
        print("Result:", num1 - num2)
    
    elif operator == "*":
        print("Result:", num1 * num2)
    
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by 0.")
        
    else:
        print("Invalid operator")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    