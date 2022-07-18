from flamework.moddels import Model
# коскруктор класу

class User(Model):
    file = "user.json"

    def __init__(self, id , email, password, first_name, last_name, adress, addusercars):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress



