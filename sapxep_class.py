import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import*
from PyQt5.QtCore import QMargins, Qt, center, forcepoint
from datetime import date
from indanhsach import indanhsach
from sinhvien_class import sinhvien,listSV
from timkiem_class import timkiem
import unidecode

class sapxep(QWidget):
    def __init__(self,data):
        super().__init__()
        self.data = data   ## dữ liệu là danh sách sinh viên
        self.algorithm =None 
        # 1 - sx_chon
        # 2 - sx_chen
        # 3 - sx_noibot
        # 4 - sx_quicksort
        self.type_sx = None
        # 1 - mã sinh viên
        # 2 - họ và tên
        # 3 - ngày sinh
        # 4 - điểm trung bình
        self.InitGui()
        self.InitMenu1()
        self.InitMenu2()
        self.InitMenu3()
        ## MENU1. CLICK##
        self.bt_sx_chon.clicked.connect(lambda:self.nextMenu1(1))
        self.bt_sx_chen.clicked.connect(lambda:self.nextMenu1(2))
        self.bt_sx_nbot.clicked.connect(lambda:self.nextMenu1(3))
        self.bt_quicksort.clicked.connect(lambda:self.nextMenu1(4))

        ## MENU2. CLICK##
        self.bt_sx_msv.clicked.connect(lambda:self.nextMenu2(1))
        self.bt_sx_hten.clicked.connect(lambda:self.nextMenu2(2))
        self.bt_sx_ns.clicked.connect(lambda:self.nextMenu2(3))
        self.bt_sx_dtb.clicked.connect(lambda:self.nextMenu2(4))
    def InitGui(self):
        self.resize(730,300)
        self.stackLayout = QStackedLayout()
        self.setLayout(self.stackLayout)

    def InitMenu1(self):
        groupbox1 = QGroupBox()
        layout1 = QVBoxLayout()
        layout1.setContentsMargins(170,50,170,50)
        self.bt_sx_chon = QPushButton(text="sắp xếp chọn",font = timkiem.font)
        self.bt_sx_chon.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_chon.setFixedHeight(50)
        self.bt_sx_chen = QPushButton(text="sắp xếp chèn",font = timkiem.font)
        self.bt_sx_chen.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_chen.setFixedHeight(50)
        self.bt_sx_nbot = QPushButton(text="sắp xếp nổi bọt",font = timkiem.font)
        self.bt_sx_nbot.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_nbot.setFixedHeight(50)
        self.bt_quicksort = QPushButton(text="quicksort",font = timkiem.font)
        self.bt_quicksort.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_quicksort.setFixedHeight(50)

        layout1.addWidget(self.bt_sx_chon)
        layout1.addWidget(self.bt_sx_chen)
        layout1.addWidget(self.bt_sx_nbot)
        layout1.addWidget(self.bt_quicksort)

        groupbox1.setLayout(layout1)
        self.stackLayout.addWidget(groupbox1)
    def nextMenu1(self,value):
        self.algorithm = value
        self.stackLayout.setCurrentIndex(1)
    def InitMenu2(self):
        groupbox2 = QGroupBox()
        layout2 = QVBoxLayout()
        layout2.setContentsMargins(170,50,170,50)
        self.bt_sx_msv = QPushButton(text="theo mã sinh viên",font = timkiem.font)
        self.bt_sx_msv.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_msv.setFixedHeight(50)
        self.bt_sx_hten = QPushButton(text="theo họ và tên",font = timkiem.font)
        self.bt_sx_hten.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_hten.setFixedHeight(50)
        self.bt_sx_ns = QPushButton(text="theo ngày sinh",font = timkiem.font)
        self.bt_sx_ns.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_ns.setFixedHeight(50)
        self.bt_sx_dtb = QPushButton(text="theo điểm trung bình",font = timkiem.font)
        self.bt_sx_dtb.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.bt_sx_dtb.setFixedHeight(50)
        self.bt_back0 = QPushButton(text="trở về",font = timkiem.font)
        self.bt_back0.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);")
        self.bt_back0.setFixedHeight(35)
        self.bt_back0.clicked.connect(lambda: self.stackLayout.setCurrentIndex(0))

        layout2.addWidget(self.bt_sx_msv)
        layout2.addWidget(self.bt_sx_hten)
        layout2.addWidget(self.bt_sx_ns)
        layout2.addWidget(self.bt_sx_dtb)
        layout2.addWidget(self.bt_back0)

        groupbox2.setLayout(layout2)
        self.stackLayout.addWidget(groupbox2)
    def nextMenu2(self,value):
        self.type_sx = value
        self.Sort(self.algorithm,self.type_sx)
        self.stackLayout.setCurrentIndex(2)
    def InitMenu3(self):
        self.result = QWidget()
        result_layout = QVBoxLayout()
        self.result.setLayout(result_layout)

        self.bt_back = QPushButton(text="trở về",font = timkiem.font)
        self.bt_back.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);")
        self.bt_back.setFixedHeight(40)
        self.bt_back.clicked.connect(lambda: self.stackLayout.setCurrentIndex(1))
        layout_back = QVBoxLayout()
        layout_back.setContentsMargins(550,0,10,0)
        layout_back.addWidget(self.bt_back)        
        result_layout.addLayout(layout_back)  

        self.Table = indanhsach() # bảng hiển thị  
        result_layout.addWidget(self.Table)
        self.stackLayout.addWidget(self.result)    
    def Sort(self,algorithm,type_sx):   ## thuật toán được chọn và kiểu tìm kiếm theo gì
        if algorithm ==1:
            self.data.selection_Sort(type_sx)
        elif algorithm ==2:
            self.data.insertion_Sort(type_sx)
        elif algorithm == 3:
            self.data.bubble_Sort(type_sx)
        else:
            self.data.quickSort(type_sx)
        self.Table.clear()
        self.Table.reload(self.data)
        ##############################################XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYYYYYYY

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ns = date(2001,10,25)
    ns2 = date(2001,10,4)
    sv1 = sinhvien('l01',1,'đỗ quang hung',ns2,9.5)
    sv2 = sinhvien('l00',0,'Hoàng quang k',ns,8.5)
    sv3 = sinhvien('l20',10,'Nguyễn Quang Sang',ns2,2.3)
    sv4 = sinhvien('L100',100,'Hung Quang Do',ns,9.8)
    sv5 = sinhvien('L60',60,'Đỗ Quang Hạnh',ns,6.5)
    sv6 = sinhvien('L61',61,'Đỗ Quốc Hạnh',ns,6.5)
    sv7 = sinhvien('L61',61,'Đỗ Quốc Hạnh',ns,6.5)
    sv8 = sinhvien('L61',61,'Đỗ Quốc Hạnh',ns,6.5)
    sv8 = sinhvien('L61',61,'Đỗ Quốc Hạnh',ns,6.5)
    danhsach = listSV()
    danhsach.append(sv1)
    danhsach.append(sv2)
    danhsach.append(sv3)
    danhsach.append(sv4)
    danhsach.append(sv6)
    danhsach.append(sv5)
    window = sapxep(danhsach)
    window.show()
    sys.exit(app.exec_())
