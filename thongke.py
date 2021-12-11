from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QPushButton, QStackedLayout, QVBoxLayout,QApplication
from PyQt5.QtChart import*
from indanhsach import indanhsach
import sys

from PyQt5.QtWidgets import QWidget
class Bieudo(QWidget):
    def __init__(self):
        super().__init__()
        #''' dữ liệu của thống kê chung '''
        self.dictionary ={'xuất sắc': 1, 'giỏi':1,'khá':1,'trung bình':1,'yếu':1}
        #''' dữ liệu của thống kê chi tiết '''
        self.dictionary_detail = dict()
        #window requirements
        self.setGeometry(200,200,600,400)
        self.setStyleSheet('background-color:green')

        self.Init1()
        self.Init2()
        self.button_detail.clicked.connect(lambda:self.stacklayout.setCurrentWidget(self.detail))
        self.button_back.clicked.connect(lambda:self.stacklayout.setCurrentWidget(self.chartview))

    def extract(self):
        lst =[]
        for item in self.dictionary_detail:
            lst.append(self.dictionary_detail[item])
        return lst

    def Init1(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        self.setLayout(layout)

        self.stacklayout = QStackedLayout()
        #create chartview and add the chart in the chartview
        self.chartview = None

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(300,0,0,0)
        btn_layout.setSpacing(10)
        self.button_detail = QPushButton(text="thống kê chi tiết")
        self.button_detail.setStyleSheet('background-color:red;')
        self.button_detail.setFixedHeight(30)
        self.button_back = QPushButton(text="trở về")
        self.button_back.setStyleSheet('background-color:red;')
        self.button_back.setFixedHeight(30)
        btn_layout.addWidget(self.button_detail)
        btn_layout.addWidget(self.button_back)

        ## bố cục trang 1:
        layout.addLayout(btn_layout)
        # self.stacklayout.addWidget(self.chartview)
        layout.addLayout(self.stacklayout)

    def Init2(self):
        self.detail = indanhsach()
        self.detail.clean()
        self.stacklayout.addWidget(self.detail)
    def refresh(self):
    # đồ thị phân loại chung *******************
        if self.chartview != None:
            self.stacklayout.removeWidget(self.chartview)
            del self.chartview
        #create barseries
        self.set0 = QBarSet("Xuất sắc")
        self.set1 = QBarSet("Giỏi")
        self.set2 = QBarSet("Khá")
        self.set3 = QBarSet("Trung bình")
        self.set4 = QBarSet("Yếu")
        #insert data to the barseries
        self.set0 << self.dictionary['xuất sắc']
        self.set1 << self.dictionary['giỏi']
        self.set2 << self.dictionary['khá']
        self.set3 << self.dictionary['trung bình']
        self.set4 << self.dictionary['yếu']
        #we want to create percent bar series
        series = QBarSeries()
        series.append(self.set0)
        series.append(self.set1)
        series.append(self.set2)
        series.append(self.set3)
        series.append(self.set4)
 
        #create chart and add the series in the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Biểu đồ phân loại học viên")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeDark)

        #create axis for the chart
        categories = "Phân loại chung"
        self.axis = QBarCategoryAxis()
        self.axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(self.axis, series)
        #create chartview and add the chart in the chartview
        self.chartview = QChartView(chart)
        self.stacklayout.addWidget(self.chartview)
        self.stacklayout.setCurrentWidget(self.chartview)
    #***** thống kê chi tiết
        self.detail.clean()
        self.detail.refresh(self.extract())

# if __name__ =='__main__':
#     App = QApplication(sys.argv)
#     window = Bieudo()
#     # window.dictionary['giỏi'] = 5
#     window.refresh()
#     window.show()
#     sys.exit(App.exec())