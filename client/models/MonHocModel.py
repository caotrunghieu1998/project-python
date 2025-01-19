from models.connectDB import ConnectDB

class MonHoc:
    def __init__(self, MAMH, TENMH, TCLT, TCTH, MAKHOA):
        self._MAMH = MAMH
        self._TENMH = TENMH
        self._TCLT = TCLT
        self._TCTH = TCTH
        self._MAKHOA = MAKHOA


class MonHocModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (MonHocModel._instance):
            return MonHocModel._instance
        MonHocModel._instance = MonHocModel()
        return MonHocModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAMH": row[0], "TENMH": row[1], "TCLT": row[2], "TCTH": row[3], "MAKHOA": row[4]}
        return data_convert
    
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} ORDER BY MAMH ASC".format(self.NAME_TABLE_MONHOC)
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def get_data_by_ma(self, item):
        """Trả về dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAMH = %s".format(self.NAME_TABLE_MONHOC)
        cursor.execute(query, (item["MAMH"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def is_ma_exist(self, ma_mh):
        """Trả về dữ liệu True|False"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MAMH = %s".format(self.NAME_TABLE_MONHOC)
            cursor.execute(query, (ma_mh))
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
        if (str(item["MAMH"]) != str(item_old["MAMH"]) or
            str(item["TENMH"]) != str(item_old["TENMH"]) or
            str(item["TCLT"]) != str(item_old["TCLT"]) or
            str(item["TCTH"]) != str(item_old["TCTH"]) or
            str(item["MAKHOA"]) != str(item_old["MAKHOA"])):
            return False
        return True
    
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MAMH, TENMH, TCLT, TCTH, MAKHOA)
                    VALUES (%s, %s, %s, %s, %s)
                    """.format(self.NAME_TABLE_MONHOC)
                    
            cursor.execute(query, (item["MAMH"], item["TENMH"], item["TCLT"], item["TCTH"], item["MAKHOA"]))
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
            item_old = self.get_data_by_ma(item)
            is_same = self.check_same(item, item_old)
            if is_same == False:
                query = """
                        UPDATE {0}
                        SET TENMH = %s, TCLT = %s, TCTH = %s, MAKHOA = %s
                        WHERE MAMH = %s
                        """.format(self.NAME_TABLE_MONHOC)

                cursor.execute(query, (item["TENMH"], item["TCLT"], item["TCTH"], item["MAKHOA"], item["MAMH"]))
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
            query = """
                    DELETE FROM {0}
                    WHERE MAMH = %s
                    """.format(self.NAME_TABLE_MONHOC)

            cursor.execute(query, (item["MAMH"]))
            db.commit()
            print(f"Xoá thành công: Mã môn học {0}".format(item["MAMH"]))
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()