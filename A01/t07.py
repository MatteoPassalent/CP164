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

from functions import matrixes_multiply

a = [[1, 2], [3, 4], [5, 6]]
# 3x2
b = [[1, 5, 3, 4], [2, 6, 5, 4]]
# 2x4
c = matrixes_multiply(a, b)

print(c)
