from tkinter import *

from common.common import Common

class GiaoVienView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienView._instance):
            return GiaoVienView._instance
        GiaoVienView._instance = GiaoVienView()
        return GiaoVienView._instance

    def __init__(self, root: Tk, giao_vien):
        self.tkRoot = root
        self._common = Common()
        self._giao_vien = giao_vien
        self._common.center_window(self.tkRoot, 610, 300)
        self.initView()

    def initView(self):
        root = self.tkRoot

        root.title("Chức năng giáo viên")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Header
        self.labelTitle = Label(self.top_frame, text="Xin chào giáo viên {0}".format(self._giao_vien[0]["HOTEN"]), font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tạo button_frame
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=1, column=0, columnspan=2, pady=20)

        # Hàng 1: "Thông tin cá nhân", "Đăng xuất"
        self.btnProfile = Button(self.button_frame, text="Thông tin cá nhân", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnProfile.grid(row=0, column=0, padx=10, pady=5)

        self.btnDangXuat = Button(self.button_frame, text="Đăng xuất", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnDangXuat.grid(row=0, column=1, padx=10, pady=5)

        # Hàng 2: "Khoa", "Học Viên", "Giảng Dạy"
        self.btnKhoa = Button(self.button_frame, text="Khoa", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnKhoa.grid(row=1, column=0, padx=10, pady=5)

        self.btnHocVien = Button(self.button_frame, text="Học Viên", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnHocVien.grid(row=1, column=1, padx=10, pady=5)

        self.btnGiangDay = Button(self.button_frame, text="Giảng Dạy", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnGiangDay.grid(row=1, column=2, padx=10, pady=5)

        # Hàng 3: "Môn Học", "Lớp", "Điểm"
        self.btnMonHoc = Button(self.button_frame, text="Môn Học", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnMonHoc.grid(row=2, column=0, padx=10, pady=5)

        self.btnLop = Button(self.button_frame, text="Lớp", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnLop.grid(row=2, column=1, padx=10, pady=5)

        self.btnKQThi = Button(self.button_frame, text="Kết quả thi HV", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnKQThi.grid(row=2, column=2, padx=10, pady=5)

    def showView(self):
        self.tkRoot.mainloop()