from datetime import datetime


class Workout:

    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, name, started_at=None, finished_at=None, tags=[], notes='', description=''):
        self.workout_id = self.generate_id()
        self.name = name
        self.started_at = started_at
        self.finished_at = finished_at
        self.tags = tags
        self.notes = notes
        self.description = description
