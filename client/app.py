# from views.loginView import LoginView

# if __name__ == '__main__':
#     userView = LoginView.getInstance()
#     userView.initView()
#     userView.showView()
    
    
from controllers.LopController import LopController

if __name__ == '__main__':
    c = LopController.getInstance()
    c.initView()
    c.showView()