from datetime import datetime

class Workout:

    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, name, started_at=None, finished_at=None, tags=[], notes=''):
        self.id = self.generate_id()
        self.name = name
        self.started_at = datetime.time()
        self.finished_at = datetime.time()
        self.tags = tags
        self.notes = notes
        
