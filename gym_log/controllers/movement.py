from ..core.models.movement import Movement
from gym_log.storage.file_storage import FileStorage

file_storage = FileStorage()


def create(
        name,
        description='',
        notes='',
        difficulty=None,
        weighted=True,
        tags=[]):
    movement = Movement(name, description, notes, difficulty, weighted, tags)
    file_storage.save(movement)


def delete(id):
    entity = retrieve(id)
    file_storage.delete(entity)


def retrieve(id):
    result = file_storage.retrieve(Movement, id)
    if not result:
        raise ValueError('No movement with given ID')
    return result


def list():
    results = file_storage.list(Movement)
    return results
