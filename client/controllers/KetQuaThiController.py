from tkinter import messagebox
from models.KetQuaThiModel import KetQuaThiModel
from views.KetQuaThiView import KetQuaThiView

class KetQuaThiController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (KetQuaThiController._instance):
            return KetQuaThiController._instance
        KetQuaThiController._instance = KetQuaThiController()
        return KetQuaThiController._instance

    def __init__(self, model: KetQuaThiModel, view: KetQuaThiView):
        self._model = model
        self._view = view
        self._tree = self._view.tree
        self._view.ma_hv.bind('<KeyRelease>', self.ma_hv_text_change)
        self._view.ma_mh.bind('<KeyRelease>', self.field_text_change)
        self._view.lanthi.bind('<KeyRelease>', self.field_text_change)
        self._view.diem.bind('<KeyRelease>', self.field_text_change)
        self._view.kqua.bind('<KeyRelease>', self.field_text_change)
        self._view.buttonRefresh["command"] = self.btn_refresh
        self._view.buttonAdd["command"] = self.add_item
        self._view.buttonEdit["command"] = self.update_item
        self._view.buttonRemove["command"] = self.delete_item
        self._view.tree.bind('<<TreeviewSelect>>', self.get_selected_item)
        
        self.load_data()
            
    def load_data(self):
        """Hiển thị danh sách"""
        print("self._view.data_param", self._view.data_param)
        data = self._model.get_data_by_ma_hv(self._view.data_param[0]["MAHV"])
        print("datadata", data)
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

        ma_hv = item["MAHV"]
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
            ma_hv = hv[0]
            ma_mh = hv[1]
            lanthi = hv[2]
            ng_thi = hv[3]
            diem = hv[4]
            kqua = hv[5]
            
            self._view.set_ma_hv(ma_hv)
            self._view.set_ma_mh(ma_mh)
            self._view.set_lanthi(lanthi)
            self._view.set_ng_thi(ng_thi)
            self._view.set_diem(diem)
            self._view.set_kqua(kqua)