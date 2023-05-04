"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_test

fv = open('movies.txt', 'r')

source = fv.readlines()


_ = stack_test(source)
