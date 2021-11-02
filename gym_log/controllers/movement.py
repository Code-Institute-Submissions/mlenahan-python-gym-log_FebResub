from ..core.models.movement import Movement
from gym_log.storage.file_storage import FileStorage
from run import args


def add():
    movement = Movement(args)
    file_storage = FileStorage()
    file_storage.save(movement)
