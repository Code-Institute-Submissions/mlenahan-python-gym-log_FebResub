import uuid

class Set:

    RPE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    FIELDS = ('id', 'movement_id', 'workout_id', 'rep_count', 'rpe', 'notes')

    @classmethod
    def generate_id(cls):
        return str(uuid.uuid4())[:8]

    @classmethod
    def from_dict(cls, data):
        return cls(data['movement_id'], data['workout_id'], data['rep_count'], data['rpe'], data['notes'], data['id'])

    def __init__(self, movement_id, workout_id, rep_count, rpe=None, notes='', id=None):
        if rpe is not None and rpe not in self.RPE:
            raise ValueError("%s is not a valid rpe." % rpe)
        self.id = id if id else self.generate_id()
        self.rep_count = rep_count
        self.rpe = rpe
        self.notes = notes
        self.workout_id = workout_id
        self.movement_id = movement_id
