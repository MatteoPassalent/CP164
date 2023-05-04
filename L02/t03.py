"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array

stack = Stack()
target = []

for i in range(6):
    stack.push(i)

_ = stack_to_array(stack, target)

print(target)
