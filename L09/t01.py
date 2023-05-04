"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""

from functions import hash_table
from Hash_Set_array import Hash_Set
from Movie import Movie


movie1 = Movie("Dellamorte Dellamore", 1994,
               "Michele Soavi", 7.2, [3, 4, 5, 8])


movie2 = Movie("Dark City", 1998, "Alex Proyas", 7.8, [0])


hash_table(7, [movie1, movie2])

h = Hash_Set(5)
l = [99, 11, 22, 33]
for f in l:
    h.insert(f)
h.debug()
h._rehash()
h.debug()
h.remove(11)
h.debug()
