"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-23"
-------------------------------------------------------
"""

from functions import shift

fv = open('pelee.txt', 'r')
file = open('shift.txt', 'w')

for line in fv:
    line = line.strip().split(" ")

    for word in line:
        estring = shift(word, 1)
        file.write(estring + " ")

fv.close()
file.close()
