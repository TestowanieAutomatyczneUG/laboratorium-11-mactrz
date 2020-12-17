class Note:
    def __init__(self, name, note):
        if name is None or type(name) != str or type(note) != float:
            raise TypeError('Wrong value types')

        if len(name) == 0 or note > 6 or note < 2:
            raise ValueError('Wrong values')

        self.name = name
        self.note = note

    def getName(self):
        return self.name

    def getNote(self):
        return self.note