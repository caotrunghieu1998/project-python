import pymysql

class ConnectDB:
    # Field Connect
    _host="localhost"
    _user="root"
    _password=""
    _database="python_qlgv"
    
    # Field Table name
    NAME_TABLE_USER = "user"

    def __init__(self):
        self.connection = None
    
    # Kết nối đến cơ sở dữ liệu
    def connect(self):
        if self.connection is None or not self.connection.open:
            return pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
        return self.connection

    # Đóng kết nối
    def close(self):
        if self.connection:
            self.connection.close()