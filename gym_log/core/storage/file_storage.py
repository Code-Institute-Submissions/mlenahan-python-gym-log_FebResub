class FileStorage:

    path = 'gym_log/core/data'

    def save(self, entity):
        # get the class name from entity
        # combine class name and storage path + .json
        # write to file
    
    def get_entity_path(self, entity):
        # get class name of entity
        # convert to lower case
        # combine with path to get e.g. 'data/movement.json'
