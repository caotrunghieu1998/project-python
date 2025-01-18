from client.controllers.ThongTinCaNhanController import ThongTinCaNhanController


class GiaoVienController:
    _instance = None
    giaoVien = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienController._instance):
            return GiaoVienController._instance
        GiaoVienController._instance = GiaoVienController()
        return GiaoVienController._instance

    def __init__(self):
        pass

    def goToProfileScreen(self):
        print("GiaoVienController.goToProfileScreen()")
        ThongTinCaNhanController.getInstance().loadData(self.giaoVien[0]["MAGV"])

    def goToKhoaScreen(self):
        print("Khoa")

    def goToMonHocScreen(self):
        print("Mon Hoc")

    def goToClassScreen(self):
        print("Lop")

    def goToScoreScreen(self):
        print("Diem")

    def dangXuat(self):
        print("Dang xuat")