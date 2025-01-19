from controllers.ThongTinCaNhanController import ThongTinCaNhanController
from models.HocVienLoginModel import HocVienLoginModel
from views.HocVienLoginView import HocVienLoginView

from tkinter import *
from controllers.LopController import LopController
from models.LopModel import LopModel
from views.lopView import LopView

from controllers.HocVienController import HocVienController
from models.HocVienModel import HocVienModel
from views.HocVienView import HocVienView

from controllers.KhoaController import KhoaController
from models.KhoaModel import KhoaModel
from views.KhoaView import KhoaView

from controllers.GiangDayController import GiangDayController
from models.GiangDayModel import GiangDayModel
from views.GiangDayView import GiangDayView


class HocVienLoginController:
    _instance = None
    giaoVien = None

    @classmethod
    def getInstance(cls):
        if (HocVienLoginController._instance):
            return HocVienLoginController._instance
        HocVienLoginController._instance = HocVienLoginController()
        return HocVienLoginController._instance

    def __init__(self, model: HocVienLoginModel, view: HocVienLoginView):
        self._model = model
        self._view = view
        self._view.btnProfile["command"] = self.goToProfileScreen
        self._view.btnDangXuat["command"] = self.goToDangXuatScreen
        self._view.btnKhoa["command"] = self.goToKhoaScreen
        self._view.btnHocVien["command"] = self.goToHocVienScreen
        self._view.btnMonHoc["command"] = self.goToMonHocScreen
        self._view.btnLop["command"] = self.goToLopScreen
        self._view.btnDiem["command"] = self.goToDiemScreen
        
        self.load_data()
        
    def load_data(self):
        """Hiển thị danh sách"""

    def goToProfileScreen(self, maGV):
        gv = self._model.login(maGV)
        ThongTinCaNhanController.getInstance().loadData(gv[0]["MAHV"])

    def goToDangXuatScreen(self):
        pass

    def goToKhoaScreen(self):
        root = Tk()
        m = KhoaModel()
        v = KhoaView(root)
        c = KhoaController(m, v)
        v.showView()

    def goToHocVienScreen(self):
        root = Tk()
        m = HocVienModel()
        v = HocVienView(root)
        c = HocVienController(m, v)
        v.showView()

    def goToMonHocScreen(self):
        pass

    def goToLopScreen(self):
        root = Tk()
        m = LopModel()
        v = LopView(root)
        c = LopController(m, v)
        v.showView()

    def goToDiemScreen(self):
        pass