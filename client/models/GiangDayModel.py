from models.connectDB import ConnectDB

class GiangDay:
    def __init__(self, MALOP, MAMH, MAGV, HOCKY, NAM, TUNGAY, DENNGAY):
        self._MALOP = MALOP
        self._MAMH = MAMH
        self._MAGV = MAGV
        self._HOCKY = HOCKY
        self._NAM = NAM
        self._TUNGAY = TUNGAY
        self._DENNGAY = DENNGAY


class GiangDayModel(ConnectDB):
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (GiangDayModel._instance):
            return GiangDayModel._instance
        GiangDayModel._instance = GiangDayModel()
        return GiangDayModel._instance
    
    def __init__(self):
        super().__init__()
    
    def convert_obj(self, row):
        data_convert = {"MALOP": row[0], "MAMH": row[1], "MAGV": row[2], "HOCKY": row[3], "NAM": row[4], "TUNGAY": row[5], "DENNGAY": row[6]}
        return data_convert
    
    def convert(self, data):
        return [self.convert_obj(row) for row in data]
    
    def get_list_data(self):
        """Trả về danh sách dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} ORDER BY MALOP ASC".format(self.NAME_TABLE_GIANGDAY)
        cursor.execute(query)
        data = cursor.fetchall()
        self.close()
        
        return self.convert(data)
    
    def get_data_by_ma(self, item):
        """Trả về dữ liệu."""
        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM {0} WHERE MALOP = %s".format(self.NAME_TABLE_GIANGDAY)
        cursor.execute(query, (item["MALOP"]))
        data = cursor.fetchone()
        self.close()
        
        return self.convert_obj(data)
    
    def is_ma_exist(self, ma_lop, ma_mh, ma_gv):
        """Trả về dữ liệu mã lớp"""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = "SELECT * FROM {0} WHERE MALOP = %s, MAMH = %s, MAGV = %s".format(self.NAME_TABLE_GIANGDAY)
            cursor.execute(query, (ma_lop, ma_mh, ma_gv))
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
        if (str(item["MALOP"]) != str(item_old["MALOP"]) or
            str(item["MAMH"]) != str(item_old["MAMH"]) or
            str(item["MAGV"]) != str(item_old["MAGV"]) or
            str(item["HOCKY"]) != str(item_old["HOCKY"]) or
            str(item["NAM"]) != str(item_old["NAM"]) or
            str(item["TUNGAY"]) != str(item_old["TUNGAY"]) or
            str(item["DENNGAY"]) != str(item_old["DENNGAY"])):
            return False
        return True
    
    
    def add_item(self, item):
        """Thêm dữ liệu mới vào CSDL."""
        db = self.connect()
        cursor = db.cursor()
        
        try:
            query = """
                    INSERT INTO {0} (MALOP, MAMH, MAGV, HOCKY, NAM, TUNGAY, DENNGAY)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """.format(self.NAME_TABLE_GIANGDAY)
                    
            cursor.execute(query, (item["MALOP"], item["MAMH"], item["MAGV"], item["HOCKY"], item["NAM"], item["TUNGAY"], item["DENNGAY"]))
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
                        SET HOCKY = %s, NAM = %s, TUNGAY = %s, DENNGAY = %s
                        WHERE MALOP = %s, MAMH = %s, MAGV = %s
                        """.format(self.NAME_TABLE_GIANGDAY)

                cursor.execute(query, (item["HOCKY"], item["NAM"], item["TUNGAY"], item["DENNGAY"], item["MALOP"], item["MAMH"], item["MAGV"]))
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
                    WHERE MALOP = %s, MAMH = %s, MAGV = %s
                    """.format(self.NAME_TABLE_GIANGDAY)

            cursor.execute(query, (item["MALOP"], item["MAMH"], item["MAGV"]))
            db.commit()
            print(f"Xoá thành công: Mã lớp: {0}, Mã môn học: {1}, Mã GV: {2}".format(item["MALOP"], item["MAMH"], item["MAGV"]))
        except Exception as e:
            db.rollback()
            print(f"Lỗi khi xoá dữ liệu: {e}")
        finally:
            self.close()