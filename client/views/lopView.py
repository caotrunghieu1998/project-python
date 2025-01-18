from tkinter import ttk
from tkinter import *

from common.common import Common

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
        self._common = Common()
        self._common.center_window(root)
        self.initView()
        
    @property
    def tree(self):
        return self._tree
    
    def initView(self):
        root = self._root

        root.title("Danh sách lớp")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        
        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Danh sách lớp", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

        # Mã lớp
        self.label_ma_lop = Label(self.top_frame, text="Mã Lớp: ", font=("Arial", 10, "bold"))
        self.label_ma_lop.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_lop_text = StringVar()
        self.ma_lop = Entry(self.top_frame, textvariable=self.entry_ma_lop_text, width=40, font=("Arial", 10))
        self.ma_lop.grid(row=1, column=1, padx=10, pady=5)

        # Tên lớp
        self.label_ten_lop = Label(self.top_frame, text="Tên Lớp: ", font=("Arial", 10, "bold"))
        self.label_ten_lop.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ten_lop_text = StringVar()
        self.ten_lop = Entry(self.top_frame, textvariable=self.entry_ten_lop_text, width=40, font=("Arial", 10))
        self.ten_lop.grid(row=2, column=1, padx=10, pady=5)

        # Trưởng lớp
        self.label_trg_lop = Label(self.top_frame, text="Trưởng Lớp: ", font=("Arial", 10, "bold"))
        self.label_trg_lop.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_trg_lop_text = StringVar()
        self.trg_lop = Entry(self.top_frame, textvariable=self.entry_trg_lop_text, width=40, font=("Arial", 10))
        self.trg_lop.grid(row=3, column=1, padx=10, pady=5)

        # Sỉ số
        self.label_siso = Label(self.top_frame, text="Sỉ Số: ", font=("Arial", 10, "bold"))
        self.label_siso.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_siso_text = StringVar()
        self.siso = Entry(self.top_frame, textvariable=self.entry_siso_text, width=10, font=("Arial", 10))
        self.siso.grid(row=4, column=1, padx=10, pady=5)

        # Mã GVCN
        self.label_ma_gvcn = Label(self.top_frame, text="Mã GVCN: ", font=("Arial", 10, "bold"))
        self.label_ma_gvcn.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_gvcn_text = StringVar()
        self.ma_gvcn = Entry(self.top_frame, textvariable=self.entry_ma_gvcn_text, width=40, font=("Arial", 10))
        self.ma_gvcn.grid(row=5, column=1, padx=10, pady=20)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=6, column=0, columnspan=2, padx=10)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonAdd = Button(self.button_frame, text="Thêm", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonAdd.grid(row=0, column=1, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=2, padx=10)

        self.buttonRemove = Button(self.button_frame, text="Xoá", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRemove.grid(row=0, column=3, padx=10)

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

        self._tree.column("MALOP", width=20, anchor="center")
        self._tree.column("TENLOP", width=40, anchor="w")
        self._tree.column("TRGLOP", width=40, anchor="w")
        self._tree.column("SISO", width=20, anchor="center")
        self._tree.column("MAGVCN", width=40, anchor="w")

    #get
    def get_selected_item(self):
        """Trả về Mã Lớp (MA_LOP) của item được chọn."""
        selected_items = self._tree.selection()
        
        if selected_items:  
            first_item = selected_items[0]  
            values = self._tree.item(first_item, "values")  
            return values
        else:
            return None

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "MALOP": self.get_ma_lop(),
            "TENLOP": self.get_ten_lop(),
            "TRGLOP": self.get_trg_lop(),
            "SISO": self.get_siso(),
            "MAGVCN": self.get_ma_gvcn(),
        }
        
    def get_ma_lop(self):
        return self.entry_ma_lop_text.get()

    def get_ten_lop(self):
        return self.entry_ten_lop_text.get()

    def get_trg_lop(self):
        return self.entry_trg_lop_text.get()

    def get_siso(self):
        return self.entry_siso_text.get()

    def get_ma_gvcn(self):
        return self.entry_ma_gvcn_text.get()

    #set
    def set_ma_lop(self, ma_lop):
        self.entry_ma_lop_text.set(ma_lop)

    def set_ten_lop(self, ten_lop):
        self.entry_ten_lop_text.set(ten_lop)

    def set_trg_lop(self, trg_lop):
        self.entry_trg_lop_text.set(trg_lop)

    def set_siso(self, siso):
        self.entry_siso_text.set(siso)

    def set_ma_gvcn(self, ma_gvcn):
        self.entry_ma_gvcn_text.set(ma_gvcn)

        
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