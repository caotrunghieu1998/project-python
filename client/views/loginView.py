from tkinter import *
from tkinter import messagebox
from controllers.userController import UserController

from controllers.GiaoVienController import GiaoVienController
from models.GiaoVienModel import GiaoVienModel
from views.GiaoVienView import GiaoVienView

from controllers.HocVienLoginController import HocVienLoginController
from models.HocVienLoginModel import HocVienLoginModel
from views.HocVienLoginView import HocVienLoginView

from common.common import Common


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
        self._common = Common()
        self._common.center_window(self.tkRoot, 500, 300)
    
    def initView(self):
        root = self.tkRoot

        root.title("Đăng nhập")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        #Creating layout of login form
        Label(root, text="Hãy điền các thông tin cần thiết", width="300", bg="orange",fg="white").pack()
        
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Đăng Nhập", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Tên đăng nhập
        self.label_inputEmail = Label(self.top_frame, text="Tên đăng nhập *: ", font=("Arial", 10, "bold"))
        self.label_inputEmail.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_inputEmail_text = StringVar(value="GV07 or K1101")
        self.inputEmail = Entry(self.top_frame, textvariable=self.entry_inputEmail_text, width=40, font=("Arial", 10))
        self.inputEmail.grid(row=1, column=1, padx=10, pady=5)

        # Mật khẩu
        self.label_inputPassword = Label(self.top_frame, text="Mật khẩu *: ", font=("Arial", 10, "bold"))
        self.label_inputPassword.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_inputPassword_text = StringVar()
        self.inputPassword = Entry(self.top_frame, textvariable=self.entry_inputPassword_text, width=40, font=("Arial", 10), show='*')
        self.inputPassword.grid(row=2, column=1, padx=10, pady=5)
        
        #login bằng giáo viên
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Đăng nhập Giáo Viên", font=("Arial", 10), width=20, relief="raised", bd=2, command=self.loginGiaoVien)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        #login bằng học viên
        self.buttonRefresh = Button(self.button_frame, text="Đăng nhập Học Viên", font=("Arial", 10), width=20, relief="raised", bd=2, command=self.loginHocVien)
        self.buttonRefresh.grid(row=0, column=1, padx=10)

    def showView(self):
        self.tkRoot.mainloop()

    def loginGiaoVien(self):
        """Lấy thông tin email và password, và xử lý."""
        email = self.inputEmail.get()
        password = self.inputPassword.get()
        
        # Kiểm tra thông tin đầu vào (có thể mở rộng kiểm tra)
        if not email or not password:
            messagebox.showerror("Cảnh báo", "Hãy điền đầy đủ Email và Password!")
        else:
            user = GiaoVienModel.getInstance().login(email)
            if (user):
                # messagebox.showinfo("Thành công", f"Đăng nhập thành công, xin chào \"{user[0]["MAGV"]}\"")
                self.tkRoot.destroy()
                root = Tk()
                m = GiaoVienModel()
                v = GiaoVienView(root, user)
                c = GiaoVienController(m, v)
                v.showView()
            else:
                messagebox.showerror("Thất bại", "Tài khoản hoặc mật khẩu giáo viên không chính xác")

    def loginHocVien(self):
        """Lấy thông tin email và password, và xử lý."""
        email = self.inputEmail.get()
        password = self.inputPassword.get()
        
        # Kiểm tra thông tin đầu vào (có thể mở rộng kiểm tra)
        if not email or not password:
            messagebox.showerror("Cảnh báo", "Hãy điền đầy đủ Email và Password!")
        else:
            user = HocVienLoginModel.getInstance().login(email)
            if (user):
                # messagebox.showinfo("Thành công", f"Đăng nhập thành công, xin chào \"{user[0]["MAHV"]}\"")
                self.tkRoot.destroy()
                root = Tk()
                m = HocVienLoginModel()
                v = HocVienLoginView(root, user)
                c = HocVienLoginController(m, v)
                v.showView()
            else:
                messagebox.showerror("Thất bại", "Tài khoản hoặc mật khẩu học viên không chính xác")