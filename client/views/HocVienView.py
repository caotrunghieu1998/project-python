from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class HocVienView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (HocVienView._instance):
            return HocVienView._instance
        HocVienView._instance = HocVienView()
        
        return HocVienView._instance

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

        root.title("Danh sách học viên")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        self.top_frame.grid_columnconfigure(4, weight=4)
        self.top_frame.grid_columnconfigure(5, weight=5)
        
        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Danh sách học viên", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã học viên
        self.label_ma_hv = Label(self.top_frame, text="Mã Học Viên: ", font=("Arial", 10, "bold"))
        self.label_ma_hv.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_hv_text = StringVar()
        self.ma_hv = Entry(self.top_frame, textvariable=self.entry_ma_hv_text, width=40, font=("Arial", 10))
        self.ma_hv.grid(row=1, column=1, padx=10, pady=5)

        # Họ tên học viên
        self.label_ho_hv = Label(self.top_frame, text="Họ: ", font=("Arial", 10, "bold"))
        self.label_ho_hv.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ho_hv_text = StringVar()
        self.ho_hv = Entry(self.top_frame, textvariable=self.entry_ho_hv_text, width=40, font=("Arial", 10))
        self.ho_hv.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_ten_hv = Label(self.top_frame, text="Tên: ", font=("Arial", 10, "bold"))
        self.label_ten_hv.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_ten_hv_text = StringVar()
        self.ten_hv = Entry(self.top_frame, textvariable=self.entry_ten_hv_text, width=40, font=("Arial", 10))
        self.ten_hv.grid(row=3, column=1, padx=10, pady=5)

        # Ngày sinh
        self.label_ngsinh_hv = Label(self.top_frame, text="Ngày sinh: ", font=("Arial", 10, "bold"))
        self.label_ngsinh_hv.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.ngsinh_hv = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ngsinh_hv.grid(row=4, column=1, padx=10, pady=5)

        # Giới tính
        self.label_gioitinh = Label(self.top_frame, text="Giới tính: ", font=("Arial", 10, "bold"))
        self.label_gioitinh.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_gioitinh_text = StringVar()
        self.gioitinh = Entry(self.top_frame, textvariable=self.entry_gioitinh_text, width=40, font=("Arial", 10))
        self.gioitinh.grid(row=5, column=1, padx=10, pady=5)

        # Nơi sinh
        self.label_noisinh = Label(self.top_frame, text="Nơi sinh: ", font=("Arial", 10, "bold"))
        self.label_noisinh.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_noisinh_text = StringVar()
        self.noisinh = Entry(self.top_frame, textvariable=self.entry_noisinh_text, width=40, font=("Arial", 10))
        self.noisinh.grid(row=6, column=1, padx=10, pady=5)

        # Mã lớp
        self.label_ma_lop = Label(self.top_frame, text="Mã Lớp: ", font=("Arial", 10, "bold"))
        self.label_ma_lop.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_lop_text = StringVar()
        self.ma_lop = Entry(self.top_frame, textvariable=self.entry_ma_lop_text, width=40, font=("Arial", 10))
        self.ma_lop.grid(row=7, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=20)

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
            self._root, columns=("MAHV", "HO", "TEN", "NGSINH", "GIOITINH", "NOISINH", "MALOP"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MAHV", text="Mã Học Viên")
        self._tree.heading("HO", text="Họ Học Viên")
        self._tree.heading("TEN", text="Tên Học Viên")
        self._tree.heading("NGSINH", text="Ngày sinh")
        self._tree.heading("GIOITINH", text="Giới tính")
        self._tree.heading("NOISINH", text="Nơi sinh")
        self._tree.heading("MALOP", text="Mã lớp")

        self._tree.column("MAHV", width=20, anchor="center")
        self._tree.column("HO", width=20, anchor="w")
        self._tree.column("TEN", width=20, anchor="w")
        self._tree.column("NGSINH", width=20, anchor="center")
        self._tree.column("GIOITINH", width=20, anchor="center")
        self._tree.column("NOISINH", width=40, anchor="w")
        self._tree.column("MALOP", width=20, anchor="center")

    #get
    def get_selected_item(self):
        """Trả về Mã Học Viên của item được chọn."""
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
            "MAHV": self.get_ma_hv(),
            "HO": self.get_ho_hv(),
            "TEN": self.get_ten_hv(),
            "NGSINH": self.get_ngsinh_hv(),
            "GIOITINH": self.get_gioitinh(),
            "NOISINH": self.get_noisinh(),
            "MALOP": self.get_ma_lop()
        }
        
    def get_ma_hv(self):
        return self.entry_ma_hv_text.get()
        
    def get_ho_hv(self):
        return self.entry_ho_hv_text.get()
        
    def get_ten_hv(self):
        return self.entry_ten_hv_text.get()
        
    def get_ngsinh_hv(self):
        return self.ngsinh_hv.get_date()
        
    def get_gioitinh(self):
        return self.entry_gioitinh_text.get()
        
    def get_noisinh(self):
        return self.entry_noisinh_text.get()
        
    def get_ma_lop(self):
        return self.entry_ma_lop_text.get()

    #set
    def set_ma_hv(self, ma_hv):
        self.entry_ma_hv_text.set(ma_hv)

    def set_ho_hv(self, ho_hv):
        self.entry_ho_hv_text.set(ho_hv)

    def set_ten_hv(self, ten_hv):
        self.entry_ten_hv_text.set(ten_hv)

    def set_ngsinh_hv(self, ngsinh_hv):
        self.ngsinh_hv.set_date(datetime.strptime(ngsinh_hv, "%Y-%m-%d %H:%M:%S").date())

    def set_gioitinh(self, gioitinh):
        self.entry_gioitinh_text.set(gioitinh)

    def set_noisinh(self, noisinh):
        self.entry_noisinh_text.set(noisinh)

    def set_ma_lop(self, ma_lop):
        self.entry_ma_lop_text.set(ma_lop)

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_hv.delete(0, END)
        self.ho_hv.delete(0, END)
        self.ten_hv.delete(0, END)
        self.ngsinh_hv.set_date(datetime.now().date())
        self.gioitinh.delete(0, END)
        self.noisinh.delete(0, END)
        self.ma_lop.delete(0, END)
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MAHV"], item["HO"], item["TEN"], item["NGSINH"], item["GIOITINH"], item["NOISINH"], item["MALOP"]))
        
    def showView(self):
        self._root.mainloop()