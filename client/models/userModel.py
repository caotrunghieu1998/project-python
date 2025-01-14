from models.baseData import dataUser

class User:
    def __init__(self, ID: int, NAME: str, EMAIL: str, PASSWORD: str, ROLE: str):
        self._ID = ID
        self._NAME = NAME
        self._EMAIL = EMAIL
        self._PASSWORD = PASSWORD
        self._ROLE = ROLE

    # GETTER ID  
    @property
    def ID(self):
        return self._ID
    
    # GETTER, SETTER NAME  
    @property
    def NAME(self):
        return self._NAME
    
    @NAME.setter
    def NAME(self, NAME):
        self._NAME = NAME

    # GETTER, SETTER EMAIL 
    @property
    def EMAIL(self):
        return self._EMAIL
    
    @EMAIL.setter
    def EMAIL(self, EMAIL):
        self._EMAIL = EMAIL
    
    # GETTER, SETTER PASSWORD  
    @property
    def PASSWORD(self):
        return self._PASSWORD
    
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD):
        self._PASSWORD = PASSWORD

    # GETTER, SETTER ROLE  
    @property
    def ROLE(self):
        return self._ROLE
    
    @ROLE.setter
    def ROLE(self, ROLE):
        self._ROLE = ROLE

class UserModel:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (UserModel._instance):
            return UserModel._instance
        UserModel._instance = UserModel()
        return UserModel._instance
    
    def __init__(self):
        pass

    def login(self, email: str, password: str):
        for user in dataUser:
            if user["EMAIL"] == email and user["PASSWORD"] == password:
                return User(user["ID"], user["NAME"], user["EMAIL"], user["PASSWORD"], user["ROLE"])
        return None