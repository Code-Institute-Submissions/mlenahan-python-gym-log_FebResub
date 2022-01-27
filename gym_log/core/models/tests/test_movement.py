import unittest
import uuid
from mock import patch
from freezegun import freeze_time


from gym_log.core.models.movement import Movement


def mock_uuid4():
    mock_uuid = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
    return mock_uuid


@patch('uuid.uuid4', mock_uuid4)
class TestMovement(unittest.TestCase):

    def test_initialization_name_only(self):
        movement = Movement('Squat')
        self.assertEqual(movement.id, '12345678')
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

    def test_initialization_override_tags(self):
        movement = Movement('Squat', tags=['quads', 'hamstrings'])
        self.assertEqual(movement.tags, ['quads', 'hamstrings'])

    def test_initialization_override_description(self):
        movement = Movement(
            'Squat', description='compound barbell exercise for legs')
        self.assertEqual(movement.description,
                         'compound barbell exercise for legs')

    def test_initialization_override_notes(self):
        movement = Movement('Squat', notes='good form is essential')
        self.assertEqual(movement.notes, 'good form is essential')

    @freeze_time("2020-04-26")
    def test_get_today_date(self):
        movement = Movement('Squat')
        self.assertEqual(str(movement.created_at), "2020-04-26 00:00:00")

    def test_generate_id(self):
        movement = Movement('Squat')
        self.assertEqual(movement.id, '12345678')
