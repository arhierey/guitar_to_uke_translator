from models import *


ukulele = SopranoUkulele()
guitar = Guitar()
tune_D = input("Tune to drop D? (type 'y' for 'yes')")
if tune_D:
    guitar.tuning[6] = 'D'

print(guitar, ukulele)
while True:
    string = int(input('Enter string (1 to 6):').strip())
    fret = int(input('Enter fret (0 to 24):').strip())

    guitar_note = guitar.get_note(string, fret)
    uke_str = ukulele.get_strings(guitar_note)
    for each in uke_str:
        print('-->', {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}[each[0]], 'string', each[1], 'fret')
    print('___')