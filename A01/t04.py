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
cost = float(input("Cost of 1 pizza slice: $"))
quantity = int(input("Number of pizza slices: "))
total_cost = cost * float(quantity)

print(f"\nTotal cost of {quantity} pizza slices: ${total_cost: .2f}")
