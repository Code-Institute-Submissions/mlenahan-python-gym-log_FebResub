from datetime import datetime


class Movement:

    DIFFICULTY = ('beginner', 'intermediate', 'advanced')

    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, name, description='', notes='', difficulty=None, weighted=True, tags=[]):
        if difficulty is not None and difficulty not in self.DIFFICULTY:
            raise ValueError("%s is not a valid difficulty." % difficulty)
        self.id = self.generate_id()
        self.name = name
        self.weighted = weighted
        self.tags = tags
        self.description = description
        self.notes = notes
        self.created_at = datetime.now()
        self.difficulty = difficulty
