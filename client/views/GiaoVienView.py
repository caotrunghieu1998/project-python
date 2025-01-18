from tkinter import *

from controllers.GiaoVienController import GiaoVienController


class GiaoVienView:
    _instance = None
    giaoVienController = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienView._instance):
            return GiaoVienView._instance
        GiaoVienView._instance = GiaoVienView()
        return GiaoVienView._instance

    def __init__(self):
        # Check Login
        self.tkRoot = Tk()
        self.giaoVienController = GiaoVienController.getInstance()

    def initView(self, giaoVien):
        self.giaoVienController.giaoVien = giaoVien
        root = self.tkRoot

        root.title("Chức năng giáo viên")
        root.geometry("500x250")

        # Creating layout of login form
        Label(root, text=f"Xin chào giáo viên {giaoVien[0]["HOTEN"]}", width="300", bg="orange", fg="white").pack()

        btnProfile = Button(root, text="Thông tin cá nhân", command=self.giaoVienController.goToProfileScreen)
        btnProfile.place(x=5, y=30, height=50, width=243)

        btnKhoa = Button(root, text="Khoa", command=self.giaoVienController.goToKhoaScreen)
        btnKhoa.place(x=248, y=30, height=50, width=243)

        btnMonHoc = Button(root, text="Môn học", command=self.giaoVienController.goToMonHocScreen)
        btnMonHoc.place(x=5, y=80, height=50, width=243)

        btnLop = Button(root, text="Lớp", command=self.giaoVienController.goToClassScreen)
        btnLop.place(x=248, y=80, height=50, width=243)

        btnDiem = Button(root, text="Điểm", command=self.giaoVienController.goToScoreScreen)
        btnDiem.place(x=5, y=130, height=50, width=243)

        btnDangXuat = Button(root, text="Đăng xuất", command=self.giaoVienController.dangXuat)
        btnDangXuat.place(x=248, y=130, height=50, width=243)

    def showView(self):
        self.tkRoot.mainloop()