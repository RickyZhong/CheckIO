VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = "".join([x.upper() if x.isalnum() else ' ' for x in text]).split()

    total = 0
    for word in text:
        if len(word) == 1:
            continue
        odd = set(word[1::2])
        even = set(word[::2])
        total += ((odd <= set(VOWELS) and even <= set(CONSONANTS)) or
                  (odd <= set(CONSONANTS) and even <= set(VOWELS)))
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"