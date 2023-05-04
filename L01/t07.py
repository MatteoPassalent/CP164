"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-19"
-------------------------------------------------------
"""

from Movie import Movie
from Movie_utilities import read_movie
from Movie_utilities import read_movies

fv = open('movies.txt', 'r')
movies = read_movies(fv)

print(movies)
