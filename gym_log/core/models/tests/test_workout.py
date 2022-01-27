import unittest
import uuid
from mock import patch

from gym_log.core.models.workout import Workout


def mock_uuid4():
    mock_uuid = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
    return mock_uuid


@patch('uuid.uuid4', mock_uuid4)
class TestWorkout(unittest.TestCase):

    def test_initialization_name_only(self):
        workout = Workout('Push Day 1')
        self.assertEqual(workout.id, '12345678')
        self.assertEqual(workout.name, 'Push Day 1')
        self.assertEqual(workout.started_at, None)
        self.assertEqual(workout.finished_at, None)
        self.assertEqual(workout.tags, [])
        self.assertEqual(workout.notes, '')
        self.assertEqual(workout.description, '')

    def test_initialization_override_tags(self):
        workout = Workout('Push Day 1', tags=['Bench Press', 'Military Press'])
        self.assertEqual(workout.tags, ['Bench Press', 'Military Press'])

    def test_initialization_override_description(self):
        workout = Workout(
            'Push Day 1',
            description='wokout focusing on chest, shoulders and triceps')
        self.assertEqual(workout.description,
                         'wokout focusing on chest, shoulders and triceps')

    def test_initialization_override_notes(self):
        workout = Workout('Push Day 1', notes='day 1 is chest focused')
        self.assertEqual(workout.notes, 'day 1 is chest focused')

    def test_generate_id(self):
        workout = Workout('Push Day 1')
        self.assertEqual(workout.id, '12345678')
