import unittest

from gym_log.storage.file_storage import FileStorage
from gym_log.core.models.movement import Movement
from gym_log.core.models.workout import Workout
from gym_log.core.models.set import Set


class TestFileStorage(unittest.TestCase):

    def test_initialization_file_storage(self):
        file_storage = FileStorage()
        self.assertTrue(isinstance(file_storage, FileStorage))

    def test_get_entity_path_for_movement(self):
        movement = Movement('Deadlift')
        file_storage = FileStorage()
        path = file_storage.get_entity_path(movement)
        self.assertTrue(path.endswith('gym_log/storage/data/movement.json'))

    def test_get_entity_path_for_workout(self):
        workout = Workout('Leg Day 1')
        file_storage = FileStorage()
        path = file_storage.get_entity_path(workout)
        self.assertTrue(path.endswith('gym_log/storage/data/workout.json'))
    
    def test_get_entity_path_for_set(self):
        set = Set(12, workout_id='abc', movement_id='abc')
        file_storage = FileStorage()
        path = file_storage.get_entity_path(set)
        self.assertTrue(path.endswith('gym_log/storage/data/set.json'))

    def test_save_movement(self):
        movement = Movement('Deadlift')
        file_storage = FileStorage()
        file_storage.save(movement)
        
