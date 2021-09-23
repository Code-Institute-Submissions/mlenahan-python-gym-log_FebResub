import unittest

from core.models.movement import Movement

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
            
            
        


    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)