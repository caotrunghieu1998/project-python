from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class MonHocView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (MonHocView._instance):
            return MonHocView._instance
        MonHocView._instance = MonHocView()
        
        return MonHocView._instance

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

        root.title("Danh sách môn học")
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
        self.labelTitle = Label(self.top_frame, text="Danh sách môn học", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã môn học
        self.label_ma_mh = Label(self.top_frame, text="Mã môn học: ", font=("Arial", 10, "bold"))
        self.label_ma_mh.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_mh_text = StringVar()
        self.ma_mh = Entry(self.top_frame, textvariable=self.entry_ma_mh_text, width=40, font=("Arial", 10))
        self.ma_mh.grid(row=1, column=1, padx=10, pady=5)

        # Tên môn học
        self.label_ten_mh = Label(self.top_frame, text="Tên môn học: ", font=("Arial", 10, "bold"))
        self.label_ten_mh.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ten_mh_text = StringVar()
        self.ten_mh = Entry(self.top_frame, textvariable=self.entry_ten_mh_text, width=40, font=("Arial", 10))
        self.ten_mh.grid(row=2, column=1, padx=10, pady=5)

        # TCLT
        self.label_tclt = Label(self.top_frame, text="TCLT: ", font=("Arial", 10, "bold"))
        self.label_tclt.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_tclt_text = StringVar()
        self.tclt = Entry(self.top_frame, textvariable=self.entry_tclt_text, width=40, font=("Arial", 10))
        self.tclt.grid(row=3, column=1, padx=10, pady=5)
        
        # TCTH
        self.label_tcth = Label(self.top_frame, text="TCTH: ", font=("Arial", 10, "bold"))
        self.label_tcth.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_tcth_text = StringVar()
        self.tcth = Entry(self.top_frame, textvariable=self.entry_tcth_text, width=40, font=("Arial", 10))
        self.tcth.grid(row=4, column=1, padx=10, pady=5)
        
        # Mã khoa
        self.label_ma_khoa = Label(self.top_frame, text="Mã khoa: ", font=("Arial", 10, "bold"))
        self.label_ma_khoa.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_khoa_text = StringVar()
        self.ma_khoa = Entry(self.top_frame, textvariable=self.entry_ma_khoa_text, width=40, font=("Arial", 10))
        self.ma_khoa.grid(row=5, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonAdd = Button(self.button_frame, text="Thêm", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonAdd.grid(row=0, column=1, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=2, padx=10)

        self.buttonRemove = Button(self.button_frame, text="Xoá", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRemove.grid(row=0, column=3, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=4, padx=10)

    def body(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self._root, columns=("MAMH", "TENMH", "TCLT", "TCTH", "MAKHOA"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MAMH", text="Mã môn học")
        self._tree.heading("TENMH", text="Tên môn học")
        self._tree.heading("TCLT", text="TCLT")
        self._tree.heading("TCTH", text="TCTH")
        self._tree.heading("MAKHOA", text="Mã khoa")

        self._tree.column("MAMH", width=20, anchor="center")
        self._tree.column("TENMH", width=20, anchor="w")
        self._tree.column("TCLT", width=20, anchor="center")
        self._tree.column("TCTH", width=20, anchor="center")
        self._tree.column("MAKHOA", width=20, anchor="center")

    #get
    def get_selected_item(self):
        """Trả về của item được chọn."""
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
            "MAMH": self.get_ma_mh(),
            "TENMH": self.get_ten_mh(),
            "TCLT": self.get_tclt(),
            "TCTH": self.get_tcth(),
            "MAKHOA": self.get_ma_khoa(),
        }
        
    def get_ma_mh(self):
        return self.entry_ma_mh_text.get()
    def get_ten_mh(self):
        return self.entry_ten_mh_text.get()
    def get_tclt(self):
        return self.entry_tclt_text.get()
    def get_tcth(self):
        return self.entry_tcth_text.get()
    def get_ma_khoa(self):
        return self.entry_ma_khoa_text.get()
        

    #set
    def set_ma_mh(self, ma_hv):
        self.entry_ma_mh_text.set(ma_hv)
    def set_ten_mh(self, ma_hv):
        self.entry_ten_mh_text.set(ma_hv)
    def set_tclt(self, ma_hv):
        self.entry_tclt_text.set(ma_hv)
    def set_tcth(self, ma_hv):
        self.entry_tcth_text.set(ma_hv)
    def set_ma_khoa(self, ma_hv):
        self.entry_ma_khoa_text.set(ma_hv)

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_mh.delete(0, END)
        self.ten_mh.delete(0, END)
        self.tclt.delete(0, END)
        self.tcth.delete(0, END)
        self.ma_khoa.delete(0, END)
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MAMH"], item["TENMH"], item["TCLT"], item["TCTH"], item["MAKHOA"]))
        
    def showView(self):
        self._root.mainloop()