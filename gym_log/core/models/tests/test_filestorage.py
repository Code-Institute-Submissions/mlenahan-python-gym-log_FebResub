import unittest

from gym_log.core.storage.file_storage import FileStorage
from gym_log.core.models.movement import Movement
from gym_log.core.models.workout import Workout
from gym_log.core.models.set import Set


class TestFileStorage(unittest.TestCase):

    def test_initialization_filestorage(self):
        file_storage = FileStorage()
        self.assertEqual(file_storage, file_storage)

    def test_initialization_movement_name_only(self):
        movement = Movement('Deadlift')
        self.assertEqual(movement.name, 'Deadlift')

    def test_initialization_workout_name_only(self):
        workout = Workout('Leg Day 2')
        self.assertEqual(workout.name, 'Leg Day 2')

    def test_initialization_set_default_only(self):
        set = Set(12, workout_id='abc', movement_id='abc')
        self.assertEqual(set.rep_count, 12)
        self.assertEqual(set.workout_id, 'abc')
        self.assertEqual(set.movement_id, 'abc')

    def test_get_entity_path_for_movement(self):
        movement = Movement('Deadlift')
        file_storage = FileStorage()
        self.assertEqual(file_storage.get_entity_path(movement), 'gym_log/core/data/movement')

    def test_get_entity_path_for_workout(self):
        workout = Workout('Leg Day 1')
        file_storage = FileStorage()
        self.assertEqual(file_storage.get_entity_path(workout), 'gym_log/core/data/workout')
    
    def test_get_entity_path_for_set(self):
        set = Set(12, workout_id='abc', movement_id='abc')
        file_storage = FileStorage()
        self.assertEqual(file_storage.get_entity_path(set), 'gym_log/core/data/set')
