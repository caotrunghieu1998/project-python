from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

from common.common import Common

class KetQuaThiView:
    _instance = None

    @classmethod
    def getInstance(cls):
        if (KetQuaThiView._instance):
            return KetQuaThiView._instance
        KetQuaThiView._instance = KetQuaThiView()
        
        return KetQuaThiView._instance

    def __init__(self, root: Tk, data, type):
        self._root = root
        self._data = data
        self._type = type
        self._tree = ttk.Treeview(None)
        self._common = Common()
        self._common.center_window(root)
        self.initView()
        
    @property
    def tree(self):
        return self._tree
    
    @property
    def data_param(self):
        return self._data
    
    def initView(self):
        root = self._root

        root.title("Danh sách kết quả thi")
        self.top_frame = Frame(root, padx=10, pady=10)
        self.top_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.top_frame.grid_rowconfigure(0, weight=1)  # Chỉ định row 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(0, weight=1)  # Chỉ định cột 0 có thể thay đổi kích thước
        self.top_frame.grid_columnconfigure(1, weight=2)
        self.top_frame.grid_columnconfigure(2, weight=2)
        self.top_frame.grid_columnconfigure(3, weight=3)
        self.top_frame.grid_columnconfigure(4, weight=4)
        self.top_frame.grid_columnconfigure(5, weight=5)
        
        self.header()
        self.body()

    def header(self):
        """Tạo các ô nhập liệu."""
        # Tiêu đề
        self.labelTitle = Label(self.top_frame, text="Danh sách kết quả thi", font=("Arial", 20, "bold"))
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

        # Mã HV
        self.label_ma_hv = Label(self.top_frame, text="Mã Học Viên: ", font=("Arial", 10, "bold"))
        self.label_ma_hv.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_hv_text = StringVar()
        self.ma_hv = Entry(self.top_frame, textvariable=self.entry_ma_hv_text, width=40, font=("Arial", 10))
        self.ma_hv.grid(row=1, column=1, padx=10, pady=5)

        # MAMH
        self.label_ma_mh = Label(self.top_frame, text="Mã môn học: ", font=("Arial", 10, "bold"))
        self.label_ma_mh.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_ma_mh_text = StringVar()
        self.ma_mh = Entry(self.top_frame, textvariable=self.entry_ma_mh_text, width=40, font=("Arial", 10))
        self.ma_mh.grid(row=2, column=1, padx=10, pady=5)
        
        #lần thi
        self.label_lanthi = Label(self.top_frame, text="Lần thi: ", font=("Arial", 10, "bold"))
        self.label_lanthi.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_lanthi_text = StringVar()
        self.lanthi = Entry(self.top_frame, textvariable=self.entry_lanthi_text, width=40, font=("Arial", 10))
        self.lanthi.grid(row=3, column=1, padx=10, pady=5)

        # Ngày thi
        self.label_ng_thi = Label(self.top_frame, text="Ngày thi: ", font=("Arial", 10, "bold"))
        self.label_ng_thi.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.ng_thi = DateEntry(self.top_frame, width=40, background="darkblue", foreground="white", borderwidth=2, date_pattern="dd/mm/yyyy")
        self.ng_thi.grid(row=4, column=1, padx=10, pady=5)

        # Điểm
        self.label_diem = Label(self.top_frame, text="Điểm: ", font=("Arial", 10, "bold"))
        self.label_diem.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_diem_text = StringVar()
        self.diem = Entry(self.top_frame, textvariable=self.entry_diem_text, width=40, font=("Arial", 10))
        self.diem.grid(row=5, column=1, padx=10, pady=5)

        # Kết quả
        self.label_kqua = Label(self.top_frame, text="Kết quả: ", font=("Arial", 10, "bold"))
        self.label_kqua.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_kqua_text = StringVar()
        self.kqua = Entry(self.top_frame, textvariable=self.entry_kqua_text, width=40, font=("Arial", 10))
        self.kqua.grid(row=6, column=1, padx=10, pady=5)

        # Các nút chức năng
        self.button_frame = Frame(self.top_frame)
        self.button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        self.buttonRefresh = Button(self.button_frame, text="Làm mới", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRefresh.grid(row=0, column=0, padx=10)

        self.buttonAdd = Button(self.button_frame, text="Thêm", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonAdd.grid(row=0, column=1, padx=10)

        self.buttonEdit = Button(self.button_frame, text="Cập nhật", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonEdit.grid(row=0, column=2, padx=10)

        self.buttonRemove = Button(self.button_frame, text="Xoá", font=("Arial", 10), width=12, relief="raised", bd=2)
        self.buttonRemove.grid(row=0, column=3, padx=10)

    def body(self):
        """Tạo bảng Treeview."""
        self._tree = ttk.Treeview(
            self._root, columns=("MAHV", "MAMH", "LANTHI", "NGTHI", "DIEM", "KQUA"), show="headings"
        )
        self._tree.pack(fill="both", expand=True, padx=10, pady=10)

        self._tree.heading("MAHV", text="Mã Học Viên")
        self._tree.heading("MAMH", text="Mã môn học")
        self._tree.heading("LANTHI", text="Lần thi")
        self._tree.heading("NGTHI", text="Ngày thi")
        self._tree.heading("DIEM", text="Điểm")
        self._tree.heading("KQUA", text="Kết quả")

        self._tree.column("MAHV", width=20, anchor="center")
        self._tree.column("MAMH", width=20, anchor="center")
        self._tree.column("LANTHI", width=20, anchor="w")
        self._tree.column("NGTHI", width=20, anchor="center")
        self._tree.column("DIEM", width=20, anchor="center")
        self._tree.column("KQUA", width=40, anchor="center")

    #get
    def get_selected_item(self):
        """Trả về du lieu của item được chọn."""
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
            "MAHV": self.get_ma_hv(),
            "MAMH": self.get_ma_mh(),
            "LANTHI": self.get_lanthi(),
            "NGTHI": self.get_ng_thi(),
            "DIEM": self.get_diem(),
            "KQUA": self.get_kqua(),
        }
        
    def get_ma_hv(self):
        return self.entry_ma_hv_text.get()
    
    def get_ma_mh(self):
        return self.entry_ma_mh_text.get()
    
    def get_lanthi(self):
        return self.entry_lanthi_text.get()
        
    def get_ng_thi(self):
        return self.ng_thi.get_date()
        
    def get_diem(self):
        return self.entry_diem_text.get()
    
    def get_kqua(self):
        return self.entry_kqua_text.get()

    #set
    def set_ma_hv(self, ma_hv):
        self.entry_ma_hv_text.set(ma_hv)

    def set_ma_mh(self, ma_mh):
        self.entry_ma_mh_text.set(ma_mh)

    def set_lanthi(self, lanthi):
        self.entry_lanthi_text.set(lanthi)

    def set_ng_thi(self, ng_thi):
        self.ng_thi.set_date(datetime.strptime(ng_thi, "%Y-%m-%d %H:%M:%S").date())

    def set_diem(self, diem):
        self.entry_diem_text.set(diem)

    def set_kqua(self, kqua):
        self.entry_kqua_text.set(kqua)

    def clear_inputs(self):
        """Xóa nội dung các ô nhập liệu."""
        self.ma_hv.delete(0, END)
        self.ma_mh.delete(0, END)
        self.lanthi.delete(0, END)
        self.ng_thi.set_date(datetime.now().date())
        self.diem.delete(0, END)
        self.kqua.delete(0, END)
        
    def load_list(self, data):
        """Cập nhật Treeview với dữ liệu."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for item in data:
            self._tree.insert("", END, values=(item["MAHV"], item["MAMH"], item["LANTHI"], item["NGTHI"], item["DIEM"], item["KQUA"]))
        
    def showView(self):
        self._root.mainloop()