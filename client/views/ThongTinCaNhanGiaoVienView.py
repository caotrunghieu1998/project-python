from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class ThongTinCaNhanGiaoVienView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanGiaoVienView._instance):
            return ThongTinCaNhanGiaoVienView._instance
        ThongTinCaNhanGiaoVienView._instance = ThongTinCaNhanGiaoVienView()
        
        return ThongTinCaNhanGiaoVienView._instance

    def __init__(self, root: Tk, giao_vien):
        self._root = root
        self._giao_vien = giao_vien
        self._common = Common()
        self._common.center_window(root, 500, 500)
        self.initView()
    
    
    @property
    def giao_vien_param(self):
        return self._giao_vien
    
    def initView(self):
        root = self._root

        root.title("Thông tin giáo viên")
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
        self.labelTitle = Label(self.top_frame, text="Thông tin giáo viên", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã giáo viên
        self.label_ma_gv = Label(self.top_frame, text="Mã giáo viên: ", font=("Arial", 10, "bold"))
        self.label_ma_gv.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_gv_text = StringVar()
        self.ma_gv = Entry(self.top_frame, textvariable=self.entry_ma_gv_text, width=40, font=("Arial", 10))
        self.ma_gv.grid(row=1, column=1, padx=10, pady=5)

        # Họ tên giáo viên
        self.label_ho_ten = Label(self.top_frame, text="Họ tên: ", font=("Arial", 10, "bold"))
        self.label_ho_ten.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ho_ten_text = StringVar()
        self.ho_ten = Entry(self.top_frame, textvariable=self.entry_ho_ten_text, width=40, font=("Arial", 10))
        self.ho_ten.grid(row=2, column=1, padx=10, pady=5)
        
        #Học vị
        self.label_hoc_vi = Label(self.top_frame, text="Học vị: ", font=("Arial", 10, "bold"))
        self.label_hoc_vi.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_hoc_vi_text = StringVar()
        self.hoc_vi = Entry(self.top_frame, textvariable=self.entry_hoc_vi_text, width=40, font=("Arial", 10))
        self.hoc_vi.grid(row=3, column=1, padx=10, pady=5)
        
        #Học hàm
        self.label_hoc_ham = Label(self.top_frame, text="Học vị: ", font=("Arial", 10, "bold"))
        self.label_hoc_ham.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_hoc_ham_text = StringVar()
        self.hoc_ham = Entry(self.top_frame, textvariable=self.entry_hoc_ham_text, width=40, font=("Arial", 10))
        self.hoc_ham.grid(row=4, column=1, padx=10, pady=5)
        
        #Giới tính
        self.label_gioi_tinh = Label(self.top_frame, text="Giới tính: ", font=("Arial", 10, "bold"))
        self.label_gioi_tinh.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_gioi_tinh_text = StringVar()
        self.gioi_tinh = Entry(self.top_frame, textvariable=self.entry_gioi_tinh_text, width=40, font=("Arial", 10))
        self.gioi_tinh.grid(row=5, column=1, padx=10, pady=5)

        # Ngày sinh
        self.label_ngay_sinh = Label(self.top_frame, text="Ngày sinh: ", font=("Arial", 10, "bold"))
        self.label_ngay_sinh.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.ngay_sinh = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ngay_sinh.grid(row=6, column=1, padx=10, pady=5)

        # Ngày VL
        self.label_ngay_vl = Label(self.top_frame, text="Ngày VL: ", font=("Arial", 10, "bold"))
        self.label_ngay_vl.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.ngay_vl = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ngay_vl.grid(row=6, column=1, padx=10, pady=5)

        # Hệ số
        self.label_heso = Label(self.top_frame, text="Hệ số: ", font=("Arial", 10, "bold"))
        self.label_heso.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.entry_heso_text = StringVar()
        self.heso = Entry(self.top_frame, textvariable=self.entry_heso_text, width=40, font=("Arial", 10))
        self.heso.grid(row=8, column=1, padx=10, pady=5)

        # Mức lương
        self.label_muc_luong = Label(self.top_frame, text="Mức lương: ", font=("Arial", 10, "bold"))
        self.label_muc_luong.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.entry_muc_luong_text = StringVar()
        self.muc_luong = Entry(self.top_frame, textvariable=self.entry_muc_luong_text, width=40, font=("Arial", 10))
        self.muc_luong.grid(row=9, column=1, padx=10, pady=5)

        # Mã khoa
        self.label_ma_khoa = Label(self.top_frame, text="Mã khoa: ", font=("Arial", 10, "bold"))
        self.label_ma_khoa.grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_khoa_text = StringVar()
        self.ma_khoa = Entry(self.top_frame, textvariable=self.entry_ma_khoa_text, width=40, font=("Arial", 10))
        self.ma_khoa.grid(row=10, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=11, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=1, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=2, padx=10)

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "MAGV": self.get_ma_gv(),
            "HOTEN": self.get_ho_ten(),
            "HOCVI": self.get_hoc_vi(),
            "HOCHAM": self.get_hoc_ham(),
            "GIOITINH": self.get_gioi_tinh(),
            "NGSINH": self.get_ngay_sinh(),
            "NGVL": self.get_ngay_vl(),
            "HESO": self.get_heso(),
            "MUCLUONG": self.get_muc_luong(),
            "MAKHOA": self.get_ma_khoa(),
        }

    def set_input_values(self, item):
        """Lấy dữ liệu từ DB vào các ô nhập liệu."""
        self.set_ma_gv(str(item["MAGV"]))
        self.set_ho_ten(str(item["HOTEN"]))
        self.set_hoc_vi(str(item["HOCVI"]))
        self.set_hoc_ham(str(item["HOCHAM"]))
        self.set_gioi_tinh(str(item["GIOITINH"]))
        self.set_ngay_sinh(str(item["NGSINH"]))
        self.set_ngay_vl(str(item["NGVL"]))
        self.set_heso(str(item["HESO"]))
        self.set_muc_luong(str(item["MUCLUONG"]))
        self.set_ma_khoa(str(item["MAKHOA"]))
        
    def get_ma_gv(self):
        return self.entry_ma_gv_text.get()
    def get_ho_ten(self):
        return self.entry_ho_ten_text.get()
    def get_hoc_vi(self):
        return self.entry_hoc_vi_text.get()
    def get_hoc_ham(self):
        return self.entry_hoc_ham_text.get()
    def get_gioi_tinh(self):
        return self.entry_gioi_tinh_text.get()
    def get_ngay_sinh(self):
        return self.ngay_sinh.get_date()
    def get_ngay_vl(self):
        return self.ngay_vl.get_date()
    def get_heso(self):
        return self.entry_heso_text.get()
    def get_muc_luong(self):
        return self.entry_muc_luong_text.get()
    def get_ma_khoa(self):
        return self.entry_ma_khoa_text.get()

    #set
    def set_ma_gv(self, ma_hv):
        self.entry_ma_gv_text.set(ma_hv)

    def set_ho_ten(self, ma_hv):
        self.entry_ho_ten_text.set(ma_hv)

    def set_hoc_vi(self, ma_hv):
        self.entry_hoc_vi_text.set(ma_hv)

    def set_hoc_ham(self, ma_hv):
        self.entry_hoc_ham_text.set(ma_hv)

    def set_gioi_tinh(self, ma_hv):
        self.entry_gioi_tinh_text.set(ma_hv)


    def set_ngay_sinh(self, ngay_sinh):
        self.ngay_sinh.set_date(datetime.strptime(ngay_sinh, "%Y-%m-%d %H:%M:%S").date())
        
    def set_ngay_vl(self, ngay_vl):
        self.ngay_vl.set_date(datetime.strptime(ngay_vl, "%Y-%m-%d %H:%M:%S").date())

    def set_heso(self, heso):
        self.entry_heso_text.set(heso)
        
    def set_muc_luong(self, muc_luong):
        self.entry_muc_luong_text.set(muc_luong)
        
    def set_ma_khoa(self, ma_khoa):
        self.entry_ma_khoa_text.set(ma_khoa)


    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_gv.delete(0, END)
        self.ho_ten.delete(0, END)
        self.hoc_vi.delete(0, END)
        self.hoc_ham.delete(0, END)
        self.gioi_tinh.delete(0, END)
        self.ngay_sinh.set_date(datetime.now().date())
        self.ngay_vl.set_date(datetime.now().date())
        self.heso.delete(0, END)
        self.muc_luong.delete(0, END)
        self.ma_khoa.delete(0, END)
        
    def showView(self):
        self._root.mainloop()