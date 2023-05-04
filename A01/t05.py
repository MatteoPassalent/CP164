"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-10-02"
-------------------------------------------------------
"""
principal = float(input("Principal: $"))
interest = float(input("Interest (decimal): "))
years = int(input("Number of years: "))
compounding = int(input("Number of times interest compounded per year: "))

middle = (1 + (interest / compounding))
balance = (middle) ** (compounding * years)
balance = principal * balance

print(f"\nBalance: ${balance}")
