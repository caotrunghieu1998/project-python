from tkinter import messagebox
from models.LopModel import LopModel, Lop
from views.lopView import LopView

class LopController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (LopController._instance):
            return LopController._instance
        LopController._instance = LopController()
        return LopController._instance

    def __init__(self, model: LopModel, view: LopView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._view.buttonAdd["command"] = self.add_item
        self._view.buttonEdit["command"] = self.update_item
        self._view.buttonRemove["command"] = self.delete_item
        self._view.tree.bind('<<TreeviewSelect>>', self.get_selected_item)
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách lớp"""
        data = self._model.get_list_data()
        self._view.load_list(data)

    def add_item(self):
        """Thêm dữ liệu"""
        item = self._view.get_input_values()
        if any(value == "" for value in item.values()):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        self._model.add_item(item)
        self._view.clear_inputs()
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        ma_lop = self._view.get_selected_ma_lop()
        if ma_lop is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để sửa.")
            return

        item = self._view.get_input_values()
        self._model.update_item(ma_lop, item)
        self._view.clear_inputs()
        self.load_data()

    def delete_item(self):
        """Xoá dữ liệu"""
        ma_lop = self._view.get_selected_ma_lop()
        if ma_lop is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        self._model.delete_item(ma_lop)
        self.load_data()
        
    def get_selected_item(self, event=None):
        """Hàm xử lý khi người dùng chọn một mục trong Treeview."""
        ma_lop = self._view.get_selected_ma_lop()
        