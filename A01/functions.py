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


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    count = 0

    values.reverse()

    for value in values:

        count = 0

        for i in values:

            if value == i:

                count += 1

        if count > 1:

            for _ in range(count-1):

                values.remove(value)

    values.reverse()


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    file = fv.read()

    for char in file:

        if char.isupper():
            u += 1

        elif char.islower():
            l += 1

        elif char.isdigit():
            d += 1

        elif char.isspace():
            w += 1

        else:
            r += 1

    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """

    locations = []
    count = string.count(sub)
    oc = string.index(sub)
    locations.append(oc)

    for i in range(count-1):

        start = len(string[:oc]) + len(sub)
        new_oc = string[oc + len(sub):].index(sub)

        oc = start + new_oc

        locations.append(oc)

    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    leap_year = False

    if year % 4 == 0 and year % 100 != 0:
        leap_year = True

    elif year % 100 == 0 and year % 400 == 0:
        leap_year = True

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True

    if not name[0].isalpha() and name[0] != '_':
        valid = False

    for i in name:

        if not i.isalpha() and not i.isdigit() and i != '_':
            valid = False

    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    b = []

    for i in range(len(a[0])):

        temp = []

        for j in range(len(a)):

            temp.append(a[j][i])

        b.append(temp)

    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """

    row = len(a)
    col = len(b[0])
    c = []

    for i in range(row):
        new = []

        for j in range(col):
            new.append(0)

        c.append(new)

    for i in range(row):

        for j in range(col):

            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    pl = ""

    upper = False

    if word[0].isupper():
        upper = True

    if word[0] in vowels:
        pl += word + "way"

    else:
        vowels_AND_Y = ["a", "e", "i", "o", "u",
                        "A", "E", "I", "O", "U", "y", "Y"]
        c = []

        if word[0] == "y"or word[0] == 'Y':
            word = word[1:] + word[0].lower()

        w = 0

        while word[w] not in vowels_AND_Y:
            c.append(word[w].lower())
            w += 1

        pl = word[len(c):]

        for i in c:
            pl += i

        pl += "ay"

    if upper:
        pl = pl[0].upper()+pl[1:]

    return pl


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = string.upper()

    count = 0
    pos = 0
    new_letter = None

    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for char in estring:

        if char.isalpha():

            pos = alpha.index(char)

            new_letter = alpha[pos + n]

            estring = estring[:count] + new_letter + estring[count + 1:]

            count += 1

    return estring
