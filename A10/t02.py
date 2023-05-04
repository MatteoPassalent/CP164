"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-04-08"
-------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List

lst = List()

lst.append(9999)
lst.append(12)
lst.append(1)
lst.append(120)
lst.append(19)
lst.append(0)

Sorts.radix_sort(lst)

for i in lst:
    print(i)
