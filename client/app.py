from views.loginView import LoginView

if __name__ == '__main__':
    userView = LoginView.getInstance()
    userView.initView()
    userView.showView()
    
from tkinter import *

from controllers.LopController import LopController
from models.LopModel import LopModel
from views.lopView import LopView

# if __name__ == '__main__':
#     root = Tk()
#     m = LopModel()
#     v = LopView(root)
#     c = LopController(m, v)
#
#     root.mainloop()