from usuarios import registerUser
from record import Record


if __name__ == '__main__':
    registerUser.RegisterUser().save()
    user = Record().getUser("Clebsonpy")
    print(user.getName())
    

