from datetime import datetime
import itertools 
import uuid


class Movement:

    DIFFICULTY = ('beginner', 'intermediate', 'advanced')

    FIELDS = ('id', 'name', 'description', 'notes', 'tags', 'weighted', 'created_at', 'difficulty')


    # Possible ID generating functions
    # @classmethod
    # def generate_id(cls):
    #     return uuid.uuid4()

    # @classmethod
    # def generate_id(cls):
    #     id_iter = itertools.count()
    #     return id_iter

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['description'], data['notes'], data['difficulty'], data['weighted'], data['tags'])
    
    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, name, description='', notes='', difficulty=None, weighted=True, tags=[], id=None):
        if difficulty is not None and difficulty not in self.DIFFICULTY:
            raise ValueError("%s is not a valid difficulty." % difficulty)
        self.id = id if id else self.generate_id()
        self.name = name
        self.weighted = weighted
        self.tags = tags
        self.description = description
        self.notes = notes
        self.created_at = datetime.now()
        self.difficulty = difficulty
