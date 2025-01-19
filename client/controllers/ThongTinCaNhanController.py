from models.GiaoVienModel import GiaoVienModel
from models.HocVienModel import HocVienModel
from views.ThongTinCaNhanView import ThongTinCaNhanView

class ThongTinCaNhanController:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (ThongTinCaNhanController._instance):
            return ThongTinCaNhanController._instance
        ThongTinCaNhanController._instance = ThongTinCaNhanController()
        return ThongTinCaNhanController._instance

    def __init__(self):
        self.thongTinCaNhanView = ThongTinCaNhanView.getInstance()
        self.giaoVienModel = GiaoVienModel()
        self.hocVienModel = HocVienModel()

    def loadData(self, ma, type):
        if type == 'HOCVIEN':
            data = self.hocVienModel.login(ma)
            self.thongTinCaNhanView.loadData(data)
        elif type == 'GIAOVIEN':
            data = self.giaoVienModel.login(ma)
            self.thongTinCaNhanView.loadData(data)

    def show(self):
        self.thongTinCaNhanView.root.mainloop()

# main.runMain()