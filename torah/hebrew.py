from enum import Enum

__author__ = 'netanelrevah'


class BaseLetter(Enum):
    def __init__(self, order, gimmatria, unicode_value, iso8859_8_value):
        self.order = order
        self.gimmatria = gimmatria
        self.unicode_value = unicode_value
        self.iso8859_8_value = iso8859_8_value

    def __str__(self):
        return chr(self.unicode_value)


class HebrewLetter(BaseLetter):
    ALEPH = (1, 1, 0x05D0, 0xE0)
    BET = (2, 2, 0x05D1, 0xE1)
    GIMEL = (3, 3, 0x05D2, 0xE2)
    DALET = (4, 4, 0x05D3, 0xE3)
    HE = (5, 5, 0x05D4, 0xE4)
    VAV = (6, 6, 0x05D5, 0xE5)
    ZAYIN = (7, 7, 0x05D6, 0xE6)
    HET = (8, 8, 0x05D7, 0xE7)
    TET = (9, 9, 0x05D8, 0xE8)
    YOD = (10, 10, 0x05D9, 0xE9)
    KAF = (11, 20, 0x05DB, 0xEB)
    LAMED = (12, 30, 0x05DC, 0xEC)
    MEM = (13, 40, 0x05DE, 0xEE)
    NUN = (14, 50, 0x05E0, 0xF0)
    SAMEKH = (15, 60, 0x05E1, 0xF1)
    AYIN = (16, 70, 0x05E2, 0xF2)
    PE = (17, 80, 0x05E4, 0xF4)
    TZADI = (18, 90, 0x05E6, 0xF6)
    QOF = (19, 100, 0x05E7, 0xF7)
    RESH = (20, 200, 0x05E8, 0xF8)
    SHIN = (21, 300, 0x05E9, 0xF9)
    TAV = (22, 400, 0x05EA, 0xFA)


class HebrewFinalLetter(BaseLetter):
    KAF = (8, 8, 0x05DA, 0xEA)
    MEM = (13, 40, 0x05DD, 0xED)
    NUN = (14, 50, 0x05DF, 0xEF)
    PEH = (17, 80, 0x05E3, 0xF3)
    TZADI = (18, 90, 0x05E5, 0xF5)
