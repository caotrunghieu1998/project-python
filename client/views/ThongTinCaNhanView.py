import tkinter as tk

from client.models.GiaoVienModel import GiaoVienModel
from client.models.connectDB import ConnectDB


class ThongTinCaNhanView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanView._instance):
            return ThongTinCaNhanView._instance
        ThongTinCaNhanView._instance = ThongTinCaNhanView()
        return ThongTinCaNhanView._instance

    def __init__(self):
        self.tkRoot = tk.Tk()

    def setupView(self):
        root = self.tkRoot
        root.geometry("500x350")

        lbMaGv = tk.Label(root, text="Ma Giao Vien").place(x=5, y=5)
        lbHoTen = tk.Label(root, text="Ho va ten").place(x=5, y=35)
        lbHocVi = tk.Label(root, text="Hoc vi").place(x=5, y=65)
        lbHocHam = tk.Label(root, text="Hoc ham").place(x=5, y=95)
        lbGioiTinh = tk.Label(root, text="Gioi tinh").place(x=5, y=125)
        lbNgSinh = tk.Label(root, text="Ngay Sinh").place(x=5, y=155)
        lbNgVL = tk.Label(root, text="Ngay Vao Lam").place(x=5, y=185)
        lbHeSo = tk.Label(root, text="He so").place(x=5, y=215)
        lbMucLuong = tk.Label(root, text="Muc luong").place(x=5, y=245)
        lbMaKhoa = tk.Label(root, text="Ma Khoa").place(x=5, y=275)

        self.etMaGv = tk.Entry(root, width=60)
        self.etMaGv.place(x=100, y=5)

        self.etHoTen = tk.Entry(root, text="Ho va ten", width=60)
        self.etHoTen.place(x=100, y=35)

        self.etHocVi = tk.Entry(root, text="Hoc vi", width=60)
        self.etHocVi.place(x=100, y=65)

        self.etHocHam = tk.Entry(root, text="Hoc ham", width=60)
        self.etHocHam.place(x=100, y=95)

        self.etGioiTinh = tk.Entry(root, text="Gioi tinh", width=60)
        self.etGioiTinh.place(x=100, y=125)

        self.etNgSinh = tk.Entry(root, text="Ngay Sinh", width=60)
        self.etNgSinh.place(x=100, y=155)

        self.etNgVL = tk.Entry(root, text="Ngay Vao Lam", width=60)
        self.etNgVL.place(x=100, y=185)

        self.etHeSo = tk.Entry(root, text="He so", width=60)
        self.etHeSo.place(x=100, y=215)

        self.etMucLuong = tk.Entry(root, text="Muc luong", width=60)
        self.etMucLuong.place(x=100, y=245)

        self.etbMaKhoa = tk.Entry(root, text="Ma Khoa", width=60)
        self.etbMaKhoa.place(x=100, y=275)

        self.capNhatBtn = tk.Button(root, text="Cap nhat")
        self.capNhatBtn.place(x=100, y=305)

        self.initData()

        root.mainloop()

    def initData(self):
        self.giaoVien = GiaoVienModel()
        self.giaoVien.maGV = "query xong cho data vao"

        self.etMaGv.insert(0, self.giaoVien.maGV)
        pass


ThongTinCaNhanView.getInstance().setupView()