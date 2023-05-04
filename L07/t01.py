"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""

from List_linked import List

mylist = List()
target = List()
target1 = List()
target2 = List()
inter = List()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)

target.append(1)
target.append(2)
target.append(3)
target.append(4)


input()
print(mylist.is_identical_r(target))


target1, target2 = mylist.split_alt_r()

input()
for i in target1:

    print(i)

input()
for i in target2:

    print(i)

input()
for i in mylist:

    print(i)

target1.append(7)
target2.append(7)
target1.append(8)
target2.append(8)

inter.intersection_r(target1, target2)

input()
for i in inter:

    print(i)

inter.union_r(target1, target2)

input()
for i in inter:

    print(i)

inter.reverse_r()

input()
for i in inter:

    print(i)
