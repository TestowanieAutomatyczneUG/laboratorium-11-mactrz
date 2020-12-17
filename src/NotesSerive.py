from src.NotesStorage import NotesStorage

class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note):
        return self.notesStorage.add(note)

    def averageOf(self, name):
        grades = self.notesStorage.getAllNotesOfName(name)
        return sum(grades) / len(grades)

    def clear(self):
        return self.notesStorage.clear()