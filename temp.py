frets = 13
uke_tuning = {1: 'A', 2: 'E', 3: 'C', 4: 'G'}
guitar_tuning = {1: 'E', 2: 'H', 3: 'G', 4: 'D', 5: 'A', 6: 'E'}
trans = {
    'C': 'C#',
    'D': 'D#',
    'E': 'F',
    'F': 'F#',
    'G': 'G#',
    'A': 'B',
    'B': 'H',
    'C#': 'D',
    'D#': 'E',
    'F#': 'G',
    'G#': 'A',
    'H': 'C'
}

# keys = [each for each in trans.keys()]
# start_note = int(input('0 to 11'))
# start_note = keys[start_note]
#
# while True:
#     print(start_note)
#     start_note = trans[start_note]

g_string = int(input('string (1 to 6): '))
g_fret = int(input('fret (1 to 24): '))

note = guitar_tuning[g_string]
print('open note is:', note)
for i in range(g_fret):
    note = trans[note]
    print(note)

for i in range(4):
    uke_note = uke_tuning[i+1]
    for j in range(frets):
        uke_note = trans[uke_note]
        if uke_note == note:
            print(['first', 'second', 'third', 'fourth'][i] + ' string', str(j+1) + ' fret')
