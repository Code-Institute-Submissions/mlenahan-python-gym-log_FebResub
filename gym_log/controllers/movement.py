from ..core.models.movement import Movement
from gym_log.storage.file_storage import FileStorage

file_storage = FileStorage()

def add(name, description='', notes='', difficulty=None, weighted=True, tags=[]):
    movement = Movement(name, description, notes, difficulty, weighted, tags)
    file_storage.save(movement)

def update(id, name=None, description=None, notes=None, difficulty=None, weighted=None, tags=None):
    entity = retrieve(id)
    if name is not None:
        entity.name = name
    if weighted is not None:
        entity.weighted = weighted
    file_storage.save(entity)

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
    