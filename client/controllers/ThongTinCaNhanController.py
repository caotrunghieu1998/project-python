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
        self.runMain()

    def loadData(self):
        data = self.giaoVienModel.getData("GV01")
        self.thongTinCaNhanView.loadData(data)

    def runMain(self):
        print("runMain")
        self.loadData()
        self.thongTinCaNhanView.root.mainloop()

main = ThongTinCaNhanController.getInstance()
# main.runMain()