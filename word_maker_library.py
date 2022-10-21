from glob import glob
import random
import numpy

# Alphabet
_consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
_vowels = ('a', 'e', 'i', 'o', 'u')

# Private
_current = ""
_previous = ""

def _set_current(letter):
    global _current
    _current = letter

def alphabet():
    return _vowels + _consonants

def vow():
    _set_current(random.choice(_vowels))

def con():
    _set_current(random.choice(_consonants))

def any():
    _set_current(random.choice(_consonants + _vowels))

def switch():
    for v in _vowels:
        if _previous == v:
            con()
            return
    vow()

def reset():
    global _consonants
    global _vowels
    _consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    _vowels = ('a', 'e', 'i', 'o', 'u')

def blacklist(blacklist):
    global _vowels
    global _consonants
    _vowels = numpy.setdiff1d(_vowels, blacklist)
    _consonants = numpy.setdiff1d(_consonants, blacklist)

def _generate_letter(index):
    pass

def make_words(word_length, word_count):
    words = []
    word = ""

    for w in range(word_count):
        reset()

        for i in range(word_length):
            _generate_letter(i)
            global _previous
            _previous = _current
            word += _current 

        words += (word, )
        word = ""
    return words