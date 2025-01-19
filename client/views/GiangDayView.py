from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class GiangDayView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (GiangDayView._instance):
            return GiangDayView._instance
        GiangDayView._instance = GiangDayView()
        
        return GiangDayView._instance

    def __init__(self, root: Tk):
        self._root = root
        self._tree = ttk.Treeview(None)
        self._common = Common()
        self._common.center_window(root)
        self.initView()
        
    @property
    def tree(self):
        return self._tree
    
    def initView(self):
        root = self._root

        root.title("Danh sách khoa")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        
        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Danh sách giảng dạy", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã lớp
        self.label_ma_lop = Label(self.top_frame, text="Mã lớp: ", font=("Arial", 10, "bold"))
        self.label_ma_lop.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_lop_text = StringVar()
        self.ma_lop = Entry(self.top_frame, textvariable=self.entry_ma_lop_text, width=40, font=("Arial", 10))
        self.ma_lop.grid(row=1, column=1, padx=10, pady=5)

        # Mã môn học
        self.label_ma_mh = Label(self.top_frame, text="Mã môn học: ", font=("Arial", 10, "bold"))
        self.label_ma_mh.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_mh_text = StringVar()
        self.ma_mh = Entry(self.top_frame, textvariable=self.entry_ma_mh_text, width=40, font=("Arial", 10))
        self.ma_mh.grid(row=2, column=1, padx=10, pady=5)

        # Mã giáo viên
        self.label_ma_gv = Label(self.top_frame, text="Mã giáo viên: ", font=("Arial", 10, "bold"))
        self.label_ma_gv.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_gv_text = StringVar()
        self.ma_gv = Entry(self.top_frame, textvariable=self.entry_ma_gv_text, width=40, font=("Arial", 10))
        self.ma_gv.grid(row=3, column=1, padx=10, pady=5)
        
        # Học kỳ
        self.label_hoc_ky = Label(self.top_frame, text="Học kỳ: ", font=("Arial", 10, "bold"))
        self.label_hoc_ky.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_hoc_ky_text = StringVar()
        self.hoc_ky = Entry(self.top_frame, textvariable=self.entry_hoc_ky_text, width=40, font=("Arial", 10))
        self.hoc_ky.grid(row=4, column=1, padx=10, pady=5)
        
        # Năm
        self.label_nam = Label(self.top_frame, text="Năm: ", font=("Arial", 10, "bold"))
        self.label_nam.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_nam_text = StringVar()
        self.nam = Entry(self.top_frame, textvariable=self.entry_nam_text, width=40, font=("Arial", 10))
        self.nam.grid(row=5, column=1, padx=10, pady=5)

        # Từ ngày
        self.label_tu_ngay = Label(self.top_frame, text="Từ ngày: ", font=("Arial", 10, "bold"))
        self.label_tu_ngay.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.tu_ngay = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.tu_ngay.grid(row=6, column=1, padx=10, pady=5)

        # Đến ngày
        self.label_den_ngay = Label(self.top_frame, text="Đến ngày: ", font=("Arial", 10, "bold"))
        self.label_den_ngay.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.den_ngay = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.den_ngay.grid(row=7, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonAdd = Button(self.button_frame, text="Thêm", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonAdd.grid(row=0, column=1, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=2, padx=10)

        self.buttonRemove = Button(self.button_frame, text="Xoá", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRemove.grid(row=0, column=3, padx=10)

        self.buttonBack = Button(self.button_frame, text="Trở về", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonBack.grid(row=0, column=4, padx=10)

    def body(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self._root, columns=("MALOP", "MAMH", "MAGV", "HOCKY", "NAM", "TUNGAY", "DENNGAY"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MALOP", text="Mã lớp")
        self._tree.heading("MAMH", text="Mã môn học")
        self._tree.heading("MAGV", text="Mã giáo viên")
        self._tree.heading("HOCKY", text="Học kỳ")
        self._tree.heading("NAM", text="Năm")
        self._tree.heading("TUNGAY", text="Từ ngày")
        self._tree.heading("DENNGAY", text="Đến ngày")

        self._tree.column("MALOP", width=20, anchor="center")
        self._tree.column("MAMH", width=20, anchor="center")
        self._tree.column("MAGV", width=20, anchor="center")
        self._tree.column("HOCKY", width=20, anchor="center")
        self._tree.column("NAM", width=20, anchor="center")
        self._tree.column("TUNGAY", width=20, anchor="w")
        self._tree.column("DENNGAY", width=20, anchor="w")

    #get
    def get_selected_item(self):
        """Trả về của item được chọn."""
        selected_items = self._tree.selection()
        
        if selected_items:  
            first_item = selected_items[0]  
            values = self._tree.item(first_item, "values")  
            return values
        else:
            return None

    def get_input_values(self):
        """Lấy dữ liệu từ các ô nhập liệu."""
        return {
            "MALOP": self.get_ma_lop(),
            "MAMH": self.get_ma_mh(),
            "MAGV": self.get_ma_gv(),
            "HOCKY": self.get_hoc_ky(),
            "NAM": self.get_nam(),
            "TUNGAY": self.get_tu_ngay(),
            "DENNGAY": self.get_den_ngay(),
        }
        
    def get_ma_lop(self):
        return self.entry_ma_lop_text.get()
        
    def get_ma_mh(self):
        return self.entry_ma_mh_text.get()
        
    def get_ma_gv(self):
        return self.entry_ma_gv_text.get()
        
    def get_hoc_ky(self):
        return self.entry_hoc_ky_text.get()
        
    def get_nam(self):
        return self.entry_nam_text.get()
    
    def get_tu_ngay(self):
        return self.tu_ngay.get_date()
    
    def get_den_ngay(self):
        return self.den_ngay.get_date()

    #set
    def set_ma_lop(self, ma_hv):
        self.entry_ma_lop_text.set(ma_hv)

    def set_ma_mh(self, ma_hv):
        self.entry_ma_mh_text.set(ma_hv)

    def set_ma_gv(self, ma_hv):
        self.entry_ma_gv_text.set(ma_hv)

    def set_hoc_ky(self, ma_hv):
        self.entry_hoc_ky_text.set(ma_hv)

    def set_nam(self, ma_hv):
        self.entry_nam_text.set(ma_hv)


    def set_tu_ngay(self, tu_ngay):
        self.tu_ngay.set_date(datetime.strptime(tu_ngay, "%Y-%m-%d %H:%M:%S").date())
        
    def set_den_ngay(self, den_ngay):
        self.den_ngay.set_date(datetime.strptime(den_ngay, "%Y-%m-%d %H:%M:%S").date())

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_lop.delete(0, END)
        self.ma_mh.delete(0, END)
        self.ma_gv.delete(0, END)
        self.hoc_ky.delete(0, END)
        self.nam.delete(0, END)
        self.tu_ngay.set_date(datetime.now().date())
        self.den_ngay.set_date(datetime.now().date())
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MALOP"], item["MAMH"], item["MAGV"], item["HOCKY"], item["NAM"], item["TUNGAY"], item["DENNGAY"]))
        
    def showView(self):
        self._root.mainloop()