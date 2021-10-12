import json
from pathlib import Path


class FileStorage:

    path = 'gym_log/core/data/'

    def save(self, entity):
        # get the entity path
        entity_path = self.get_entity_path(entity)
        # check if the file exists
        with open(entity_path) as json_file:
            file_dict = json.load(json_file)

        # if the file doesn't exist throw error
        # load JSON file contents as python dictionary
        # create dictionary representaion of entity
        entity_dict = {}
        for field in entity.FIELDS:
            value = getattr(entity, field)
            entity_dict[field] = value
            
        # add entity_dict to file dict using id as key
        file_dict[entity.id] = entity_dict
        # convert file dict back to JSON
        with open(entity_path, 'w') as json_file:
            # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
            json.dump(file_dict, json_file, indent=4, sort_keys=True, default=str)
        # save JSON to file
        pass

    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__.lower()
        path = Path(__file__).parent / "data" / class_name  # ./data/movement.json
        return str(path) + '.json'

    def load_file(self, entity_path):
        # use to replace lines 12, 13
        # returns file_dict
        with open(entity_path) as json_file:
            file_dict = json.load(json_file)
        return file_dict

    def convert_entity_to_dict(self, entity):
        # use to replace 18, 21
        # returns entity_dict
        entity_dict = {}
        for field in entity.FIELDS:
            value = getattr(entity, field)
            entity_dict[field] = value
        return entity_dict

    def add_entry_to_file_dict(self, file_dict, entry):
        # use to replace line 24
        # returns file_dict
        # entry is entity_dict
        file_dict[entity.id] = entity_dict
        return file_dict

    def write_file_dict(self, file_dict, entity_path):
        # use to replace line 23 to 28
        with open(entity_path, 'w') as json_file:
            # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
            json.dump(file_dict, json_file, indent=4, sort_keys=True, default=str)
        

    def delete(self, entity):
        pass
