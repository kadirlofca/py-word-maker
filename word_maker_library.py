from glob import glob
import random
from secrets import randbits
import numpy

_consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
_vowels = ('a', 'e', 'i', 'o', 'u')

_current_letter = ""
_previous_letter = ""
_max_words = 5
_max_letters = 5
_index_letter = 0
_index_word = 0

def _set_current_letter(letter):
    global _current_letter
    _current_letter = letter

def half_words():
    return _index_word > _max_words / 2

def half_letters():
    return _index_letter > _max_letters / 2

def maybe():
    return bool(random.getrandbits(1))

def vow():
    _set_current_letter(random.choice(_vowels))

def con():
    _set_current_letter(random.choice(_consonants))

def any():
    _set_current_letter(random.choice(_consonants + _vowels))

def switch():
    for v in _vowels:
        if _previous_letter == v:
            con()
            return
    vow()

def blacklist(blacklist):
    global _vowels
    global _consonants
    _vowels = tuple(numpy.setdiff1d(_vowels, blacklist))
    _consonants = tuple(numpy.setdiff1d(_consonants, blacklist))

def reset():
    global _consonants
    global _vowels
    _consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    _vowels = ('a', 'e', 'i', 'o', 'u')

def _generate_letter(index, word_length):
    pass

def make_words(word_length_min, word_length_max, word_count):
    words = []
    word = ""

    global _index_word
    global _max_words
    _max_words = word_count
    for _index_word in range(_max_words):
        reset()

        global _index_letter
        global _max_letters
        _max_letters = random.randint(word_length_min, word_length_max)
        for _index_letter in range(_max_letters):
            _generate_letter(_index_letter, _max_letters)
            
            global _previous_letter
            _previous_letter = _current_letter
            word += _current_letter 

        words += (word, )
        word = ""
    return words