import sys
from info import Ui_Form
from datetime import date
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import*
from themhososv import themhoso
from indanhsach import indanhsach
from sinhvien_class import sinhvien,listSV
from timkiem_class import timkiem
from sapxep_class import sapxep
from thongke import Bieudo
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitGui()
        ##############################DATA _BACK**************
        self._list_sv = listSV()
        #*************Font########********
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.font = font
        #**************************************************PAGE1
        self.page1 = themhoso()
        self.stackedLayout.addWidget(self.page1)
        #**********************************PAGE2 - IN danh sách
        self.page2= indanhsach()
        self.stackedLayout.addWidget(self.page2)
        #**********************************PAGE3 - Sắp xếp
        self.page3 = sapxep(self._list_sv)
        self.is_sort =0 ## đánh dấu loại nào đang được sắp xếp (1 -8)
        self.stackedLayout.addWidget(self.page3)
        #**********************************PAGE4 - TÌM Kiếm
        self.page4 = timkiem(self._list_sv)
        self.stackedLayout.addWidget(self.page4)
        #**********************************PAGE5 - Thống kê
        self.page5 = Bieudo()
        self.stackedLayout.addWidget(self.page5)
            #____-->>load data<<------#
        self.load_data()
        #*******************************************
        self.page_design = QWidget()
        ui = Ui_Form()
        ui.setupUi(self.page_design)
        self.stackedLayout.addWidget(self.page_design)
        self.stackedLayout.setCurrentIndex(5)
        #***************************************su kien xuat hien*************
        self.button1.clicked.connect(lambda:self.switchPage(1))
        self.button2.clicked.connect(lambda:self.switchPage(2)) ## to do
        self.button3.clicked.connect(lambda:self.switchPage(3))
        self.button4.clicked.connect(lambda:self.switchPage(4))
        self.button5.clicked.connect(self.thongke_click)
        self.button6.clicked.connect(self.Exit_click)
        self.page1.bt_Add.clicked.connect(self.themhoso_click)
        
    #@@@@@ method

    def InitGui(self):
        self.setWindowTitle("Quản lí sinh viên")
        self.setGeometry(400,200,1100,600)
        self.setStyleSheet("background-color: rgb(51, 63, 196);")
        # Create a top-level layout
        layout = QHBoxLayout()                                      ## layout cho windoww
        
        layout.setSpacing(0)
        self.stackedLayout = QStackedLayout()                              ## tạo stack layout
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        ##                                                             tạo groupbox là phần MENU trái
        self.groupbox1 = QGroupBox()
        self.groupbox1.setStyleSheet("background-color: rgb(51, 63, 196);color: rgb(255,255,255);")
        self.groupbox1.setFont(font)
        groupbox1Layout = QVBoxLayout()
        self.groupbox1.setLayout(groupbox1Layout)
        
        self.button1 = QPushButton(text="Thêm hồ sơ",font = font)
        self.button1.setFixedHeight(50)
        self.button1.setFixedWidth(190)
        self.button1.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.button2 = QPushButton(text="In danh sách",font = font)
        self.button2.setFixedHeight(50)
        self.button2.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.button3 = QPushButton(text="Sắp xếp",font = font)
        self.button3.setFixedHeight(50)
        self.button3.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.button4 = QPushButton(text="Tìm kiếm",font = font)
        self.button4.setFixedHeight(50)
        self.button4.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.button5 = QPushButton(text="Thống kê",font = font)
        self.button5.setFixedHeight(50)
        self.button5.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        self.button6 = QPushButton(text="Thoát",font = font)
        self.button6.setFixedHeight(50)
        self.button6.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        groupbox1Layout.addWidget(self.button1)
        groupbox1Layout.addWidget(self.button2)
        groupbox1Layout.addWidget(self.button3)
        groupbox1Layout.addWidget(self.button4)
        groupbox1Layout.addWidget(self.button5)
        groupbox1Layout.addWidget(self.button6)
        ## them vao layou window
        layout.addWidget(self.groupbox1)
        layout.addLayout(self.stackedLayout)
        self.setLayout(layout)
    ### tải dữ liệu từ file csv -> load lên in danh sách và thêm vào list_sv
    def load_data(self):
        file = open('sinhvien.csv','r',encoding='utf-8-sig')
        data = []
        file.readline()
        line = file.readline().strip()
        while line !='':
            lst = line.split(',')
            lst[4] = float(lst[4])
            ## xu li ngay sinh cho sinh vien
            date_lst = lst[3].split('/')
            date_ = date(int(date_lst[2]),int(date_lst[1]),int(date_lst[0]))
            sv = sinhvien(lst[0],int(lst[1]),lst[2],date_,lst[4])
            self._list_sv.append(sv)
            data.append(lst)
            line = file.readline().strip()      
        file.close()
        self.page2.refresh(data)
        ## load bieu do ( chung và chi tiết)
        self.page5.dictionary, self.page5.dictionary_detail = self._list_sv.collect()

    ## nút thoát clicked
    def Exit_click(self):
        button = QMessageBox.question(self,"Quản Lí Sinh Viên", "Bạn có chắc mình muốn thoát chương trình")
        if button == QMessageBox.Yes:
            self.close()
    ##     chuyển layout
    def switchPage(self,value):
        if value == 2:
            self.page2.clear()
            self.page2.reload(self._list_sv)
        if value ==4:
            self.page4.is_sort = self.page3.type_sx          
        self.stackedLayout.setCurrentIndex(value-1)
        
    def themhoso_click(self):                       ## nhấn thêm hồ sơ
        def handle(lst,point):
            if point >=9:
                lst[1] +=1
            elif point >=8:
                lst[2] +=1
            elif point >=7:
                lst[3] +=1
            elif point >=5:
                lst[4] +=1
            else:
                lst[5] +=1
            lst[6] +=1

        if self.page1.tb_masv.text() == '':
            button = QMessageBox(self,text='bạn chưa nhập mã sinh viên')
            button.setFont(self.font)
            button.setStyleSheet("color: rgb(255,255,255);")
            button.setWindowTitle("Quản Lí Sinh Viên")
            button.exec()
        else:
            sv = sinhvien(
                self.page1.tb_malop.text().upper(),
                int(self.page1.tb_masv.text()),
                self.page1.tb_hoten.text(),
                self.page1.dateEdit.date().toPyDate(),
                self.page1.doubleSpinBox.value()
                )
            self._list_sv.append(sv)
            self.page2.themhoso(new_data=sv.get_list())
            ### load thong ke chung__________________--------------------------->>>>>>>>>>
            if sv.dtb >=9:
                self.page5.dictionary['xuất sắc'] +=1
            elif sv.dtb >=8:
                self.page5.dictionary['giỏi'] +=1
            elif sv.dtb >=7:
                self.page5.dictionary['khá'] +=1
            elif sv.dtb >=5:
                self.page5.dictionary['trung bình'] +=1
            else:
                self.page5.dictionary['yếu'] +=1
            ### load thong ke chi tiet__________________--------------------------->>>>>>>>>>
            if sv.mlop not in self.page5.dictionary_detail:
                self.page5.dictionary_detail[sv.mlop] = [sv.mlop,0,0,0,0,0,0]
            handle(self.page5.dictionary_detail[sv.mlop],sv.dtb)
            ## làm mới layout thêm hồ sơ--------------------------->>>>>>>>>>
            self.page1.refresh_gui()
            ## ghi vao file csv
            file = open('sinhvien.csv','a',encoding='utf-8-sig')
            file.write(sv.get_line())
            file.close()
            ## show messagebox
            button = QMessageBox(self,text="thêm hồ sơ thành công")
            button.setFont(self.font)
            button.setStyleSheet("color: rgb(255,255,255);")
            button.setWindowTitle("Quản Lí Sinh Viên")
            button.exec()
        
    def thongke_click(self):
        self.page5.refresh()
        self.switchPage(5)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())