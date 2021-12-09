from datetime import datetime
import uuid


class Workout:

    FIELDS = ('id', 'name', 'description', 'notes', 'tags')

    @classmethod
    def generate_id(cls):
        return str(uuid.uuid4())

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], description=data['description'], notes=data['notes'], tags=data['tags'], id=data['id'])

    def __init__(self, name, started_at=None, finished_at=None, tags=[], notes='', description='', id=None):
        self.id = id if id else self.generate_id()
        self.name = name
        self.started_at = started_at
        self.finished_at = finished_at
        self.tags = tags
        self.notes = notes
        self.description = description
