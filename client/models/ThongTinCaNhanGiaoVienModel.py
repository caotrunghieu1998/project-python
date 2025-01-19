from models.connectDB import ConnectDB

class ThongTinCaNhanGiaoVien:
    def __init__(self, MAGV, TENLOP, TRGLOP, SISO, MAGVCN):
        self._MAGV = MAGV
        self._TENLOP = TENLOP
        self._TRGLOP = TRGLOP
        self._SISO = SISO
        self._MAGVCN = MAGVCN


class ThongTinCaNhanGiaoVienModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanGiaoVienModel._instance):
            return ThongTinCaNhanGiaoVienModel._instance
        ThongTinCaNhanGiaoVienModel._instance = ThongTinCaNhanGiaoVienModel()
        return ThongTinCaNhanGiaoVienModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAGV": row[0],
                        "HOTEN": row[1],
                        "HOCVI": row[2],
                        "HOCHAM": row[3],
                        "GIOITINH": row[4],
                        "NGSINH": row[5],
                        "NGVL": row[6],
                        "HESO": row[7],
                        "MUCLUONG": row[8],
                        "MAKHOA": row[9]}
        return data_convert
        
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def login(self, ma):
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAGV = %s".format(self.NAME_TABLE_GIAOVIEN)
        cursor.execute(query, (ma))
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def load_item(self, item):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAGV = %s".format(self.NAME_TABLE_GIAOVIEN)
        cursor.execute(query, (item[0]["MAGV"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def check_same(self, item, item_old): 
    # Chuyển đổi các giá trị về cùng một kiểu (sang chuỗi) trước khi so sánh
        if (str(item["MAGV"]) != str(item_old["MAGV"]) or
            str(item["HOTEN"]) != str(item_old["HOTEN"]) or
            str(item["HOCVI"]) != str(item_old["HOCVI"]) or
            str(item["HOCHAM"]) != str(item_old["HOCHAM"]) or
            str(item["GIOITINH"]) != str(item_old["GIOITINH"]) or
            str(item["NGSINH"]) != str(item_old["NGSINH"]) or
            str(item["NGVL"]) != str(item_old["NGVL"]) or
            str(item["HESO"]) != str(item_old["HESO"]) or
            str(item["MUCLUONG"]) != str(item_old["MUCLUONG"]) or
            str(item["MAKHOA"]) != str(item_old["MAKHOA"])):
            return False
        return True
    
    def update_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        try:
            query = """
                    UPDATE {0}
                    SET HOTEN = %s, HOCVI = %s, HOCHAM = %s, GIOITINH = %s, NGSINH = %s, NGVL = %s, HESO = %s, MUCLUONG = %s, MAKHOA = %s
                    WHERE MAGV = %s
                    """.format(self.NAME_TABLE_GIAOVIEN)

            cursor.execute(query, (item["HOTEN"], item["HOCVI"], item["HOCHAM"], item["GIOITINH"], item["NGSINH"], item["NGVL"], item["HESO"], item["MUCLUONG"], item["MAKHOA"], item["MAGV"]))
            db.commit()
            
            return "UPDATED"
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi cập nhật dữ liệu: {e}")
            return "ERROR"
        finally:
            self.close()