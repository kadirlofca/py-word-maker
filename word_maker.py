import word_maker_library as w

# Here, use provided functions to define rules.
# Letters in your words will be generated using these rules.
# Functions called later might override previous functions.
def generate_letter(index, word_length):

    # Example procedure.

    # Exclude letters.
    w.blacklist(('w', 'x', 'z', 'q', 'j'))

    # Select any letter from the alphabet (except the letters blacklisted above).
    w.any()

    # In half of the length-5 words generated, use switch() for all letters except the third.
    # The switch() rule makes sure each consonant is followed by a vowel and vice versa. 
    if word_length == 5 and index != 4 and w.half_words():
        w.switch()

    # Use switch() for all letters in 4-length words.
    if word_length == 4:
        w.switch()

    # Force initial letter to be a consonant.
    if index == 0:
        w.con()

# Make words. Pass parameters to set min/max word length and number of words to be generated.
w._generate_letter = generate_letter
generated_words = w.make_words(4, 5, 12)

for word in generated_words:
    print(word)