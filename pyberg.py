import numpy

def noteToPitchClass(notes):
    """Convert one or multiple musical notes to pitch classes
    
    Keyword arguments
    notes -- a string or list of strings containing musical notes
    """
    assert (isinstance(notes, str) or (isinstance(notes, list), all(isinstance(n, str) for n in notes))), "input is wrong type, accepted types: str, list of strings"
    
    if(isinstance(notes, str)):
        notes = [notes]

    assert(all(len(n) <= 2 for n in notes)), "invalid notes"

    classes = []

    for note in notes:
        note = note.lower()
        classes.append({
            'cb': 0,
            'c': 0,
            'c#': 1,
            'db': 1,
            'd': 2,
            'd#': 3,
            'eb': 3,
            'e': 4,
            'e#': 5,
            'fb': 4,
            'f': 5,
            'f#': 6,
            'gb': 6,
            'g': 7,
            'g#': 8,
            'ab': 8,
            'a': 9,
            'a#': 10,
            'bb': 10,
            'b': 11,
            'b#': 0
            }.get(note, -1))
    return classes

def pitchClassToNote(classes):
    """ Converts a pitch class or list of pitch classes to musical notes

    Keyword Arguments
    classes -- an int or list of ints representing the pitch clas
    """
    assert(isinstance(classes, int) or (isinstance(classes, list) and all(isinstance(n, int) for n in classes))), "Input is wrong type. Accepted types: int, list of ints"

    if(isinstance(classes, int)):
        classes = [classes]

    notes = []

    for pitch in classes:
        pitch = pitch % 12
        notes.append({
                0: 'C',
                1: 'C#',
                2: 'D',
                3: 'D#',
                4: 'E',
                5: 'F',
                6: 'F#',
                7: 'G',
                8: 'G#',
                9: 'A',
                10: 'A#',
                11: 'B'
            }.get(pitch, ''))
    return notes

def isRowValid(row):
    """ Returns true if the row is valid under classical serialism
    """

    assert(isinstance(row, list)), "Input is wrong type. Accepted types: list"
    if(all(isinstance(n, str) for n in row)):
        row = noteToPitchClass(row)

    if(len(set(row)) != 12):
        return False
    return True

def generateMatrix(row):
    """ Returns a list of lists containing all the possible forms of a row.
    """

    assert(isRowValid(row)), "Row is not valid, please enter a valid row"

    if(all(isinstance(n, str) for n in row)):
        row = noteToPitchClass(row)

    matrix = []
    for i in range(0,12):
        dist = row[0] - row[i]
        op = [(x + dist)%12 for x in row]
        matrix.append(op)

    return matrix

def searchRow(matrix, row):
    """Returns the form notation of the row if it is found on the matrix, else returns False"""
    assert(all(isRowValid(row) for row in matrix)), "Matrix contains invalid rows"
    assert(isRowValid(row)), "Row is invalid"
    assert(all(len(row) == 12 for row in matrix) and len(matrix) == 12), "Matrix is of wrong shape. must be (12,12)"

    try:
        i = matrix.index(row)
        form = "P"
        transposition = (matrix[i][0] - matrix[0][0])%12
        print(form + str(transposition))
        return matrix[i]
    except ValueError:
        pass

    return False
