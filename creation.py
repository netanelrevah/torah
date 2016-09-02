# coding=utf-8
import json
import os

__author__ = 'netanelrevah'

FILE_FORMAT = 'D:\\Temp\\Torah\\0\\c{:02}{:02}.htm'

HEBREW_ALPHABET = u'אבגדהוזחטיכלמנסעפצקרשת'


def number_to_hebrew(number):
    hebrew = ''

    if number <= 0 or number >= 1000:
        raise TypeError('Can not transform zero or less to hebrew chars!')

    thousands = 400
    while number >= 100:
        if number >= thousands:
            hebrew += HEBREW_ALPHABET[18 + (thousands / 100 - 1)]
            number -= thousands
        else:
            thousands -= 100

    if number >= 10:
        if number == 15:
            hebrew += u"טו"
            number -= 15
        elif number == 16:
            hebrew += u"טז"
            number -= 16
        else:
            hebrew += HEBREW_ALPHABET[9 + (number / 10 - 1)]
    number %= 10

    if number > 0:
        hebrew += HEBREW_ALPHABET[number - 1]

    return hebrew


def generate_files():
    current_episode = 1
    for book in xrange(1, 6):
        path = FILE_FORMAT.format(book, current_episode)
        while os.path.exists(path):
            yield path, book, current_episode
            current_episode += 1
            path = FILE_FORMAT.format(book, current_episode)
        current_episode = 1

def main():
    for input_path, book, episode in generate_files():
        file_content = open(input_path, 'rb').read().decode('utf-8')

        current_part = 1
        parts = []

        start_string = '<B>' + number_to_hebrew(current_part) + '</B>'
        index = file_content.find(start_string)
        while index > 0:
            end_of_string = min(file_content.find('<A', index + len(start_string) + 1),
                            file_content.find('</P', index + len(start_string) + 1))
            parts.append(file_content[index + len(start_string):end_of_string].strip().encode('utf8'))

            current_part += 1
            start_string = '<B>' + number_to_hebrew(current_part) + '</B>'
            index = file_content.find(start_string)

        with open('D:\\Temp\\Torah\\1\\{:02}{:02}.txt'.format(book, episode), 'wb') as js:
            js.write('\r\n'.join(parts))


if __name__ == '__main__':
    main()
