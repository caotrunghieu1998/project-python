from tkinter import messagebox
from models.ThongTinCaNhanGiaoVienModel import ThongTinCaNhanGiaoVienModel
from views.ThongTinCaNhanGiaoVienView import ThongTinCaNhanGiaoVienView

class ThongTinCaNhanGiaoVienController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanGiaoVienController._instance):
            return ThongTinCaNhanGiaoVienController._instance
        ThongTinCaNhanGiaoVienController._instance = ThongTinCaNhanGiaoVienController()
        return ThongTinCaNhanGiaoVienController._instance

    def __init__(self, model: ThongTinCaNhanGiaoVienModel, view: ThongTinCaNhanGiaoVienView):
        self._model = model
        self._view = view
        self._view.ma_gv.bind('<KeyRelease>', self.ma_gv_text_change)
        self._view.ho_ten.bind('<KeyRelease>', self.field_text_change)
        self._view.hoc_vi.bind('<KeyRelease>', self.field_text_change)
        self._view.hoc_ham.bind('<KeyRelease>', self.field_text_change)
        self._view.gioi_tinh.bind('<KeyRelease>', self.field_text_change)
        self._view.heso.bind('<KeyRelease>', self.field_text_change)
        self._view.muc_luong.bind('<KeyRelease>', self.field_text_change)
        self._view.ma_khoa.bind('<KeyRelease>', self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonEdit["command"] = self.update_item
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        data = self._model.load_item(self._view.giao_vien_param)
        self._view.set_input_values(data)
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonEdit.config(state="disabled")

    def ma_gv_text_change(self, event=None):
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