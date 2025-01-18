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
        return [{"MALOP": row[0], "TENLOP": row[1], "TRGLOP": row[2], "SISO": row[3], "MAGVCN": row[4]} for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = f"SELECT * FROM {self.NAME_TABLE_LOP}"
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = f"""
            INSERT INTO {self.NAME_TABLE_LOP} (MALOP, TENLOP, TRGLOP, SISO, MAGVCN)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (item["MALOP"], item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"]))
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi thêm dữ liệu: {e}")
        finally:
            self.close()

    def update_item(self, ma_lop, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = f"""
            UPDATE {self.NAME_TABLE_LOP}
            SET TENLOP = %s, TRGLOP = %s, SISO = %s, MAGVCN = %s
            WHERE MALOP = %s
            """

            cursor.execute(query, (item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"], ma_lop))
            db.commit()
            print(f"Cập nhật thành công lớp: {ma_lop}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi cập nhật dữ liệu: {e}")
        finally:
            self.close()

    def delete_item(self, ma_lop):
        """Xoá dữ liệu CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = f"""
            DELETE FROM {self.NAME_TABLE_LOP}
            WHERE MALOP = %s
            """

            cursor.execute(query, ( ma_lop))
            db.commit()
            print(f"Xoá thành công lớp: {ma_lop}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()