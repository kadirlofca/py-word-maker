import word_maker_library as w

# Here, use provided functions to define rules.
# Letters in your words will be generated using these rules.
# Functions called later might override previous functions.
def generate_letter(index, word_index, word_length):

    # Example procedure.

    # Exclude letters.
    w.blacklist(('w', 'x', 'z', 'q', 'j'))

    # Select any letter from the alphabet (except the letters blacklisted above).
    w.any()

    # Use switch() for all letters.
    # switch() forces consonants to be followed by vowels and vice versa.
    w.switch()

    # Insert a string to the beginning of the word.
    # Note: the whole string counts as a single letter.
    if index == 0:
        w.insert("o")

# Make words. Pass parameters to set min/max word length and number of words to be generated.
w._generate_letter = generate_letter
generated_words = w.make_words(4, 6, 999)

for word in generated_words:
    print(word)