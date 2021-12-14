from ..core.models.workout import Workout
from gym_log.storage.file_storage import FileStorage

file_storage = FileStorage()

def create(name, description='', notes='', tags=[]):
    workout = Workout(name, description, notes, tags)
    file_storage.save(workout)

def delete(id):
    entity = retrieve(id)
    file_storage.delete(entity)

def retrieve(id):
    result = file_storage.retrieve(Workout, id)
    if not result:
        raise ValueError('No workout with given ID')
    return result

def list():
    results = file_storage.list(Workout)
    return results
    