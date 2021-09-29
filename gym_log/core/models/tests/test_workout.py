import unittest
from datetime import datetime, time
from freezegun import freeze_time

from gym_log.core.models.workout import Workout


class TestWorkout(unittest.TestCase):

    def test_initialization_name_only(self):
        workout = Workout('Push Day 1')
        self.assertEqual(workout.id, 'abc')
        self.assertEqual(workout.name, 'Push Day 1')
        self.assertEqual(workout.started_at, None)
        self.assertEqual(workout.finished_at, None)
        self.assertEqual(workout.tags, [])
        self.assertEqual(workout.notes, '')

    def test_initialization_override_started_at(self):
        workout = Workout('Push Day 1', started_at=datetime.time(13, 30, 45, 0))
        self.assertEqual(workout.started_at, (13, 30, 45, 0))

    # def test_initialization_override_difficulty(self):
    #     movement = Movement('Squat', difficulty='beginner')
    #     self.assertEqual(movement.difficulty, 'beginner')

    # def test_initialization_override_difficulty_invalid(self):
    #     with self.assertRaises(ValueError):
    #         Movement('Squat', difficulty='invalid')

    # @freeze_time("2021-09-29")
    # def test_created_at(self):
    #     movement = Movement('Squat', created_at=datetime.now())
    #     self.assertEqual(movement.created_at, (2021, 9, 29, 0, 0))

    # def test_generate_id(self):
    #     workout = Movement('Push Day 1')
    #     self.assertEqual(movement.id, 'abc')
# TODO
# Add tests for created_at
# Add test for generate_id          