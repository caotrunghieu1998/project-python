from models.GiaoVienModel import GiaoVienModel
from views.GiaoVienView import GiaoVienView

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

from controllers.ThongTinCaNhanGiaoVienController import ThongTinCaNhanGiaoVienController
from models.ThongTinCaNhanGiaoVienModel import ThongTinCaNhanGiaoVienModel
from views.ThongTinCaNhanGiaoVienView import ThongTinCaNhanGiaoVienView

from controllers.KetQuaThiController import KetQuaThiController
from models.KetQuaThiModel import KetQuaThiModel
from views.KetQuaThiView import KetQuaThiView

from controllers.MonHocController import MonHocController
from models.MonHocModel import MonHocModel
from views.MonHocView import MonHocView


class GiaoVienController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (GiaoVienController._instance):
            return GiaoVienController._instance
        GiaoVienController._instance = GiaoVienController()
        return GiaoVienController._instance

    def __init__(self, model: GiaoVienModel, view: GiaoVienView):
        self._model = model
        self._view = view
        
    def initItemView(self):
        self._view.btnProfile["command"] = self.goToProfileScreen
        self._view.btnKhoa["command"] = self.goToKhoaScreen
        self._view.btnHocVien["command"] = self.goToHocVienScreen
        self._view.btnGiangDay["command"] = self.goToGiangDayScreen
        self._view.btnMonHoc["command"] = self.goToMonHocScreen
        self._view.btnLop["command"] = self.goToLopScreen
        self._view.btnKQThi["command"] = self.goToKetQuaThiScreen
        if self.commandBack:
            def _back():
                self._view.tkRoot.destroy()
                self.commandBack()

            self._view.btnDangXuat["command"] = _back
        
        self.load_data()
        
    def load_data(self):
        """Hiển thị danh sách"""

    def goToProfileScreen(self):
        self._view.tkRoot.destroy()
        data = self._model.get_data_by_id(self._view._giao_vien[0]["MAGV"])
        root = Tk()
        m = ThongTinCaNhanGiaoVienModel()
        v = ThongTinCaNhanGiaoVienView(root, data)
        c = ThongTinCaNhanGiaoVienController(m, v)
        c.initCommandButtonBack(self.back)

    def goToKhoaScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = KhoaModel()
        v = KhoaView(root)
        c = KhoaController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def goToHocVienScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = HocVienModel()
        v = HocVienView(root)
        c = HocVienController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def goToGiangDayScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = GiangDayModel()
        v = GiangDayView(root)
        c = GiangDayController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def goToMonHocScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = MonHocModel()
        v = MonHocView(root)
        c = MonHocController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def goToLopScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = LopModel()
        v = LopView(root)
        c = LopController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def goToKetQuaThiScreen(self):
        self._view.tkRoot.destroy()
        ma_gv = self._view._giao_vien[0]["MAGV"]
        root = Tk()
        m = KetQuaThiModel()
        v = KetQuaThiView(root, ma_gv, "GIAOVIEN")
        c = KetQuaThiController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()
    
    def back(self):
        self._view.reuse()
        self.initItemView()
        self._view.showView()

    def initCommandButtonDangXuat(self, commandBack):
         self.commandBack = commandBack