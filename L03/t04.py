"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-02-01"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = [5, 4, 3, 2, 1]

for i in value:

    pq.insert(i)

v = pq.peek()
print(v)
print("")

for i in pq:
    print(i)
