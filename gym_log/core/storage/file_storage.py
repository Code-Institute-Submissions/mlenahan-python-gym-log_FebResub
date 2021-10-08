class FileStorage:

    path = 'gym_log/core/data/'

    def __init__(self):
        pass

    def save(self, entity):
        pass

    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__.lower()
        return self.path + class_name
