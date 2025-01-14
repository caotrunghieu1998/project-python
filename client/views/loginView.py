from tkinter import *
from tkinter import messagebox
from controllers.userController import UserController
from views.hocVienView import HocVienView

class LoginView:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if (LoginView._instance):
            return LoginView._instance
        LoginView._instance = LoginView()
        return LoginView._instance

    def __init__(self):
        self.tkRoot = Tk()
        self.userController = UserController.getInstance()
    
    def initView(self):
        root = self.tkRoot

        root.title("Đăng nhập")
        root.geometry("300x250")

        #Creating layout of login form
        Label(root, text="Hãy điền các thông tin cần thiết", width="300", bg="orange",fg="white").pack()

        #Email label and text entry box
        Label(root, text="Email *").place(x=20,y=40)
        self.inputEmail = StringVar(value="nguyenVanA@gmail.com")
        Entry(root, textvariable=self.inputEmail).place(x=90,y=42)  

        #password label and password entry box
        Label(root,text="Password *").place(x=20,y=80)  
        self.inputPassword = StringVar(value="12345678")
        Entry(root, textvariable=self.inputPassword, show='*').place(x=90,y=82)  
        #login button

        Button(root, text="Đăng nhập", width=10, height=1, bg="orange", command=self.login).place(x=105,y=130) 

    def showView(self):
        self.tkRoot.mainloop()

    def login(self):
        """Lấy thông tin email và password, và xử lý."""
        email = self.inputEmail.get()
        password = self.inputPassword.get()
        
        # Kiểm tra thông tin đầu vào (có thể mở rộng kiểm tra)
        if not email or not password:
            messagebox.showerror("Cảnh báo", "Hãy điền đầy đủ Email và Password!")
        else:
            user = self.userController.login(email, password)
            if (user):
                messagebox.showinfo("Thành công", f"Đăng nhập thành công, xin chào \"{user.NAME}\"")
                self.tkRoot.destroy()
                hocVienView = HocVienView.getInstance(user)
                hocVienView.initView()
                hocVienView.showView()
            else:
                messagebox.showerror("Thất bại", "Sai thông tin đăng nhập!")