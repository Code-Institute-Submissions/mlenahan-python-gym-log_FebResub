from datetime import datetime
import itertools 
import uuid


class Movement:

    DIFFICULTY = ('beginner', 'intermediate', 'advanced')


    # Possible ID generating functions
    # @classmethod
    # def generate_id(cls):
    #     return uuid.uuid4()

    # @classmethod
    # def generate_id(cls):
    #     id_iter = itertools.count()
    #     return id_iter

    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, name, created_at=datetime.now(), description='', notes='', difficulty=None, weighted=True, tags=[]):
        if difficulty is not None and difficulty not in self.DIFFICULTY:
            raise ValueError("%s is not a valid difficulty." % difficulty)
        self.id = self.generate_id()
        self.name = name
        self.weighted = weighted
        self.tags = tags
        self.description = description
        self.notes = notes
        self.created_at = created_at
        self.difficulty = difficulty
