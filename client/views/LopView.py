import tkinter as tk
from tkinter import ttk
from controllers.LopController import LopController

class LopView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (LopView._instance):
            return LopView._instance
        LopView._instance = LopView()
        return LopView._instance

    def __init__(self):
        
        self.tkRoot = tk.Tk()
        self._lopController = LopController.getInstance()

    def initView(self):
        root = self.tkRoot

        root.title("Danh sách lóp")
        root.geometry("800x600")

        # Tạo frame trên cùng để chứa nút và ô nhập liệu
        top_frame = tk.Frame(root)
        top_frame.pack(fill="x", padx=10, pady=10)
        
        # Nhãn và ô nhập liệu
        self.entry_ma_khoa = tk.Entry(top_frame, width=10)
        self.entry_ma_khoa.grid(row=0, column=1, padx=5)
        tk.Label(top_frame, text="Mã Khoa:").grid(row=0, column=0)

        self.entry_ten_khoa = tk.Entry(top_frame, width=30)
        self.entry_ten_khoa.grid(row=0, column=3, padx=5)
        tk.Label(top_frame, text="Tên Khoa:").grid(row=0, column=2)

        self.entry_ngay_tl = tk.Entry(top_frame, width=15)
        self.entry_ngay_tl.grid(row=0, column=5, padx=5)
        tk.Label(top_frame, text="Ngày TL:").grid(row=0, column=4)

        self.entry_trg_khoa = tk.Entry(top_frame, width=20)
        self.entry_trg_khoa.grid(row=0, column=7, padx=5)
        tk.Label(top_frame, text="Trưởng Khoa:").grid(row=0, column=6)

        # Nút thêm, sửa, xóa
        tk.Button(top_frame, text="Thêm", command=self._lopController.add_item).grid(row=1, column=1, pady=10)
        tk.Button(top_frame, text="Sửa", command=self._lopController.edit_item).grid(row=1, column=3, pady=10)
        tk.Button(top_frame, text="Xóa", command=self._lopController.delete_item).grid(row=1, column=5, pady=10)

        # Tạo Treeview
        self.tree = ttk.Treeview(root, columns=("MAKHOA", "TENKHOA", "NGTLAP", "TRGKHOA"), show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Định nghĩa tiêu đề các cột
        self.tree.heading("MAKHOA", text="Mã Khoa")
        self.tree.heading("TENKHOA", text="Tên Khoa")
        self.tree.heading("NGTLAP", text="Ngày Thành Lập")
        self.tree.heading("TRGKHOA", text="Trưởng Khoa")

        # Định nghĩa độ rộng cho các cột
        self.tree.column("MAKHOA", width=100, anchor="center")
        self.tree.column("TENKHOA", width=200, anchor="w")
        self.tree.column("NGTLAP", width=150, anchor="center")
        self.tree.column("TRGKHOA", width=150, anchor="w")

        # Thêm dữ liệu vào Treeview
        self.refresh_treeview()

    def refresh_treeview(self):
        """Cập nhật Treeview với dữ liệu hiện tại."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in self.data:
            self.tree.insert("", tk.END, values=(item["MAKHOA"], item["TENKHOA"], item["NGTLAP"], item["TRGKHOA"]))
    
    def showView(self):
        self.tkRoot.mainloop()