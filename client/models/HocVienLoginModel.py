from models.connectDB import ConnectDB

class HocVienLogin:
    def __init__(self):
        pass

class HocVienLoginModel(ConnectDB):
    _instance = None

    @classmethod
    def getInstance(cls):
        if (HocVienLoginModel._instance):
            return HocVienLoginModel._instance
        HocVienLoginModel._instance = HocVienLoginModel()
        return HocVienLoginModel._instance

    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAHV": row[0], "HO": row[1], "TEN": row[2], "NGSINH": row[3], "GIOITINH": row[4], "NOISINH": row[5], "MALOP": row[6]}
        return data_convert
        
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def login(self, ma):
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_HOCVIEN)
        cursor.execute(query, (ma))
        data = cursor.fetchall()
        self.close()
        return self.convert(data)

    def update(self, query):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        print(res)
        self.close()