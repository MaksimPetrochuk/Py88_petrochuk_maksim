from classes import user_class
from dataclasses import dataclass
import json


@dataclass
class DataStorage:
    path_to_storage: str = '/home/mk/pp_tms/Py_88_maksim_petrochuk/logins.json'

    @classmethod
    def get_all_logins(cls):
        while True:
            try:
                with open(cls.path_to_storage, 'r') as file:
                    logins = file.read()
                    return [] if not logins else json.loads(logins)
            except OSError:
                print('File with logins do not exists so it has been created.')
                with open(cls.path_to_storage, 'w'):
                    pass

    @staticmethod
    def turn_logins_into_class_user():
        logins = DataStorage.get_all_logins()
        result = []
        for obj in logins:
            name = obj["name"]
            password = obj["password"]
            age = obj["age"]
            key = obj["key"]
            user = user_class.User(name, password, age, key)
            result.append(user)
        return result

    @staticmethod
    def delete_changed_user(name):
        result = DataStorage.get_all_logins()
        for user in result:
            if user["name"] == name:
                result.remove(user)
        return result

    @staticmethod
    def find_user_by_name(name):
        users = DataStorage.turn_logins_into_class_user()
        for user in users:
            if user.name == name:
                return user
        return None
