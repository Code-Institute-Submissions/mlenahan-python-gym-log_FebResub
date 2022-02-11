from gym_log.storage.file_storage import FileStorage
from ..core.models.set import Set
from . import movement, workout

file_storage = FileStorage()


def create(movement_id, workout_id, rep_count, rpe=None, notes=''):
    movement.retrieve(movement_id)
    workout.retrieve(workout_id)
    set = Set(movement_id, workout_id, rep_count, rpe, notes)
    file_storage.save(set)


def delete(id):
    entity = retrieve(id)
    file_storage.delete(entity)


def retrieve(id):
    result = file_storage.retrieve(Set, id)
    if not result:
        raise ValueError('No set with given ID')
    return result


def list():
    results = file_storage.list(Set)
    return results
