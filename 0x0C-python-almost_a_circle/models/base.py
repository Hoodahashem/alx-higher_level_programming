#!/usr/bin/python3
import json
"""i'm just working on myself and hoping from GOD that gives me
what i'm looking for."""


class Base:
    """stay hard and let the GOD DO HIS JOB AND JRUST HIM"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the class"""
        if id is None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                listob = []
                for obj in list_objs:
                    listob.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(listob))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string function"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns a new instance of the given JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        if dictionary or dictionary != {}:
            if cls.__name__ == 'Rectangle':
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """load_from_file function"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
