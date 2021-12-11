import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import*
from PyQt5.QtCore import QMargins, Qt, center, fixed
from datetime import date
from indanhsach import indanhsach
from sinhvien_class import sinhvien,listSV

class timkiem(QWidget):
    font = QtGui.QFont()
    font.setFamily("Times New Roman")
    font.setPointSize(12)
    font.setWeight(75)
    def __init__(self,data = None):
        super().__init__()
        self.data = data
        self.is_sort = None
        self.InitGui()
        #######su kien xay ra#######
        self.bt_TT_mlop.clicked.connect(lambda: self.InitFind(0))
        self.bt_TT_msv.clicked.connect(lambda: self.InitFind(1))
        self.bt_TT_hten.clicked.connect(lambda: self.InitFind(2))
        self.bt_TT_ns.clicked.connect(lambda: self.InitFind(3))
        self.bt_TT_dtb.clicked.connect(lambda: self.InitFind(4))

        self.bt_NP_mlop.clicked.connect(lambda: self.InitFind(0,1))
        self.bt_NP_msv.clicked.connect(lambda: self.InitFind(1,1))
        self.bt_NP_hten.clicked.connect(lambda: self.InitFind(2,1))
        self.bt_NP_ns.clicked.connect(lambda: self.InitFind(3,1))
        self.bt_NP_dtb.clicked.connect(lambda: self.InitFind(4,1))


    def InitGui(self):
        self.resize(730,300)
        #######
        self.stackLayout = QStackedLayout()
        self.setLayout(self.stackLayout)
        ###########
        big_group = QGroupBox()
        layout_big_group = QHBoxLayout()
        big_group.setLayout(layout_big_group)
        groupbox1 = QGroupBox()
        groupbox1.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        groupbox1_layout = QVBoxLayout()
        label1 = QLabel(text="TÌM KIẾM TUẦN TỰ",font = timkiem.font)
        label1.setStyleSheet("color: rgb(255,255,255);")
        label1.setMargin(70)
        label1.setFixedHeight(50)
        self.bt_TT_mlop = QPushButton(text="Theo mã lớp",font = timkiem.font)
        self.bt_TT_mlop.setFixedHeight(40)
        self.bt_TT_msv = QPushButton(text="Theo mã sinh viên",font = timkiem.font)
        self.bt_TT_msv.setFixedHeight(40)
        self.bt_TT_hten = QPushButton(text="Theo họ và tên",font = timkiem.font)
        self.bt_TT_hten.setFixedHeight(40)
        self.bt_TT_ns = QPushButton(text="Theo ngày sinh",font = timkiem.font)
        self.bt_TT_ns.setFixedHeight(40)
        self.bt_TT_dtb = QPushButton(text="Theo điểm trung bình",font = timkiem.font)
        self.bt_TT_dtb.setFixedHeight(40)

        groupbox1_layout.addWidget(label1)
        groupbox1_layout.addWidget(self.bt_TT_mlop)
        groupbox1_layout.addWidget(self.bt_TT_msv)
        groupbox1_layout.addWidget(self.bt_TT_hten)
        groupbox1_layout.addWidget(self.bt_TT_ns)
        groupbox1_layout.addWidget(self.bt_TT_dtb)
        groupbox1.setLayout(groupbox1_layout)

        groupbox2 = QGroupBox()
        groupbox2.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(11,131,120,219),stop:1 rgba(85,98,112,226));color:rgba(255,255,255,220);")
        groupbox2_layout = QVBoxLayout()
        label2 = QLabel(text="TÌM KIẾM NHỊ PHÂN",font = timkiem.font)
        label2.setStyleSheet("color: rgb(255,255,255);")
        label2.setMargin(70)
        label2.setFixedHeight(50)
        self.bt_NP_mlop = QPushButton(text="Theo mã lớp",font = timkiem.font)
        self.bt_NP_mlop.setFixedHeight(40)
        self.bt_NP_msv = QPushButton(text="Theo mã sinh viên",font = timkiem.font)
        self.bt_NP_msv.setFixedHeight(40)
        self.bt_NP_hten = QPushButton(text="Theo họ và tên",font = timkiem.font)
        self.bt_NP_hten.setFixedHeight(40)
        self.bt_NP_ns = QPushButton(text="Theo ngày sinh",font = timkiem.font)
        self.bt_NP_ns.setFixedHeight(40)
        self.bt_NP_dtb = QPushButton(text="Theo điểm trung bình",font = timkiem.font)
        self.bt_NP_dtb.setFixedHeight(40)
        
        groupbox2_layout.addWidget(label2)
        groupbox2_layout.addWidget(self.bt_NP_mlop)
        groupbox2_layout.addWidget(self.bt_NP_msv)
        groupbox2_layout.addWidget(self.bt_NP_hten)
        groupbox2_layout.addWidget(self.bt_NP_ns)
        groupbox2_layout.addWidget(self.bt_NP_dtb)
        groupbox2.setLayout(groupbox2_layout)

        layout_big_group.setContentsMargins(50,0,50,0)
        layout_big_group.addWidget(groupbox1)
        layout_big_group.addWidget(groupbox2)

        self.stackLayout.addWidget(big_group)                                               ### page1

        ####################################
    def InitHeaderFind(self,column_index):
        layout_header = QHBoxLayout()
        layout_header.setContentsMargins(200,0,0,0)
        label = QLabel(text="mã lớp",font = timkiem.font)
        label.setStyleSheet("color:rgb(255,255,255);")
        if column_index == 0:
            f = QtGui.QFont()
            f.setCapitalization(QtGui.QFont.Capitalization.AllUppercase)
            f.setFamily("Times New Roman")
            f.setPointSize(14)
            f.setWeight(75)
            label.setText("Mã lớp: ")
            self.contentFind = QLineEdit()
            self.contentFind.setFont(f)
        elif column_index == 1:
            label.setText("Mã sinh viên: ")
            self.contentFind = QLineEdit()
            self.contentFind.setValidator(QtGui.QIntValidator(self.contentFind))
            self.contentFind.setFont(timkiem.font)
        elif column_index ==2:
            label.setText("Họ và tên: ")
            self.contentFind = QLineEdit()
            self.contentFind.setFont(timkiem.font)
        elif column_index ==3:
            label.setText("Ngày sinh: ")
            self.contentFind = QDateEdit()
            self.contentFind.setDisplayFormat("yyyy/M/d")
            self.contentFind.setFont(timkiem.font)
        else :
            label.setText("Điểm trung bình: ")
            self.contentFind = QDoubleSpinBox()
            self.contentFind.setFont(timkiem.font)
            self.contentFind.setDecimals(1)
            self.contentFind.setMaximum(10.0)
            self.contentFind.setSingleStep(0.1)
        self.contentFind.setStyleSheet("color:rgb(255,255,255);")
        layout_header.addWidget(label)
        layout_header.addWidget(self.contentFind)
        self.bt_find = QPushButton(text="tìm kiếm",font = timkiem.font)
        self.bt_find.setStyleSheet("background-color: rgb(133, 151, 224); color: rgb(255,255,255);")
        self.bt_back = QPushButton(text="trở về",font = timkiem.font)
        self.bt_back.setStyleSheet("background-color: rgb(255, 0, 0);color: rgb(255,255,255);")
        layout_header.addWidget(self.bt_find)
        layout_header.addWidget(self.bt_back)
        return layout_header

    def InitFind(self,column_index,algorithm = None):
        self.result = QWidget()
        result_layout = QVBoxLayout()
        self.result.setLayout(result_layout)
        ## tao nut an header gồm hộp nội dung tìm kiếm và  nút tìm kiếm, nút trở về
        result_layout.addLayout(self.InitHeaderFind(column_index))
        ## su kien phat sinh  nút back trở lại layout tìm kiếm đầu tiên
        self.bt_back.clicked.connect(self.bt_back_click)
        ## table hien thi ket qua tim kiem
        self._table = indanhsach()
        result_layout.addWidget(self._table)                            #page2
        ##########
        self.stackLayout.addWidget(self.result)
        self.stackLayout.setCurrentIndex(1)
        ## su kien tim kiem
        self.bt_find.clicked.connect(lambda: self.Find(column_index,algorithm))
        
    def Find(self,column_index,algorithm):
        #**************aduma
        if column_index ==1:
            if ('+,-' in self.contentFind.text() ) or self.contentFind.text() == '' :
                return
            else:
                content = int(self.contentFind.text())
        elif column_index == 3:
            content = self.contentFind.date().toPyDate()
        elif column_index ==4:
            content = self.contentFind.value()
        elif column_index ==0:
            content = self.contentFind.text().upper()
        else:
            content = self.contentFind.text()

        if not algorithm:
            polydata = self.data.timkiem_TT(column_index,content)    ## danh sách sinh viên tìm thấy
        else:
            if self.is_sort == column_index:
                polydata = self.data.timkiem_NP(column_index,content)
            else:
                button = QMessageBox(self,text='bạn chưa sắp xếp')
                button.setFont(timkiem.font)
                button.setStyleSheet("color:rgb(255,255,255);")
                button.setWindowTitle("Quản Lí Sinh Viên")
                button.exec()
                return
        self._table.clear()
        new_data = []
        if polydata:
            for sv in polydata:
                new_data.append(sv.get_list())
            self._table.refresh(new_data)

    def bt_back_click(self):
        self.stackLayout.removeWidget(self.result)
        del self.result
        self.stackLayout.setCurrentIndex(0)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ns = date(2001,10,25)
    ns2 = date(2001,10,4)
    sv1 = sinhvien('l01',15,'đỗ quang',ns,7.5)
    sv2 = sinhvien('l02',20,'đỗ quang',ns2,8.5)
    sv4 = sinhvien('L100',100,'Hung Quang Do',ns,8.5)
    sv5 = sinhvien('L60',60,'Đỗ Quang Hạnh',ns,8.5)
    sv6 = sinhvien('L61',61,'Đỗ Quốc Hạnh',ns,9.5)
    data = listSV()
    data.append(sv1)
    data.append(sv2)
    data.append(sv4)
    data.append(sv5)
    data.append(sv6)
    data.append(sv6)
    data.append(sv6)
    data.append(sv6)

    window = timkiem(data)
    window.show()
    sys.exit(app.exec_())