import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import*
from PyQt5.QtCore import QMargins, Qt
from datetime import date
from sinhvien_class import sinhvien,listSV
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
    def data(self, index, role):
        if (role == QtCore.Qt.TextAlignmentRole):
            return QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            if isinstance(value, date):
            # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
            # Render float to 2 dp
                return "%.2f" % value

            return value
        ############################################
        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if index.row() ==0:
                return QtGui.QColor('blue')
            if (isinstance(value, float)and value < 5):
                return QtGui.QColor('red')
            elif (isinstance(value, float)and value < 7):
                return QtGui.QColor('gray')


    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class indanhsach(QWidget):
    def __init__(self):
        super().__init__()
        self.data = [['Mã lớp','Mã sinh viên','Họ và tên','Ngày sinh','Điểm trung bình tích lũy']]
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setWeight(75)
        layout = QFormLayout()
        self.setLayout(layout)
        self.resize(710,400)
        self.table = QTableView()
        self.table.setStyleSheet("background-color: white;")
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        # self.table
        self.table.setColumnWidth(4,210)
        self.table.setColumnWidth(2,230)
        self.table.setRowHeight(0,60)
        self.table.setFont(font)
        layout.addWidget(self.table)
    def themhoso(self,new_data):
        self.data.append(new_data)
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
    def refresh(self,new_data):  ## them data sau khi thay doi ## data dạng list các list( dòng info sinh vien)
        self.data += new_data
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
    def reload(self,list_sv):  ## data dạng list các sinh viên lst = [sv1,sv2,..]
        lst = []
        for sv in list_sv.list:
            lst.append(sv.get_list())
        self.refresh(lst)
    def clear(self):
        self.data = [['Mã lớp','Mã sinh viên','Họ và tên','Ngày sinh','Điểm trung bình tích lũy']]
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
    def clean(self):
        self.data = [['Mã lớp','Xuất sắc','Giỏi','Khá','Trung bình','Yếu','Tổng']]
        self.model = TableModel(self.data)
        self.table.setModel(self.model)
        self.table.setColumnWidth(2,114)   ## default
        self.table.setColumnWidth(4,114)   ## default
        self.table.setRowHeight(0,34)       ##default
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ns = date(2001,10,25)
    sv1 = sinhvien('l01','sv01','đỗ quang',ns,7.5)
    sv2 = sinhvien('l02','sv00','đỗ quang',ns,6.5)
    danhsach = listSV()
    danhsach.append(sv1)
    danhsach.append(sv2)
    window = indanhsach()
    b = ['l01','sv01','đỗ quang hùng','25-10-2001',2.3]
    window.themhoso(b)
    window.reload(danhsach)
    # window.clean()
    window.show()
    sys.exit(app.exec_())