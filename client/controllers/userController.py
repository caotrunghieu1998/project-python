from models.userModel import UserModel

class UserController:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (UserController._instance):
            return UserController._instance
        UserController._instance = UserController()
        return UserController._instance
    
    def __init__(self):
        self._userModel = UserModel.getInstance()

    def login(self, email: str, password: str):
        return self._userModel.getUserByLogin(email, password)

