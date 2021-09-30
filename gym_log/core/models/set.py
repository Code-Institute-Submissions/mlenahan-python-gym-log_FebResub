from gym_log.core.models.movement import Movement
from gym_log.core.models.workout import Workout


class Set(Movement, Workout):

    RPE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @classmethod
    def generate_id(cls):
        return 'abc'

    def __init__(self, rep_count, rpe=None, notes=''):
        if rpe is not None and rpe not in self.RPE:
            raise ValueError("%s is not a valid rpe." % rpe)
        self.id = self.generate_id()
        self.rep_count = rep_count
        self.rpe = rpe
        self.notes = notes
        Movement.id = movement_id
        Workout.id = workout_id
