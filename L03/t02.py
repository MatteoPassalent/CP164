"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-31"
-------------------------------------------------------
"""

from Queue_array import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)

value2 = q.peek()
value = q.remove()
value3 = q.peek()

print(value2)
print(value)
print(value3)
print("")

for i in q:
    print(i)
