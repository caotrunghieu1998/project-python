from models.baseData import dataLop

class Lop:
    def __init__(self, MALOP, TENLOP, TRGLOP, SISO, MAGVCN):
        self._MALOP = MALOP
        self._TENLOP = TENLOP
        self._TRGLOP = TRGLOP
        self._SISO = SISO
        self._MAGVCN = MAGVCN


class LopModel:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (LopModel._instance):
            return LopModel._instance
        LopModel._instance = LopModel()
        return LopModel._instance
    
    def __init__(self):
        pass
    
    def get_data(self):
        """Trả về danh sách dữ liệu."""
        return self.data

    def add_item(self, item):
        """Thêm một khoa mới."""
        self.data.append(item)

    def update_item(self, index, item):
        """Cập nhật thông tin khoa."""
        self.data[index] = item

    def delete_item(self, index):
        """Xóa khoa."""
        del self.data[index]