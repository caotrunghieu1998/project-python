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
        query = "SELECT * FROM {0} ORDER BY MALOP ASC".format(self.NAME_TABLE_LOP)
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def is_ma_lop_exist(self, ma_lop):
        """Trả về dữ liệu mã lớp"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MALOP = %s".format(self.NAME_TABLE_LOP)
            cursor.execute(query, (ma_lop))
            data = cursor.fetchone()
            if data != None:
                return True
            return False
        
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi kiểm tra: {e}")
        finally:
            self.close()
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MALOP, TENLOP, TRGLOP, SISO, MAGVCN)
                    VALUES (%s, %s, %s, %s, %s)
                    """.format(self.NAME_TABLE_LOP)
                    
            cursor.execute(query, (item["MALOP"], item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"]))
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi thêm dữ liệu: {e}")
        finally:
            self.close()

    def update_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    UPDATE {0}
                    SET TENLOP = %s, TRGLOP = %s, SISO = %s, MAGVCN = %s
                    WHERE MALOP = %s
                    """.format(self.NAME_TABLE_LOP)

            cursor.execute(query, (item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"], item["MALOP"]))
            db.commit()
            print("Cập nhật thành công lớp: {}".format(item["MALOP"]))
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi cập nhật dữ liệu: {e}")
        finally:
            self.close()

    def delete_item(self, item):
        """Xoá dữ liệu CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "DELETE FROM {0} WHERE MALOP = %s".format(self.NAME_TABLE_LOP)

            cursor.execute(query, (item["MALOP"]))
            db.commit()
            print(f"Xoá thành công lớp: {item["MALOP"]}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()