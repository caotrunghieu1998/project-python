from tkinter import ttk
from tkinter import *


class LopView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (LopView._instance):
            return LopView._instance
        LopView._instance = LopView()
        
        return LopView._instance

    def __init__(self, root: Tk):
        self._root = root
        self._tree = ttk.Treeview(None)
        self.initView()
        
    @property
    def tree(self):
        return self._tree
    
    def initView(self):
        root = self._root

        root.title("Danh sách lóp")
        root.geometry("800x600")
        self.top_frame = Frame(root)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        self.ma_lop = self.add_labeled_entry("Mã Lớp:", 0)
        self.ten_lop = self.add_labeled_entry("Tên Lớp:", 2)
        self.trg_lop = self.add_labeled_entry("Trưởng Lớp:", 4)
        self.siso = self.add_labeled_entry("Sỉ Số:", 6)
        self.ma_gvcn = self.add_labeled_entry("Mã GVCN:", 8)
        
        self.buttonAdd = Button(self.top_frame, text="Thêm")
        self.buttonAdd.grid(row=1, column=1, pady=10)
        self.buttonEdit = Button(self.top_frame, text="Sửa")
        self.buttonEdit.grid(row=1, column=3, pady=10)
        self.buttonRemove = Button(self.top_frame, text="Xoá")
        self.buttonRemove.grid(row=1, column=5, pady=10)

    def add_labeled_entry(self, label, column):
        """Thêm nhãn và ô nhập liệu."""
        Label(self.top_frame, text=label).grid(row=0, column=column)
        entry = Entry(self.top_frame, width=15)
        entry.grid(row=0, column=column + 1, padx=5)
        return entry

    def body(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self._root, columns=("MALOP", "TENLOP", "TRGLOP", "SISO", "MAGVCN"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MALOP", text="Mã Lớp")
        self._tree.heading("TENLOP", text="Tên Lớp")
        self._tree.heading("TRGLOP", text="Trưởng Lớp")
        self._tree.heading("SISO", text="Sỉ Số")
        self._tree.heading("MAGVCN", text="Mã GVCN")

        self._tree.column("MALOP", width=100, anchor="center")
        self._tree.column("TENLOP", width=200, anchor="w")
        self._tree.column("TRGLOP", width=200, anchor="w")
        self._tree.column("SISO", width=150, anchor="center")
        self._tree.column("MAGVCN", width=150, anchor="w")

    #get
    def get_selected_ma_lop(self):
        """Trả về Mã Lớp (MA_LOP) của item được chọn."""
        selected_items = self._tree.selection()
        ma_lop = None
        
        if selected_items:  
            first_item = selected_items[0]  
            values = self._tree.item(first_item, "values")  
            if values:  
                ma_lop = values[0]
        return ma_lop

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
        self.ma_lop.delete(0, END)
        self.ten_lop.delete(0, END)
        self.trg_lop.delete(0, END)
        self.siso.delete(0, END)
        self.ma_gvcn.delete(0, END)
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MALOP"], item["TENLOP"], item["TRGLOP"], item["SISO"], item["MAGVCN"]))
        
    def showView(self):
        self._root.mainloop()