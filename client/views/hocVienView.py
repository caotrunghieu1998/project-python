from tkinter import *
from tkinter import messagebox
from models.userModel import *
from controllers.userController import UserController

class HocVienView:
    _instance = None
    
    @classmethod
    def getInstance(cls, user: User):
        if (HocVienView._instance):
            return HocVienView._instance
        HocVienView._instance = HocVienView(user)
        return HocVienView._instance
    
    def __init__(self, user: User):
        # Check Login
        self.tkRoot = Tk()
        self.user = user

    
    def initView(self):
        root = self.tkRoot

        root.title("Quản lý học viên")
        root.geometry("300x250")

        #Creating layout of login form
        Label(root, text="Hãy điền các thông tin cần thiết", width="300", bg="orange",fg="white").pack()


    def showView(self):
        self.tkRoot.mainloop()
