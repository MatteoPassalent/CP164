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
from utilities import array_to_stack

stack = Stack()
source = [0, 1, 2, 3, 4, 5]

_ = array_to_stack(stack, source)

while not stack.is_empty():
    print(stack.pop())
