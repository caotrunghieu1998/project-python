import tkinter as tk
from tkinter import messagebox
from models.LopModel import LopModel
from client.views.lopView import LopView

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
        self._view = LopView.getInstance()
        
    def initView(self):
        return self._view.initView()

    def add_item(self):
        item = self._view.get_input_values()
        if any(value == "" for value in item.values()):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        self._model.add_item(item)
        self._view.refresh_treeview(self._model.get_data())
        self._view.clear_inputs()

    def edit_item(self):
        index = self._view.get_selected_item()
        if index is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để sửa.")
            return

        item = self._view.get_input_values()
        self._model.update_item(index, item)
        self._view.refresh_treeview(self._model.get_data())
        self._view.clear_inputs()

    def delete_item(self):
        index = self._view.get_selected_item()
        if index is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        self._model.delete_item(index)
        self._view.refresh_treeview(self._model.get_data())
    
    def refresh_treeview(self):
        """Cập nhật Treeview với dữ liệu hiện tại."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in self.data:
            self.tree.insert("", tk.END, values=(item["MAKHOA"], item["TENKHOA"], item["NGTLAP"], item["TRGKHOA"]))
    
    def showView(self):
        return self._view.showView()
