
class GiaoVienController:
    _instance = None

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