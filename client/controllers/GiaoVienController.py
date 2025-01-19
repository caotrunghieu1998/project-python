from controllers.ThongTinCaNhanController import ThongTinCaNhanController
from models.GiaoVienModel import GiaoVienModel
from views.GiaoVienView import GiaoVienView

from tkinter import *
from controllers.LopController import LopController
from models.LopModel import LopModel
from views.lopView import LopView


class GiaoVienController:
    _instance = None
    giaoVien = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienController._instance):
            return GiaoVienController._instance
        GiaoVienController._instance = GiaoVienController()
        return GiaoVienController._instance

    def __init__(self, model: GiaoVienModel, view: GiaoVienView):
        self._model = model
        self._view = view
        
        self.load_data()
        
    def load_data(self):
        """Hiển thị danh sách"""

    def goToProfileScreen(self, maGV):
        gv = self._model.getData(maGV)
        ThongTinCaNhanController.getInstance().loadData(gv[0]["MAGV"])

    def goToKhoaScreen(self):
        print("Khoa")

    def goToMonHocScreen(self):
        print("Mon Hoc")

    def goToClassScreen(self):
        pass

    def goToScoreScreen(self):
        print("Diem")

    def dangXuat(self):
        print("Dang xuat")