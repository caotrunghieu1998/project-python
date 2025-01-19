from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class KhoaView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (KhoaView._instance):
            return KhoaView._instance
        KhoaView._instance = KhoaView()
        
        return KhoaView._instance

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

        root.title("Danh sách khoa")
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
        self.labelTitle = Label(self.top_frame, text="Danh sách khoa", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã khoa
        self.label_ma_khoa = Label(self.top_frame, text="Mã khoa: ", font=("Arial", 10, "bold"))
        self.label_ma_khoa.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_khoa_text = StringVar()
        self.ma_khoa = Entry(self.top_frame, textvariable=self.entry_ma_khoa_text, width=40, font=("Arial", 10))
        self.ma_khoa.grid(row=1, column=1, padx=10, pady=5)

        # Tên khoa
        self.label_ten_khoa = Label(self.top_frame, text="Tên Khoa: ", font=("Arial", 10, "bold"))
        self.label_ten_khoa.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ten_khoa_text = StringVar()
        self.ten_khoa = Entry(self.top_frame, textvariable=self.entry_ten_khoa_text, width=40, font=("Arial", 10))
        self.ten_khoa.grid(row=2, column=1, padx=10, pady=5)

        # Ngày thành lập
        self.label_ngtlap = Label(self.top_frame, text="Ngày thành lập: ", font=("Arial", 10, "bold"))
        self.label_ngtlap.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.ngtlap = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ngtlap.grid(row=3, column=1, padx=10, pady=5)

        # Trưởng khoa
        self.label_trgkhoa = Label(self.top_frame, text="Trưởng khoa: ", font=("Arial", 10, "bold"))
        self.label_trgkhoa.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_trgkhoa_text = StringVar()
        self.trgkhoa = Entry(self.top_frame, textvariable=self.entry_trgkhoa_text, width=40, font=("Arial", 10))
        self.trgkhoa.grid(row=4, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=20)

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
            self._root, columns=("MAKHOA", "TENKHOA", "NGTLAP", "TRGKHOA"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MAKHOA", text="Mã khoa")
        self._tree.heading("TENKHOA", text="Tên khoa")
        self._tree.heading("NGTLAP", text="Ngày thành lập")
        self._tree.heading("TRGKHOA", text="Trưởng khoa")

        self._tree.column("MAKHOA", width=20, anchor="center")
        self._tree.column("TENKHOA", width=20, anchor="w")
        self._tree.column("NGTLAP", width=20, anchor="w")
        self._tree.column("TRGKHOA", width=20, anchor="center")

    #get
    def get_selected_item(self):
        """Trả về Mã khoa của item được chọn."""
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
            "MAKHOA": self.get_ma_khoa(),
            "TENKHOA": self.get_ten_khoa(),
            "NGTLAP": self.get_ngtlap(),
            "TRGKHOA": self.get_trgkhoa(),
        }
        
    def get_ma_khoa(self):
        return self.entry_ma_khoa_text.get()
        
    def get_ten_khoa(self):
        return self.entry_ten_khoa_text.get()
        
    def get_ngtlap(self):
        return self.ngtlap.get_date()
        
    def get_trgkhoa(self):
        return self.entry_trgkhoa_text.get()

    #set
    def set_ma_khoa(self, ma_hv):
        self.entry_ma_khoa_text.set(ma_hv)

    def set_ten_khoa(self, ho_hv):
        self.entry_ten_khoa_text.set(ho_hv)

    def set_ngtlap(self, ngtlap):
        self.ngtlap.set_date(datetime.strptime(ngtlap, "%Y-%m-%d %H:%M:%S").date())

    def set_trgkhoa(self, ma_lop):
        self.entry_trgkhoa_text.set(ma_lop)

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_khoa.delete(0, END)
        self.ten_khoa.delete(0, END)
        self.ngtlap.set_date(datetime.now().date())
        self.trgkhoa.delete(0, END)
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MAKHOA"], item["TENKHOA"], item["NGTLAP"], item["TRGKHOA"]))
        
    def showView(self):
        self._root.mainloop()