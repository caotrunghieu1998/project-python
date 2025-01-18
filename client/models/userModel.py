from models.baseData import dataUser
from models.connectDB import ConnectDB

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

class UserModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (UserModel._instance):
            return UserModel._instance
        UserModel._instance = UserModel()
        return UserModel._instance
    
    def __init__(self):
        super().__init__()

    def convertDataTableUserToUserModel(self, data):
        return User(data[0], data[1], data[2], data[3], data[4])

    def getListUser(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {self.NAME_TABLE_USER}")
        data = cursor.fetchall()
        self.close(db)
        return [self.convertDataTableUserToUserModel(row) for row in data] 

    def getUserByLogin(self, email: str, password: str):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {self.NAME_TABLE_USER} WHERE EMAIL = %s AND PASSWORD = %s", (email, password))
        data = cursor.fetchone()
        self.close()
        if data:
            return self.convertDataTableUserToUserModel(data)
        return None
    
    # Update thông tin của user
    def update_user(self, user_id, name, email, password, role):
        db = self.connect()
        cursor = db.cursor()
        sql = f"UPDATE {self.NAME_TABLE_USER} SET NAME = %s, EMAIL = %s, PASSWORD = %s, ROLE = %s WHERE ID = %s"
        values = (name, email, password, role, user_id)
        cursor.execute(sql, values)
        db.commit()
        self.close()

    # Xóa 1 user
    def delete_user(self, user_id):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM {self.NAME_TABLE_USER} WHERE ID = %s", (user_id,))
        db.commit()
        self.close()