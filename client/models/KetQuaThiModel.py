from models.connectDB import ConnectDB

class KetQuaThi:
    def __init__(self, MAHV, TENLOP, TRGLOP, SISO, MAGVCN):
        self._MAHV = MAHV
        self._TENLOP = TENLOP
        self._TRGLOP = TRGLOP
        self._SISO = SISO
        self._MAGVCN = MAGVCN


class KetQuaThiModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (KetQuaThiModel._instance):
            return KetQuaThiModel._instance
        KetQuaThiModel._instance = KetQuaThiModel()
        return KetQuaThiModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MAHV": row[0], "MAMH": row[1], "LANTHI": row[2], "NGTHI": row[3], "DIEM": row[4], "KQUA": row[5]}
        return data_convert
        
    def convert(self, data):
        return [self.convert_obj(row) for row in data]

    def get_data_by_ma_gv(self, magv):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = """
                SELECT C.MAHV, C.MAMH, C.LANTHI, C.NGTHI, C.DIEM, C.KQUA FROM {0} A
                INNER JOIN {1} B
                ON A.MAGV = B.MAGV
                INNER JOIN {2} C
                ON B.MAMH = C.MAMH
                WHERE A.MAGV = %s
                """.format(self.NAME_TABLE_GIAOVIEN, self.NAME_TABLE_GIANGDAY, self.NAME_TABLE_KETQUATHI)
        cursor.execute(query, (magv))
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)

    def get_data_by_ma_hv(self, ma_hv):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_KETQUATHI)
        cursor.execute(query, (ma_hv))
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def is_ma_hv_exist(self, ma_hv):
        """Trả về dữ liệu mã lớp"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_KETQUATHI)
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
            str(item["MAMH"]) != str(item_old["MAMH"]) or
            str(item["LANTHI"]) != str(item_old["LANTHI"]) or
            str(item["NGTHI"]) != str(item_old["NGTHI"]) or
            str(item["DIEM"]) != str(item_old["DIEM"]) or
            str(item["KQUA"]) != str(item_old["KQUA"])):
            return False
        return True
    
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MAHV, MAMH, LANTHI, NGTHI, DIEM, KQUA)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """.format(self.NAME_TABLE_KETQUATHI)
                    
            cursor.execute(query, (item["MAHV"], item["MAMH"], item["LANTHI"], item["NGTHI"], item["DIEM"], item["KQUA"]))
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
                        SET MAMH = %s, LANTHI = %s, NGTHI = %s, DIEM = %s, KQUA = %s
                        WHERE MAHV = %s
                        """.format(self.NAME_TABLE_KETQUATHI)

                cursor.execute(query, (item["MAMH"], item["LANTHI"], item["NGTHI"], item["DIEM"], item["KQUA"],item["MAHV"]))
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
            query = "DELETE FROM {0} WHERE MAHV = %s".format(self.NAME_TABLE_KETQUATHI)

            cursor.execute(query, (item["MAHV"]))
            db.commit()
            print(f"Xoá thành công: {item["MAHV"]}")
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()