from client.models.GiaoVienModel import GiaoVienModel
from client.views.ThongTinCaNhanView import ThongTinCaNhanView

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

    def loadData(self, MAGV):
        data = self.giaoVienModel.getData(MAGV)
        self.thongTinCaNhanView.loadData(data)

    def show(self):
        self.thongTinCaNhanView.root.mainloop()

# main.runMain()