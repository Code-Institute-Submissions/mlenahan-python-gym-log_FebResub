from ..core.models.movement import Movement
from gym_log.storage.file_storage import FileStorage


def add(name, description='', notes='', difficulty=None, weighted=True, tags=[]):
    movement = Movement(name, description, notes, difficulty, weighted, tags)
    file_storage = FileStorage()
    file_storage.save(movement)
