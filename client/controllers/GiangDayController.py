from tkinter import messagebox
from models.GiangDayModel import GiangDayModel
from views.GiangDayView import GiangDayView

class GiangDayController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (GiangDayController._instance):
            return GiangDayController._instance
        GiangDayController._instance = GiangDayController()
        return GiangDayController._instance

    def __init__(self, model: GiangDayModel, view: GiangDayView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._view.ma_lop.bind('<KeyRelease>', self.ma_key_text_change)
        self._view.ma_mh.bind('<KeyRelease>', self.ma_key_text_change)
        self._view.ma_gv.bind('<KeyRelease>', self.ma_key_text_change)
        self._view.hoc_ky.bind('<KeyRelease>', self.field_text_change)
        self._view.nam.bind('<KeyRelease>', self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonAdd["command"] = self.add_item
        self._view.buttonEdit["command"] = self.update_item
        self._view.buttonRemove["command"] = self.delete_item
        self._view.tree.bind('<<TreeviewSelect>>', self.get_selected_item)
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        data = self._model.get_list_data()
        self._view.load_list(data)
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")

    def ma_key_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonAdd.config(state="normal")
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")

    def field_text_change(self, event=None):
        self._view.buttonRefresh.config(state="normal")
        self._view.buttonAdd.config(state="normal")
        self._view.buttonEdit.config(state="normal")
        self._view.buttonRemove.config(state="normal")

    def btn_refresh(self):
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")
        self._view.clear_inputs()
        self.load_data()
        
    def add_item(self):
        """Thêm dữ liệu"""
        item = self._view.get_input_values()
        if any(value == "" for value in item.values()):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        ma_lop = item["MALOP"]
        ma_mh = item["MAMH"]
        ma_gv = item["MAGV"]
        is_exist = self._model.is_ma_exist(ma_lop, ma_mh, ma_gv)
        if is_exist == True:
            messagebox.showwarning("Cảnh báo", "Mã đã tồn tại")
            return
        
        self._model.add_item(item)
        self._view.clear_inputs()
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        ma = self._view.get_selected_item()
        if ma is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để sửa.")
            return

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
        
    def delete_item(self):
        """Xoá dữ liệu đã chọn"""
        ma = self._view.get_selected_item()
        
        if ma is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        # Hiển thị hộp thoại xác nhận
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa không?")
        
        if confirm:  # Nếu người dùng nhấn "Yes"
            item = self._view.get_input_values()
            self._model.delete_item(item)
            self.load_data()
            messagebox.showinfo("Thông báo", "Xóa thành công.")
        
    def get_selected_item(self, event=None):
        """Hàm xử lý khi người dùng chọn một mục trong Treeview."""
        self._view.buttonAdd.config(state="normal")
        self._view.buttonRemove.config(state="normal")
        
        self._view.clear_inputs()
        hv = self._view.get_selected_item()
        if hv != None:
            ma_lop = hv[0]
            ma_mh = hv[1]
            ma_gv = hv[2]
            hoc_ky = hv[3]
            nam = hv[4]
            tu_ngay = hv[5]
            den_ngay = hv[6]
            
            self._view.set_ma_lop(ma_lop)
            self._view.set_ma_mh(ma_mh)
            self._view.set_ma_gv(ma_gv)
            self._view.set_hoc_ky(hoc_ky)
            self._view.set_nam(nam)
            self._view.set_tu_ngay(tu_ngay)
            self._view.set_den_ngay(den_ngay)