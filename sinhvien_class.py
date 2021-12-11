from datetime import date
from typing import Pattern
from unidecode import unidecode

class sinhvien:
    def __init__(self,malop,masv,hoten,ngaysinh,dtb):
        self.mlop= malop  # str
        self.msv = masv   # int
        self.hten = hoten # str
        self.ns = ngaysinh # date 2001-12-24
        self.dtb = dtb  # float
    def get_list(self):
        return [self.mlop,self.msv,self.hten,self.ns,self.dtb]
    def get_line(self):
        # xu li định dạng date khi trả về kiểu  25/12/2001
        buff = str(self.ns).split('-')
        buff.reverse()
        buff = '{0}/{1}/{2}'.format(*buff)
        result = '{0},{1},{2},{3},{4}\n'.format(self.mlop,self.msv,self.hten,buff,self.dtb)
        return result
    def get_ppt(self,type):  # get properties (thuộc tính)
        if type == 0:
            return self.mlop
        elif type == 1:
            return self.msv
        elif type ==2:
            return self.hten
        elif type ==3:
            return self.ns
        else:
            return self.dtb
    @staticmethod
    def compare(ppt1,ppt2,type_sx):
        if type_sx ==2:
        # chuyển chữ có dấu về ko dấu,viết thường, sxep tên -> họ -> tên đệm
            value1 = ppt1.lower().split(' ')
            value1 = [value1[-1]] + value1
            value1 = ' '.join(value1)
            value2 = ppt2.lower().split(' ')
            value2 = [value2[-1]] + value2
            value2 = ' '.join(value2)
            return unidecode(value1) < unidecode(value2)
        else:
            return ppt1 < ppt2
# class danh sach xu li toan bo ham tim kiem va sap xep
class listSV:
    is_sort =0
    def __init__(self):
        self.list = []
        ## dictionary for bieu do
        self.dct = dict()
    def append(self,sv):
        self.list.append(sv)

    def get_list(self):
        return self.list
    ## phân loại học viên cho phần thống kê chung và chi tiết
    def collect(self):
        def handle(lst,dct,point):
            if point >=9:
                lst[1] +=1
                dct['xuất sắc'] +=1
            elif point >=8:
                lst[2] +=1
                dct['giỏi'] +=1
            elif point >=7:
                lst[3] +=1
                dct['khá'] +=1
            elif point >=5:
                lst[4] +=1
                dct['trung bình'] +=1
            else:
                lst[5] +=1
                dct['yếu'] +=1
            lst[6] +=1    

        self.dct ={'xuất sắc': 0, 'giỏi':0,'khá':0,'trung bình':0,'yếu':0}
        self.dct_detail = dict()  # dạng {'BĐATTT':['BĐATTT',0,0,0,0,0,0]}
        for sv in self.list:
            if sv.mlop not in self.dct_detail:
                self.dct_detail[sv.mlop] = [sv.mlop,0,0,0,0,0,0]
            handle(self.dct_detail[sv.mlop],self.dct,sv.dtb)
        
        return self.dct,self.dct_detail
    ### tìm kiếm tuần tự
    def timkiem_TT(self,column_index,value):
        result = []
        for sv in self.list:
            if value == sv.get_ppt(column_index):
                result.append(sv)
        return result
    def timkiem_NP(self,column_index,value):
        S = self.list
        low =0
        high = len(S) -1
        while low<=high:
            middle = int((low + high)/2)
            if S[middle].get_ppt(column_index) == value:
                top = middle +1
                dow = middle -1
                ## tiếp tục tìm xung quanh middle
                while top<=high and S[top].get_ppt(column_index) == value:
                    top +=1
                while dow >= low and S[dow].get_ppt(column_index) == value:
                    dow -=1
                return S[dow+1 : top] # trả về khoảng sinh viên thỏa mãn
            elif sinhvien.compare(value,S[middle].get_ppt(column_index),column_index):
                high = middle -1
            else:
                low = middle +1
                
        ## SẮP XẾP
    def selection_Sort(self,type_sx):
        S = self.list
        for i in range(len(S)):
            min =i
            for j in range(1+i,len(S)):
                if sinhvien.compare(S[j].get_ppt(type_sx),S[min].get_ppt(type_sx),type_sx):
                    min = j
            S[i],S[min] = S[min],S[i]
    def insertion_Sort(self,type_sx):
        S = self.list
        for i in range(len(S)):
            cursor = S[i]
            pos = i
            while pos>0 and sinhvien.compare(cursor.get_ppt(type_sx),S[pos-1].get_ppt(type_sx),type_sx):
                S[pos] = S[pos - 1]
                pos -=1
            S[pos] = cursor
    def bubble_Sort(self,type_sx):
        S = self.list
        n = len(S)
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if sinhvien.compare(S[i].get_ppt(type_sx),S[i-1].get_ppt(type_sx),type_sx):
                    S[i],S[i-1] = S[i-1],S[i]
                    swapped = True
    def quickSort(self,type_sx):
        S = self.list
        def partition(S,low,high):
            i = low -1
            pivot = S[high]
            for j in range(low,high):
                if sinhvien.compare(S[j].get_ppt(type_sx),pivot.get_ppt(type_sx),type_sx):
                    i = i +1
                    S[i],S[j] = S[j],S[i]
            S[i+1],S[high] = S[high],S[i+1]
            return i+1
        def quicksort(S,low,high):
            if len(S) <=1:
                return
            if low < high:
                pi = partition(S,low,high)
                quicksort(S,low,pi-1)
                quicksort(S,pi+1,high)
        quicksort(S,0,len(S)-1)

if __name__ == "__main__":
    ns = date(2001,10,25)
    sv1 = sinhvien('l01',15,'đỗ quang hung',ns,7.5)
    sv2 = sinhvien('l02',20,'Hoàng quang k',ns,2.5)
    sv4 = sinhvien('l02',20,'Hoàng quang k',ns,9.5)
    sv3 = sinhvien('l05',1,'Nguyễn Quang Sang',ns,4.5)

    # print(sv1.get_line())
    danhsach = listSV()
    danhsach.append(sv1)
    danhsach.append(sv2)
    danhsach.append(sv3)
    danhsach.append(sv4)
    # danhsach.Sort_selection(2)
    # danhsach.insertion_Sort(1)
    # danhsach.quickSort(4)