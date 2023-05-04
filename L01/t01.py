"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""

from Movie import Movie

harry_potter = Movie('Harry Potter', 1990, 'JK rowling',
                     9.5, [5, 4, 3, 0, 10, 1])

string = harry_potter.genres_string()

print(string)
