import pymysql

class ConnectDB:
    # Field Connect
    _host="sql5.freemysqlhosting.net"
    _user="sql5758315"
    _password="KD6vKqAYH5"
    _database="sql5758315"
    _port=3306
    
    # Field Table name
    NAME_TABLE_USER = "user"
    NAME_TABLE_LOP = "lop"
    NAME_TABLE_GIAOVIEN = "giaovien"
    NAME_TABLE_HOCVIEN = "hocvien"
    NAME_TABLE_KHOA = "khoa"

    def __init__(self):
        self.connection = None
    
    # Kết nối đến cơ sở dữ liệu
    def connect(self):
        if self.connection is None or not self.connection.open:
            return pymysql.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database,
                port=self._port
            )
        return self.connection

    # Đóng kết nối
    def close(self):
        if self.connection:
            self.connection.close()