from tkinter import *

class Common:
    def center_window(self, root: Tk, width=800, height=600):
        # Lấy kích thước màn hình
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Lấy kích thước cửa sổ
        window_width = width
        window_height = height

        # Tính toán vị trí để căn giữa
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        # Đặt vị trí cửa sổ
        root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')