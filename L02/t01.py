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

s = Stack()

b = s.is_empty()

print(b)

c = s.push(1)
c = s.push(2)
c = s.push(3)

b = s.is_empty()
print(b)


value = s.pop()

print(value)

value = s.peek()

print(value)

value = s.pop()

print(value)

value = s.pop()

print(value)

b = s.is_empty()
print(b)
