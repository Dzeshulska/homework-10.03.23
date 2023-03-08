def registration (login , password ):
    return {
        "Login" : login,
        "password" : password,
    }
login = input("Enter login that you want to use :")
password = input("Enter your password :")
user = registration(login, password)
print(user)

