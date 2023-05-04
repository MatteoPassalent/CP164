"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""

from List_linked import List
l = List()

l.append(5)
l.append(99)
l.remove(99)
for v in l:
    print(v)

print(l[0])
l[0] = 66
print(l[0])
