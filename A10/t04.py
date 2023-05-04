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

from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(999999)
a.insert_rear(1)
a.insert_rear(12)
a.insert_rear(14)
a.insert_rear(15)
a.insert_rear(1123)
a.insert_rear(0)
a.insert_rear(-1)

Sorts.gnome_sort(a)

for i in a:
    print(i)
