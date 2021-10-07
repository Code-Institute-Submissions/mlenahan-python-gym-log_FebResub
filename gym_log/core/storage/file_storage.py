class FileStorage:

    path = 'gym_log/core/data/'

    def save(self, entity):
        pass

    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__
        return self.path + class_name
