import unittest

from gym_log.core.storage.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    file_storage = FileStorage()

    def __init__(self):
        super(TestFileStorage, self).__init__()
        FileStorage()
