from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class ThongTinCaNhanHocVienView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanHocVienView._instance):
            return ThongTinCaNhanHocVienView._instance
        ThongTinCaNhanHocVienView._instance = ThongTinCaNhanHocVienView()
        
        return ThongTinCaNhanHocVienView._instance

    def __init__(self, root: Tk, hoc_vien):
        self._root = root
        self._hoc_vien = hoc_vien
        self._common = Common()
        self._common.center_window(root, 500, 350)
        self.initView()
    
    @property
    def hoc_vien_param(self):
        return self._hoc_vien
    
    def initView(self):
        root = self._root

        root.title("Thông tin học viên")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        self.top_frame.grid_columnconfigure(4, weight=4)
        
        self.header()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Thông tin học viên", font=("Arial", 20, "bold"))
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

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=1, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=2, padx=10)


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

    def set_input_values(self, item):
        """Lấy dữ liệu từ DB vào các ô nhập liệu."""
        self.set_ma_hv(str(item["MAHV"]))
        self.set_ho_hv(str(item["HO"]))
        self.set_ten_hv(str(item["TEN"]))
        self.set_ngsinh_hv(str(item["NGSINH"]))
        self.set_gioitinh(str(item["GIOITINH"]))
        self.set_noisinh(str(item["NOISINH"]))
        self.set_ma_lop(str(item["MALOP"]))
        
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
        
    def showView(self):
        self._root.mainloop()