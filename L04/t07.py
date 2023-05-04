"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""

from utilities import list_test
from Movie import Movie

fv = open('movies.txt', 'r')

source = fv.readlines()

list_test(source)
