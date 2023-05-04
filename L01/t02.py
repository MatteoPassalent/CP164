"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""

from Movie import Movie

Dellamorte = Movie("Dellamorte", 2000, 'Me', 9.8, [3, 4, 5, 8])

string = Dellamorte.genres_list_string()

print(string)
