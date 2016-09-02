from torah.hebrew import HebrewLetter, HebrewFinalLetter
from torah.scribe import HebrewWrittenWord, HebrewScribeLetter, HebrewScribeLetterSize, HebrewWrittenSentence

__author__ = 'netanelrevah'

BERESHIT = HebrewWrittenWord(
    HebrewScribeLetter(HebrewLetter.BET, size=HebrewScribeLetterSize.LARGE),
    HebrewLetter.RESH,
    HebrewLetter.ALEPH,
    HebrewLetter.SHIN,
    HebrewLetter.YOD,
    HebrewLetter.TAV)

BARA = HebrewWrittenWord(
    HebrewLetter.BET,
    HebrewLetter.RESH,
    HebrewLetter.ALEPH)

ELOHIM = HebrewWrittenWord(
    HebrewLetter.ALEPH,
    HebrewLetter.LAMED,
    HebrewLetter.HE,
    HebrewLetter.YOD,
    HebrewFinalLetter.MEM)

ET = HebrewWrittenWord(
    HebrewLetter.ALEPH,
    HebrewLetter.TAV)

HASHAMIM = HebrewWrittenWord(
    HebrewLetter.HE,
    HebrewLetter.SHIN,
    HebrewLetter.MEM,
    HebrewLetter.YOD,
    HebrewFinalLetter.MEM)

VE_ET = HebrewWrittenWord(
    HebrewLetter.VAV,
    HebrewLetter.ALEPH,
    HebrewLetter.TAV)

HA_ARETZ = HebrewWrittenWord(
    HebrewLetter.HE,
    HebrewLetter.ALEPH,
    HebrewLetter.RESH,
    HebrewFinalLetter.TZADI
)

PASUK_A = HebrewWrittenSentence(BERESHIT, BARA, ELOHIM, ET, HASHAMIM, VE_ET, HA_ARETZ)
