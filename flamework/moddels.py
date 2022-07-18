from abc import ABC, abstractmethod
import json


# батьківський клас

class Model(ABC):
    file = 'default.json'

    def save(self):
        get_dict = self._generate_dict()
        data = self.get_file_data(self.file)
        data.append(get_dict)
        self.save_to_file(data)

    def _generate_dict(self):
        get_dict = self.__dict__
        return get_dict

    @classmethod
    def get_by_id(cls, email, password=None):
        data = cls.get_file_data(cls.file)
        use = []
        for user in data:
            if user["email"] == email and user["password"] == password:
                use.append(user)
        if use:
            print(use)
        else:
            raise Exception(str("User not found"))

    @classmethod
    def get_by_cars(cls, email,):
        data_cars = cls.get_file_data(cls.file)
        data_user = cls.get_file_data(file_name="user.json")
        for user in data_user:
            if user['email'] == email:
                use1 = []
                for user_car in data_cars:
                    if user_car["email"] == email:
                        use1.append(user_car)
                if use1:
                    print(use1)
                else:
                    raise Exception(str("Users car not found"))
            else:
                raise Exception(str("User not found"))


    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
