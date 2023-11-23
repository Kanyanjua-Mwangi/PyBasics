'''Number of cars from KAA 001A to KZZ 999Z'''

import string

def possibleiterations (iter_legnth:int, group_size: int):
    return iter_legnth**group_size


if  __name__ == "__main__":
    alphabet = string.ascii_lowercase
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    alphabet_count = len(alphabet)
    numbers_count = len(numbers)

    prefixcombs = possibleiterations(alphabet_count, 2)
    numcombs = possibleiterations(numbers_count, 3)
    suffixcombs = possibleiterations(alphabet_count, 1)

    '''numcombs -1 to exclude 000'''

    possiblecombs = (prefixcombs*(numcombs - 1)*suffixcombs)

    print(possiblecombs)
