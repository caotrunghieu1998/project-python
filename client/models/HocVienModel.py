from models.connectDB import ConnectDB

class HocVien:
    def __init__(self, MAHV, TENLOP, TRGLOP, SISO, MAGVCN):
        self._MAHV = MAHV
        self._TENLOP = TENLOP
        self._TRGLOP = TRGLOP
        self._SISO = SISO
        self._MAGVCN = MAGVCN


class HocVienModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (HocVienModel._instance):
            return HocVienModel._instance
        HocVienModel._instance = HocVienModel()
        return HocVienModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAHV": row[0], "HO": row[1], "TEN": row[2], "NGSINH": row[3], "GIOITINH": row[4], "NOISINH": row[5], "MALOP": row[6]}
        return data_convert
    
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} ORDER BY MAHV ASC".format(self.NAME_TABLE_HOCVIEN)
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def get_data_by_ma_hv(self, item):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_HOCVIEN)
        cursor.execute(query, (item["MAHV"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def is_ma_hv_exist(self, ma_hv):
        """Trả về dữ liệu mã lớp"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_HOCVIEN)
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
        if (str(item["MAHV"]) != str(item_old["MAHV"]) or
            str(item["HO"]) != str(item_old["HO"]) or
            str(item["TEN"]) != str(item_old["TEN"]) or
            str(item["NGSINH"]) != str(item_old["NGSINH"]) or
            str(item["GIOITINH"]) != str(item_old["GIOITINH"]) or
            str(item["NOISINH"]) != str(item_old["NOISINH"]) or
            str(item["MALOP"]) != str(item_old["MALOP"])):
            return False
        return True
    
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MAHV, HO, TEN, NGSINH, GIOITINH, NOISINH, MALOP)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """.format(self.NAME_TABLE_HOCVIEN)
                    
            cursor.execute(query, (item["MAHV"], item["HO"], item["TEN"], item["NGSINH"], item["GIOITINH"], item["NOISINH"], item["MALOP"]))
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
                        SET HO = %s, TEN = %s, NGSINH = %s, GIOITINH = %s, NOISINH = %s, MALOP = %s
                        WHERE MAHV = %s
                        """.format(self.NAME_TABLE_HOCVIEN)

                cursor.execute(query, (item["HO"], item["TEN"], item["NGSINH"], item["GIOITINH"], item["NOISINH"], item["MALOP"], item["MAHV"]))
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
            query = "DELETE FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_HOCVIEN)

            cursor.execute(query, (item["MAHV"]))
            db.commit()
            print(f"Xoá thành công: {item["MAHV"]}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()