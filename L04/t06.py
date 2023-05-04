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
from utilities import array_to_list
from utilities import list_to_array

llist = List()
source = [4, 5, 6]
target = []

array_to_list(llist, source)

for i in llist:
    print(i)

list_to_array(llist, target)
print(target)
