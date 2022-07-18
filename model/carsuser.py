from flamework.moddels import Model

class Cars(Model):
    file = "cars.json"

    def __init__(self, email, addusercars, ):
        self.email = email
        self.addusercars = addusercars

