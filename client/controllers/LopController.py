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

    def __init__(self, model: LopModel, view: LopView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._view.ma_lop.bind('<KeyRelease>', self.ma_lop_text_change)
        self._view.ten_lop.bind('<KeyRelease>', self.field_text_change)
        self._view.trg_lop.bind('<KeyRelease>', self.field_text_change)
        self._view.siso.bind('<KeyRelease>', self.field_text_change)
        self._view.ma_gvcn.bind('<KeyRelease>', self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonAdd["command"] = self.add_item
        self._view.buttonEdit["command"] = self.update_item
        self._view.buttonRemove["command"] = self.delete_item
        self._view.tree.bind('<<TreeviewSelect>>', self.get_selected_item)
        
        self.load_data()

    def initCommandButtonBack(self, commandBack):
         if commandBack:
            def back():
                self._view._root.destroy()
                commandBack()

            self._view.buttonBack["command"] = back
            
    def load_data(self):
        """Hiển thị danh sách lớp"""
        data = self._model.get_list_data()
        self._view.load_list(data)
        self._view.buttonEdit.config(state="disabled")
        self._view.buttonRemove.config(state="disabled")

    def ma_lop_text_change(self, event=None):
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
        is_exist = self._model.is_ma_lop_exist(ma_lop)
        if is_exist == True:
            messagebox.showwarning("Cảnh báo", "Mã lớp đã tồn tại")
            return
        
        self._model.add_item(item)
        self._view.clear_inputs()
        self.load_data()

    def update_item(self):
        """Chỉnh sửa dữ liệu"""
        ma_lop = self._view.get_selected_item()
        if ma_lop is None:
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
        ma_lop = self._view.get_selected_item()
        
        if ma_lop is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một dòng để xóa.")
            return

        # Hiển thị hộp thoại xác nhận
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa lớp này không?")
        
        if confirm:  # Nếu người dùng nhấn "Yes"
            item = self._view.get_input_values()
            self._model.delete_item(item)
            self.load_data()
            messagebox.showinfo("Thông báo", "Xóa lớp thành công.")
        
    def get_selected_item(self, event=None):
        """Hàm xử lý khi người dùng chọn một mục trong Treeview."""
        self._view.buttonAdd.config(state="normal")
        self._view.buttonRemove.config(state="normal")
        
        self._view.clear_inputs()
        lop = self._view.get_selected_item()
        if lop != None:
            ma_lop = lop[0]
            ten_lop = lop[1]
            trg_lop = lop[2]
            siso = lop[3]
            ma_gvcn = lop[4]
            
            self._view.set_ma_lop(ma_lop)
            self._view.set_ten_lop(ten_lop)
            self._view.set_trg_lop(trg_lop)
            self._view.set_siso(siso)
            self._view.set_ma_gvcn(ma_gvcn)