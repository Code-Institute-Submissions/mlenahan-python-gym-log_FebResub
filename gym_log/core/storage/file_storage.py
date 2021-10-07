from gym_log.core.models.movement import Movement
from gym_log.core.models.workout import Workout
from gym_log.core.models.set import Set


class FileStorage(Set, Movement, Workout):

    path = 'gym_log/core/data/'
        
    def save(self, entity):
        pass
    
    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__
        return self.path + class_name
