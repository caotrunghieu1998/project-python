from views.loginView import LoginView

if __name__ == '__main__':
    userView = LoginView.getInstance()
    userView.initView()
    userView.showView()