def registration (login , password ):
    return {
        "Login" : login,
        "password" : password,
    }
login = input("Enter login that you want to use :")
password = input("Enter your password :")
user = registration(login, password)
print(user)


store = [
    {
    "label" : "kit-kat",
    "price" : "200"
    },
    {"label" : "nuts",
    "price" : "300"
    },
    {"label" : "coca-cola",
    "price" : "350"
    }
]
for index , store in enumerate(store) :
    print(index)
    print(store)

money = input("How much money do you has? : ")
if int(money) < 200 :
    print("Sorry, you don`tt have enough money")
else:
    print("What do you want to buy? ")  
