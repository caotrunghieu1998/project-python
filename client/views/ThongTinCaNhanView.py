import tkinter as tk

from client.models.GiaoVienModel import GiaoVienModel


class ThongTinCaNhanView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanView._instance):
            return ThongTinCaNhanView._instance
        ThongTinCaNhanView._instance = ThongTinCaNhanView()
        return ThongTinCaNhanView._instance

    def __init__(self):
        self.root = tk.Tk()
        self.setupView()

    def loadData(self, data):
        print("ThongTinCaNhanView.loadData()")
        for row in data:
            for field_name in row:
                self.entries[field_name].insert(0, row[field_name])

    def setupView(self):
        root = self.root
        root.geometry("450x400")

        self.entries = {}
        self.fields = [
            ("Mã Giáo Viên", "MAGV"),
            ("Họ và tên", "HOTEN"),
            ("Học vị", "HOCVI"),
            ("Học hàm", "HOCHAM"),
            ("Giới tính", "GIOITINH"),
            ("Ngày Sinh", "NGSINH"),
            ("Ngày Vào Làm", "NGVL"),
            ("Hệ số", "HESO"),
            ("Mức lương", "MUCLUONG"),
            ("Mã Khoa", "MAKHOA")
        ]

        for i, (label_text, field_name) in enumerate(self.fields):
            # Label
            tk.Label(root, text=label_text).grid(row=i, column=0, sticky=tk.W, pady=5)
            # Entry
            entry = tk.Entry(root, width=50)
            entry.grid(row=i, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
            self.entries[field_name] = entry

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=len(self.fields), column=0, columnspan=2, pady=20)

        tk.Button(button_frame, text="Cập nhật", command=self.capNhat).pack(side=tk.LEFT, padx=5)

    def capNhat(self):
        print("ThongTinCaNhanView.capNhat()")
        data = (
            self.entries["MAGV"].get(),
            self.entries["HOTEN"].get(),
            self.entries["HOCVI"].get(),
            self.entries["HOCHAM"].get(),
            self.entries["GIOITINH"].get(),
            self.entries["NGSINH"].get(),
            self.entries["NGVL"].get(),
            float(self.entries["HESO"].get() or 0),
            float(self.entries["MUCLUONG"].get() or 0),
            self.entries["MAKHOA"].get()
        )
        query=(f"UPDATE giaovien SET HOTEN = '{data[1]}', "
               f"HOCVI = '{data[2]}', HOCHAM = '{data[3]}', GIOITINH = '{data[4]}', "
               f"NGSINH = '{data[5]}', NGVL = '{data[6]}', HESO = '{data[7]}', "
               f"MUCLUONG = '{data[8]}', MAKHOA = '{data[9]}' "
               f"WHERE maGV = '{data[0]}'")

        GiaoVienModel.getInstance().update(query)




