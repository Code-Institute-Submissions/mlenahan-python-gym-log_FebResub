import unittest

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


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)