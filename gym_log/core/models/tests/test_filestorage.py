import unittest

from gym_log.core.storage.file_storage import FileStorage
from gym_log.core.models.movement import Movement


class TestFileStorage(unittest.TestCase):

    def test_get_entity(self):
        file_storage = FileStorage('Squat', 'abc', 'abc')
        movement = Movement('Squat')
        self.assertEqual(file_storage.get_entity_path, (file_storage.path, movement))
        
