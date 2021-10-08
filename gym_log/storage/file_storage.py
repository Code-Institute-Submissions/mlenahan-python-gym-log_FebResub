import json
from pathlib import Path

class FileStorage:

    path = 'gym_log/core/data/'

    def save(self, entity):
        # get the entity path
        entity_path = self.get_entity_path(entity)
        # check if the file exists
        with open(entity_path) as json_file:
            data = json.load(json_file)
            print(data)

        # if the file doesn't exist throw error
        # load JSON file contents as python dictionary
        # create dictionary representaion of entity
        entity_dict = {}
        for field in entity.FIELDS:
            value = getattr(entity, field)
            entity_dict[field] = value
        print(entity_dict)
            
        # add representation to file dict using id as key
        # convert file dict back to JSON
        # save JSON to file
        pass

    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__.lower()
        path = Path(__file__).parent / "data" / class_name  # ./data/movement.json
        return str(path) + '.json'
