import unittest
from datetime import datetime
from freezegun import freeze_time

from gym_log.core.models.movement import Movement


class TestMovement(unittest.TestCase):

    def test_initialization_name_only(self):
        movement = Movement('Squat')
        self.assertEqual(movement.id, 'abc')
        self.assertEqual(movement.name, 'Squat')
        self.assertEqual(movement.weighted, True)
        self.assertEqual(movement.tags, [])
        self.assertEqual(movement.description, '')
        self.assertEqual(movement.notes, '')
        self.assertEqual(movement.difficulty, None)

    def test_initialization_override_default(self):
        movement = Movement('Squat', weighted=False)
        self.assertEqual(movement.weighted, False)

    def test_initialization_override_difficulty(self):
        movement = Movement('Squat', difficulty='beginner')
        self.assertEqual(movement.difficulty, 'beginner')

    def test_initialization_override_difficulty_invalid(self):
        with self.assertRaises(ValueError):
            Movement('Squat', difficulty='invalid')

    @freeze_time("2021-09-28")
    def test_created_at(self):
        movement = Movement('Squat', created_at=datetime.now())
        # self.assertEqual(movement.created_at, datetime(2021-09-28))
        self.assertEqual(movement.created_at, (2021, 9, 28))

    def test_generate_id(self):
        movement = Movement('Squat')
        self.assertEqual(movement.id, 'abc')
# TODO
# Add tests for created_at
# Add test for generate_id          