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

from controllers.ThongTinCaNhanHocVienController import ThongTinCaNhanHocVienController
from models.ThongTinCaNhanHocVienModel import ThongTinCaNhanHocVienModel
from views.ThongTinCaNhanHocVienView import ThongTinCaNhanHocVienView

from controllers.KetQuaThiController import KetQuaThiController
from models.KetQuaThiModel import KetQuaThiModel
from views.KetQuaThiView import KetQuaThiView


class HocVienLoginController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (HocVienLoginController._instance):
            return HocVienLoginController._instance
        HocVienLoginController._instance = HocVienLoginController()
        return HocVienLoginController._instance

    def __init__(self, model: HocVienLoginModel, view: HocVienLoginView):
        self._model = model
        self._view = view
        
    def initItemView(self):
        self._view.btnProfile["command"] = self.goToProfileScreen
        self._view.btnKhoa["command"] = self.goToKhoaScreen
        self._view.btnHocVien["command"] = self.goToHocVienScreen
        self._view.btnLop["command"] = self.goToLopScreen
        self._view.btnKQThi["command"] = self.goToKetQuaThiScreen
        if self.commandBack:
            def _back():
                self._view.tkRoot.destroy()
                self.commandBack()

            self._view.btnDangXuat["command"] = _back
        
        self._data = self._model.get_data_by_id(self._view._hoc_vien[0]["MAHV"])
        self.load_data()
        
    def load_data(self):
        """Hiển thị danh sách"""

    def goToProfileScreen(self):
        self._view.tkRoot.destroy()
        root = Tk()
        m = ThongTinCaNhanHocVienModel()
        v = ThongTinCaNhanHocVienView(root, self._data)
        c = ThongTinCaNhanHocVienController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

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
        root = Tk()
        m = KetQuaThiModel()
        v = KetQuaThiView(root, self._data, "HOCVIEN")
        c = KetQuaThiController(m, v)
        c.initCommandButtonBack(self.back)
        v.showView()

    def initCommandButtonDangXuat(self, commandBack):
         self.commandBack = commandBack

    def back(self):
        self._view.reuse()
        self.initItemView()
        self._view.showView()