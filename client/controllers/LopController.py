import tkinter as tk
from tkinter import messagebox
from models.LopModel import LopModel
from views.lopView import LopView

class LopController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (LopController._instance):
            return LopController._instance
        LopController._instance = LopController()
        return LopController._instance

    def __init__(self):
        self._model = LopModel.getInstance()
        self._view = LopView.getInstance(self._model)
        self._tree = LopView.tree
        
    def initView(self):
        """Khởi tạo màn hình"""
        return self._view.initView(self._model)
    
    def load_data(self):
        """Hiển thị danh sách lớp"""
        data = self._model.get_list_data()
        self._view.refresh_treeview(data)

    def add_item(self):
        """Thêm dữ liệu"""
        item = self._view.get_input_values()
        if any(value == "" for value in item.values()):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        self._model.add_item(item)
        self._view.refresh_treeview(self._model.get_list_data())
        self._view.clear_inputs()

    def edit_item(self):
        """Chỉnh sửa dữ liệu"""
        index = self._view.get_selected_item()
        if index is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để sửa.")
            return

        item = self._view.get_input_values()
        self._model.update_item(index, item)
        self._view.refresh_treeview(self._model.get_list_data())
        self._view.clear_inputs()

    def delete_item(self):
        """Xoá dữ liệu"""
        index = self._view.get_selected_item()
        if index is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        self._model.delete_item(index)
        self._view.refresh_treeview(self._model.get_list_data())
    
    def refresh_treeview(self):
        """Làm mới dữ liệu bảng"""
        return self._view.refresh_treeview()
    
    def showView(self):
        """Hiển thị màn hình"""
        return self._view.showView()
