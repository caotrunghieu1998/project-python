from models.connectDB import ConnectDB
import hashlib


class GiaoVien:
    def __init__(self):
        self.maGV = None
        self.hoTen = None
        self.hocVi = None
        self.hocHam = None
        self.gioiTinh = None
        self.ngSinh = None
        self.ngVL = None
        self.heSo = None
        self.mucLuong = None
        self.maKhoa = None

class GiaoVienModel(ConnectDB):
    _instance = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienModel._instance):
            return GiaoVienModel._instance
        GiaoVienModel._instance = GiaoVienModel()
        return GiaoVienModel._instance

    def __init__(self):
        super().__init__()

    def convertData(self, data):
        return [{"MAGV": row[0],
                 "HOTEN": row[1],
                 "HOCVI": row[2],
                 "HOCHAM": row[3],
                 "GIOITINH": row[4],
                 "NGSINH": row[5],
                 "NGVL": row[6],
                 "HESO": row[7],
                 "MUCLUONG": row[8],
                 "MAKHOA": row[9],
                 "PASSWORD": row[10]
                 } for row in data]

    def login(self, MAGV: str, password: str):
        db = self.connect()
        cursor = db.cursor()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        query = "SELECT * FROM {0} WHERE MAGV = %s AND PASSWORD = %s".format(self.NAME_TABLE_GIAOVIEN)
        cursor.execute(query, (MAGV, hashed_password))
        data = cursor.fetchall()
        self.close()
        return self.convertData(data)
    
    def get_data_by_id(self, MAGV: str):
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAGV = %s".format(self.NAME_TABLE_GIAOVIEN)
        cursor.execute(query, (MAGV))
        data = cursor.fetchall()
        self.close()
        return self.convertData(data)

    def update(self, query):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        print(res)
        self.close()