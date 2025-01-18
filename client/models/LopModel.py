from models.connectDB import ConnectDB

class Lop:
    def __init__(self, MALOP, TENLOP, TRGLOP, SISO, MAGVCN):
        self._MALOP = MALOP
        self._TENLOP = TENLOP
        self._TRGLOP = TRGLOP
        self._SISO = SISO
        self._MAGVCN = MAGVCN


class LopModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (LopModel._instance):
            return LopModel._instance
        LopModel._instance = LopModel()
        return LopModel._instance
    
    def __init__(self):
        super().__init__()
    
    
    def convert(self, data):
        return [{"MALOP": row[0], "TENLOP": row[1], "TRGLOP": row[2], "SISO": row[3], "MAGVCN": row[3]} for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {self.NAME_TABLE_LOP}")
        data = cursor.fetchall()
        print(data)
        self.close(db)
        
        return [{"MALOP": row[0], "TENLOP": row[1], "TRGLOP": row[2], "SISO": row[3], "MAGVCN": row[4]} for row in data]
    
    def add_item(self, item):
        """Thêm một khoa mới."""
        print("Khoa")

    def update_item(self, index, item):
        """Cập nhật thông tin khoa."""
        print("Khoa")

    def delete_item(self, index):
        """Xóa khoa."""
        print("Khoa")