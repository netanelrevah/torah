from enum import Enum

__author__ = 'netanelrevah'


class HebrewScribeLetterSize(Enum):
    TINY = 'tiny'
    REGULAR = 'regular'
    LARGE = 'large'


class HebrewScribeLetter(object):
    def __init__(self, letter, size=HebrewScribeLetterSize.REGULAR):
        self.letter = letter
        self.size = size

    def __str__(self):
        return str(self.letter)


class HebrewWrittenWord(object):
    def __init__(self, *letters):
        self.letters = self.to_scribe_letters(letters)

    @staticmethod
    def to_scribe_letters(letters):
        scribe_letters = []
        for letter in letters:
            scribe_letter = letter
            if not isinstance(scribe_letter, HebrewScribeLetter):
                scribe_letter = HebrewScribeLetter(letter)
            scribe_letters.append(scribe_letter)
        return scribe_letters

    def __str__(self):
        return ''.join(str(letter) for letter in self.letters)


class HebrewWrittenSentence(object):
    def __init__(self, *words):
        self.words = words

    def __str__(self):
        return ' '.join(str(word) for word in self.words)
