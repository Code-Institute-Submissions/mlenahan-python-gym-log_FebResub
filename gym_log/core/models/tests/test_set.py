import unittest

from gym_log.core.models.set import Set


class TestSet(unittest.TestCase):

    def test_initialization_default_only(self):
        set = Set(8, workout_id='abc', movement_id='abc')
        self.assertEqual(set.rep_count, 8)
        self.assertEqual(set.workout_id, 'abc')
        self.assertEqual(set.movement_id, 'abc')

    def test_initialization_rpe(self):
        set = Set(8, workout_id='abc', movement_id='abc', rpe=9)
        self.assertEqual(set.rpe, 9)

    def test_initialization_notes(self):
        set = Set(8, workout_id='abc', movement_id='abc', notes='hard set')
        self.assertEqual(set.notes, 'hard set')
