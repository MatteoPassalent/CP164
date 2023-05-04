"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2023-02-19"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating 1 - 10: "))
    genres = read_genres()

    movie = Movie(title, year, director, rating, genres)

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    data = line.strip().split("|")
    data_1 = data[4].split(',')

    title = data[0]

    year = data[1]
    year = int(year)

    director = data[2]

    rating = data[3]
    rating = float(rating)

    genre = data_1

    for i in range(len(genre)):
        genre[i] = int(genre[i])

    movie = Movie(title, year, director, rating, genre)

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    movies = []

    for line in fv:
        movie = read_movie(line.strip())
        movies.append(movie)

    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    print(Movie.genres_menu())

    valid = True

    genres = []

    number = input("Enter a genre number (Enter to quit): ")

    while number != '' or genres == []:

        valid = True

        if number.isdigit():
            number = int(number)

            if number >= 0 and number <= 10:

                if genres != []:

                    for value in genres:

                        if value == number:
                            print("Error: Genre already entered")
                            valid = False

                    if valid == True:
                        genres.append(number)

                else:
                    genres.append(number)

            else:
                print("Error: input must be between 0 and 10")

        else:
            print("Error: input must be a positive integer")

        number = input("Enter a genre number (Enter to quit): ")

    genres.sort()

    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    ymovies = []

    for i in movies:

        if i.year == year:

            ymovies.append(i)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = []

    for i in movies:

        if i.rating >= rating:

            rmovies.append(i)

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []

    for movie in movies:

        for g in movie.genres:

            if g == genre:

                gmovies.append(movie)

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    count = 0

    for movie in movies:

        if len(movie.genres) == len(genres):

            count = 0

            for genre in movie.genres:

                for selec in genres:

                    if selec == genre:

                        count += 1

                        if count == len(genres):

                            gmovies.append(movie)

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for movie in movies:

        for genre in movie.genres:

            counts[genre] = counts[genre] + 1

    return counts
