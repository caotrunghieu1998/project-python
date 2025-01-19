from tkinter import messagebox
from models.KhoaModel import KhoaModel
from views.KhoaView import KhoaView

class KhoaController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (KhoaController._instance):
            return KhoaController._instance
        KhoaController._instance = KhoaController()
        return KhoaController._instance

    def __init__(self, model: KhoaModel, view: KhoaView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._view.ma_khoa.bind('<KeyRelease>', self.ma_hv_text_change)
        self._view.ten_khoa.bind('<KeyRelease>', self.field_text_change)
        self._view.trgkhoa.bind('<KeyRelease>', self.field_text_change)
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

    def ma_hv_text_change(self, event=None):
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

        ma_hv = item["MAKHOA"]
        is_exist = self._model.is_ma_hv_exist(ma_hv)
        if is_exist == True:
            messagebox.showwarning("Cảnh báo", "Mã đã tồn tại")
            return
        
        self._model.add_item(item)
        self._view.clear_inputs()
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        ma_hv = self._view.get_selected_item()
        if ma_hv is None:
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
        ma_hv = self._view.get_selected_item()
        
        if ma_hv is None:
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
            ma_khoa = hv[0]
            ten_khoa = hv[1]
            ngtlap = hv[2]
            trgkhoa = hv[3]
            
            self._view.set_ma_khoa(ma_khoa)
            self._view.set_ten_khoa(ten_khoa)
            self._view.set_ngtlap(ngtlap)
            self._view.set_trgkhoa(trgkhoa)