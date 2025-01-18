import tkinter as tk
from tkinter import ttk

from models.LopModel import LopModel

class LopView:
    _instance = None
    _model = None

    @classmethod
    def getInstance(cls, model: LopModel):
        if (LopView._instance):
            return LopView._instance
        LopView._instance = LopView()
        LopView._model = model
        
        return LopView._instance

    def __init__(self):
        self.tkRoot = tk.Tk()
        self._ds = []
        self._tree = ttk.Treeview(None)
        
    @property
    def tree(self):
        return self._tree
    
    def initView(self, model):
        root = self.tkRoot

        root.title("Danh sách lóp")
        root.geometry("800x600")
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.create_input_fields()
        self.create_buttons(model)
        self.create_treeview()

    def create_input_fields(self):
        """Tạo các ô nhập liệu."""
        self.ma_lop = self.add_labeled_entry("Mã Lớp:", 0)
        self.ten_lop = self.add_labeled_entry("Tên Lớp:", 2)
        self.trg_lop = self.add_labeled_entry("Trưởng Lớp:", 4)
        self.siso = self.add_labeled_entry("Sỉ Số:", 6)
        self.ma_gvcn = self.add_labeled_entry("Mã GVCN:", 8)

    def add_labeled_entry(self, label, column):
        """Thêm nhãn và ô nhập liệu."""
        tk.Label(self.top_frame, text=label).grid(row=0, column=column)
        entry = tk.Entry(self.top_frame, width=15)
        entry.grid(row=0, column=column + 1, padx=5)
        return entry

    def create_buttons(self, model: LopModel):
        """Tạo các nút chức năng."""
        tk.Button(self.top_frame, text="Thêm", command=self._model.add_item).grid(row=1, column=1, pady=10)
        tk.Button(self.top_frame, text="Sửa", command=self._model.update_item).grid(row=1, column=3, pady=10)
        tk.Button(self.top_frame, text="Xóa", command=self._model.delete_item).grid(row=1, column=5, pady=10)

    def create_treeview(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self.tkRoot, columns=("MALOP", "TENLOP", "TRGLOP", "SISO", "MAGVCN"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MALOP", text="Mã Lớp")
        self._tree.heading("TENLOP", text="Tên Lớp")
        self._tree.heading("TRGLOP", text="Trưởng Lớp")
        self._tree.heading("SISO", text="Sỉ Số")
        self._tree.heading("MAGVCN", text="Trưởng Lớp")

        self._tree.column("MALOP", width=100, anchor="center")
        self._tree.column("TENLOP", width=200, anchor="w")
        self._tree.column("TRGLOP", width=200, anchor="w")
        self._tree.column("SISO", width=150, anchor="center")
        self._tree.column("MAGVCN", width=150, anchor="w")

    def get_selected_item(self):
        """Trả về item được chọn."""
        selected = self._tree.selection()
        if selected:
            return self._tree.index(selected[0])
        return self._tree

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "MALOP": self.ma_lop.get().strip(),
            "TENLOP": self.ten_lop.get().strip(),
            "TRGLOP": self.trg_lop.get().strip(),
            "SISO": self.siso.get().strip(),
            "MAGVCN": self.ma_gvcn.get().strip(),
        }
        
    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_lop.delete(0, tk.END)
        self.ten_lop.delete(0, tk.END)
        self.trg_lop.delete(0, tk.END)
        self.siso.delete(0, tk.END)
        self.ma_gvcn.delete(0, tk.END)
        
    def refresh_treeview(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", tk.END, values=(item["MALOP"], item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"]))
        
    def showView(self):
        self.tkRoot.mainloop()