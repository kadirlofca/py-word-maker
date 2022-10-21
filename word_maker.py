import word_maker_library as w

# Here, use provided functions to define rules.
# Letters in your words will be generated using these rules.
# Priority is bottom to top. Meaning functions called later can override previous functions.
def generate_letter(index):
    w.blacklist(('w', 'x', 'z', 'q', 'j'))
    w.switch()

    # Force initial letter to be a consonant.
    if index == 0:
        w.con()

# Make words. Pass parameters to set word length and number of words to be generated.
w._generate_letter = generate_letter
generated_words = w.make_words(5, 50)

for word in generated_words:
    print(word)