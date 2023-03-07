class StringInstrument:
    def __init__(self):
        self.str_number = None
        self.fret_number = None
        self.tuning = None
        self.trans = {
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

    def get_note(self, string, fret):
        note = self.tuning[string]
        for i in range(fret):
            note = self.trans[note]
        print('Your note is:', note)
        return note

    def get_strings(self, note):
        res = []
        for i in range(self.str_number):
            instr_note = self.tuning[i + 1]
            if instr_note == note:
                res.append([i + 1, 0])
            for j in range(self.fret_number):
                instr_note = self.trans[instr_note]
                if instr_note == note:
                    res.append([i+1, j+1])
        return res


class SopranoUkulele(StringInstrument):
    def __init__(self):
        super().__init__()
        self.fret_number = 13
        self.str_number = 4
        self.tuning = {1: 'A', 2: 'E', 3: 'C', 4: 'G'}

    def __str__(self):
        tuning = ''.join(self.tuning[each] for each in self.tuning)
        return 'soprano ukulele with tuning:' + tuning[::-1]


class Guitar(StringInstrument):
    def __init__(self):
        super().__init__()
        self.fret_number = 24
        self.str_number = 6
        self.tuning = {1: 'E', 2: 'H', 3: 'G', 4: 'D', 5: 'A', 6: 'E'}

    def __str__(self):
        tuning = ''.join(self.tuning[each] for each in self.tuning)
        return 'guitar with tuning:' + tuning[::-1]
