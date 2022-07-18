from model.user import User
from model.carsuser import Cars

class Controler:

    def run(self): # метод класу люба функція в ооп
        print(
            "choose your option: \n" +
            "1. Registraton : \n" +
            "2. Login/password : \n" +
            "3. Add User Car  : \n" +
            "4. Show Users Cars : "
        )
        menu_flag = int(input("Your choose: "))

        if menu_flag == 1:
            self.Add_User()
        elif menu_flag == 2:
            self.Login_User()
        elif menu_flag == 3:
            self.ADDUsers_cars()
        elif menu_flag == 4:
            self.Showusers_cars()

    def Add_User (self):
        id = input("ID")
        email = input("Email: ")
        password = input("password : ")
        first_name = input("first name")
        last_name = input("last name")
        adress = input("your adress ")
        user = User(id, email, password, first_name, last_name, adress)
        user.save()
        print(User)
        print("Registration Success")

    def Login_User(self):
        email = input("Your Emeil: ")
        password = input("Your password: ")
        User.get_by_id(email=email, password=password)

    def ADDUsers_cars(self):
        email = input("Your Emeil :  ")
        addusercars = input("Add your car : ")
        cars = Cars(email, addusercars)
        cars.save()
        print("You add car")

    def Showusers_cars(self):
        email = input("Your email:")
        Cars.get_by_cars(email=email)











