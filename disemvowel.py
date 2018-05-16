# disemvowel function removes vowels from words: both uppercase and lowercase from a given word
def disemvowel(word):
    # vowels tuple which is an immutable list
    vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
    for letter in word:
        if letter in vowels:
            try:
                word = word.replace(letter, "")
            except ValueError:
                pass
    return word
disemvowel("Ouijwwae")
