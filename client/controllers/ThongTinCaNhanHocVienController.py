from tkinter import messagebox
from models.ThongTinCaNhanHocVienModel import ThongTinCaNhanHocVienModel
from views.ThongTinCaNhanHocVienView import ThongTinCaNhanHocVienView

class ThongTinCaNhanHocVienController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanHocVienController._instance):
            return ThongTinCaNhanHocVienController._instance
        ThongTinCaNhanHocVienController._instance = ThongTinCaNhanHocVienController()
        return ThongTinCaNhanHocVienController._instance

    def __init__(self, model: ThongTinCaNhanHocVienModel, view: ThongTinCaNhanHocVienView):
        self._model = model
        self._view = view
        self._view.ma_hv.bind('<KeyRelease>', self.ma_hv_text_change)
        self._view.ho_hv.bind('<KeyRelease>', self.field_text_change)
        self._view.ten_hv.bind('<KeyRelease>', self.field_text_change)
        self._view.gioitinh.bind('<KeyRelease>', self.field_text_change)
        self._view.noisinh.bind('<KeyRelease>', self.field_text_change)
        self._view.ma_lop.bind('<KeyRelease>', self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonEdit["command"] = self.update_item
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        data = self._model.load_item(self._view.hoc_vien_param)
        self._view.set_input_values(data)
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="disabled")

    def ma_hv_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="disabled")

    def field_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="normal")

    def btn_refresh(self):
        self._view.buttonEdit.config(state="disabled")
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        item = self._view.get_input_values()
        status = self._model.update_item(item)
        if status == "UPDATED":
            messagebox.showinfo("Thông báo", "Cập nhật thành công")
            self._view.clear_inputs()
        elif status == "NONE":
            messagebox.showinfo("Thông báo", "Dữ liệu không bị thay đổi, không cần cập nhật")
        else:
            messagebox.showerror("Thông báo", "Lôi thao tác")
        self.load_data()