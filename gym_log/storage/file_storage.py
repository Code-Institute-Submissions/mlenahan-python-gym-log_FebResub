import json
from pathlib import Path


class FileStorage:

    path = 'gym_log/core/data/'

    def save(self, entity):
        
        entity_path = self.get_entity_path(entity)

        try:
            with open(entity_path) as json_file:
                try:
                    file_dict = json.load(json_file)
                except json.decoder.JSONDecodeError:
                    file_dict = {}
                    
        except FileNotFoundError:
            file_dict = {}
        entity_dict = {}
        for field in entity.FIELDS:
            value = getattr(entity, field)
            entity_dict[field] = value
        file_dict[entity.id] = entity_dict
        
        with open(entity_path, 'w+') as json_file:
            json.dump(file_dict, json_file, indent=4, sort_keys=True, default=str)

    def retrieve(self, type, id):
        type_string = type.__name__.lower()
        path = self.get_path(type_string)
        data = self.load_file(path)
        entity_data = data.get(id)
        if not entity_data:
            return None
        return type.from_dict(entity_data)
        
    def delete(self, entity):
        entity_path = self.get_entity_path(entity)
        with open(entity_path) as json_file:
            file_dict = json.load(json_file)
        del file_dict[entity.id]
        with open(entity_path, 'w') as json_file:
            json.dump(file_dict, json_file, indent=4, sort_keys=True, default=str)

    def list(self, type):
        type_string = type.__name__.lower()
        path = self.get_path(type_string)
        data = self.load_file(path)
        entities_data = data.values()
        entity_list = []
        for entity in entities_data:
            entity_type = type.from_dict(entity)
            entity_list.append(entity_type)
        return entity_list

    def get_path(self, type):
        path = Path(__file__).parent / "data" / type  # ./data/movement.json
        return str(path) + '.json'

    def get_entity_path(self, entity):
        class_name = entity.__class__.__name__.lower()
        return self.get_path(class_name)

    def load_file(self, entity_path):
        with open(entity_path) as json_file:
            file_dict = json.load(json_file)
        return file_dict

    def convert_entity_to_dict(self, entity):
        entity_dict = {}
        for field in entity.FIELDS:
            value = getattr(entity, field)
            entity_dict[field] = value
        return entity_dict

    def add_entry_to_file_dict(self, file_dict, entry):
        file_dict[entity.id] = entity_dict
        return file_dict

    def write_file_dict(self, file_dict, entity_path):
        with open(entity_path, 'w') as json_file:
            json.dump(file_dict, json_file, indent=4, sort_keys=True, default=str)
