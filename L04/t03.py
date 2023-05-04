"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-02-09"
-------------------------------------------------------
"""

from List_array import List

source = List()

source.append(5)
source.append(6)
source.insert(0, 4)
r = source.remove(5)

print(r)
for i in source:
    print(i)
