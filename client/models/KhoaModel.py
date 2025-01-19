from models.connectDB import ConnectDB

class Khoa:
    def __init__(self, MAKHOA, TENKHOA, NGTLAP, TRGKHOA):
        self._MAKHOA = MAKHOA
        self._TENKHOA = TENKHOA
        self._NGTLAP = NGTLAP
        self._TRGKHOA = TRGKHOA


class KhoaModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (KhoaModel._instance):
            return KhoaModel._instance
        KhoaModel._instance = KhoaModel()
        return KhoaModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAKHOA": row[0], "TENKHOA": row[1], "NGTLAP": row[2], "TRGKHOA": row[3]}
        return data_convert
    
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} ORDER BY MAKHOA ASC".format(self.NAME_TABLE_KHOA)
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def get_data_by_ma_hv(self, item):
        """Trả về dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAKHOA = %s".format(self.NAME_TABLE_KHOA)
        cursor.execute(query, (item["MAKHOA"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def is_ma_hv_exist(self, ma_hv):
        """Trả về dữ liệu mã lớp"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MAKHOA = %s".format(self.NAME_TABLE_KHOA)
            cursor.execute(query, (ma_hv))
            data = cursor.fetchone()
            if data != None:
                return True
            return False
        
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi kiểm tra: {e}")
        finally:
            self.close()
    
    def check_same(self, item, item_old): 
    # Chuyển đổi các giá trị về cùng một kiểu (sang chuỗi) trước khi so sánh
        if (str(item["MAKHOA"]) != str(item_old["MAKHOA"]) or
            str(item["TENKHOA"]) != str(item_old["TENKHOA"]) or
            str(item["NGTLAP"]) != str(item_old["NGTLAP"]) or
            str(item["TRGKHOA"]) != str(item_old["TRGKHOA"])):
            return False
        return True
    
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MAKHOA, TENKHOA, NGTLAP, TRGKHOA)
                    VALUES (%s, %s, %s, %s)
                    """.format(self.NAME_TABLE_KHOA)
                    
            cursor.execute(query, (item["MAKHOA"], item["TENKHOA"], item["NGTLAP"], item["TRGKHOA"]))
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
            item_old = self.get_data_by_ma_hv(item)
            is_same = self.check_same(item, item_old)
            if is_same == False:
                query = """
                        UPDATE {0}
                        SET TENKHOA = %s, NGTLAP = %s, TRGKHOA = %s
                        WHERE MAKHOA = %s
                        """.format(self.NAME_TABLE_KHOA)

                cursor.execute(query, (item["TENKHOA"], item["NGTLAP"], item["TRGKHOA"], item["MAKHOA"]))
                db.commit()
                
                return "UPDATED"
            else:
                return "NONE"
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi cập nhật dữ liệu: {e}")
            return "ERROR"
        finally:
            self.close()

    def delete_item(self, item):
        """Xoá dữ liệu CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "DELETE FROM {0} WHERE MAKHOA = %s".format(self.NAME_TABLE_KHOA)

            cursor.execute(query, (item["MAKHOA"]))
            db.commit()
            print(f"Xoá thành công: {item["MAKHOA"]}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()