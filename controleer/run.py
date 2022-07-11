from model.user import User

class Controler:

    def run(self):
        print(
            "choose your option: \n" +
            "1. Registraton : \n" +
            "2.  Login/password : \n"
        )
        menu_flag = int(input("Your choose: "))

        if menu_flag == 1:
            self.Add_User()
        elif menu_flag == 2:
            self.Login_User()

    def Add_User (self):
        id = input("ID")
        email = input("Email: ")
        password = input("password : ")
        first_name = input("first name")
        last_name = input("last name")
        adress = input("your adress ")
        user = User(id, email, password, first_name, last_name, adress )
        user.save()
        print(User)
        print("Registration Success")

    def Login_User(self):
        email = input("Your Emeil: ")
        password = input("Your password: ")
        User.get_by_id(email=email, password=password)










