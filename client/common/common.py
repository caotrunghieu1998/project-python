from client.views.hocVienView import HocVienView

class Common:
    @staticmethod
    def goToHocVienView(currentScreenRoot, user):
        currentScreenRoot.destroy()
        hocVienView = HocVienView.getInstance(user)
        hocVienView.initView()
        hocVienView.showView()