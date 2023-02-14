from models import *
from pprint import pprint


ukulele = SopranoUkulele()
guitar = Guitar()

while True:
    string = int(input('Enter string (1 to 6):'))
    fret = int(input('Enter fret (1 to 24):'))

    guitar_note = guitar.get_note(string, fret)
    uke_str = ukulele.get_strings(guitar_note)
    for each in uke_str:
        print('-->', {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}[each[0]], 'string', each[1], 'fret')
    print('___')