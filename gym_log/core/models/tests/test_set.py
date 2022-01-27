import unittest
import uuid
from mock import patch

from gym_log.core.models.set import Set


def mock_uuid4():
    mock_uuid = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
    return mock_uuid


@patch('uuid.uuid4', mock_uuid4)
class TestSet(unittest.TestCase):

    def test_initialization_default_only(self):
        set = Set('12345678', '12345678', 8)
        self.assertEqual(set.rep_count, 8)
        self.assertEqual(set.workout_id, '12345678')
        self.assertEqual(set.movement_id, '12345678')

    def test_initialization_rpe(self):
        set = Set('12345678', '12345678', 8, rpe=9)
        self.assertEqual(set.rpe, 9)

    def test_initialization_notes(self):
        set = Set('12345678', '12345678', 8, notes='hard set')
        self.assertEqual(set.notes, 'hard set')
