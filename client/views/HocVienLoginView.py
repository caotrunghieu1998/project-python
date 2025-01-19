from tkinter import *

from common.common import Common

class HocVienLoginView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (HocVienLoginView._instance):
            return HocVienLoginView._instance
        HocVienLoginView._instance = HocVienLoginView()
        return HocVienLoginView._instance

    def __init__(self, root: Tk, hoc_vien):
        self.tkRoot = root
        self._hoc_vien = hoc_vien
        self._common = Common()
        self._common.center_window(self.tkRoot, 610, 300)
        self.initView()

    def initView(self):
        root = self.tkRoot

        root.title("Chức năng học viên")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Header
        self.labelTitle = Label(self.top_frame, text="Xin chào học viên {0} {1}".format(self._hoc_vien[0]["HO"], self._hoc_vien[0]["TEN"]), font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tạo button_frame
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=1, column=0, columnspan=2, pady=20)

        # Hàng 1: "Thông tin cá nhân", "Đăng xuất"
        self.btnProfile = Button(self.button_frame, text="Thông tin cá nhân", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnProfile.grid(row=0, column=0, padx=10, pady=5)

        self.btnDangXuat = Button(self.button_frame, text="Đăng xuất", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnDangXuat.grid(row=0, column=1, padx=10, pady=5)

        # Hàng 2: "Khoa", "Học Viên"
        self.btnKhoa = Button(self.button_frame, text="Khoa", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnKhoa.grid(row=1, column=0, padx=10, pady=5)

        self.btnHocVien = Button(self.button_frame, text="Học Viên", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnHocVien.grid(row=1, column=1, padx=10, pady=5)

        # Hàng 3: "Môn Học", "Lớp", "Điểm"
        self.btnMonHoc = Button(self.button_frame, text="Môn Học", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnMonHoc.grid(row=2, column=0, padx=10, pady=5)

        self.btnLop = Button(self.button_frame, text="Lớp", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnLop.grid(row=2, column=1, padx=10, pady=5)

        self.btnDiem = Button(self.button_frame, text="Điểm", font=("Arial", 10), width=20, relief="raised", bd=2)
        self.btnDiem.grid(row=2, column=2, padx=10, pady=5)

    def showView(self):
        self.tkRoot.mainloop()