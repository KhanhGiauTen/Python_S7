def menu():
    print("""   --------------------------------MENU--------------------------------
    1. In ra danh sách vừa tạo.
    2. In đảo ngược danh sách.
    3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
    4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
    5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
    6. In ra vị trí các phần tử là số nguyên tố.
    7. tìm các số duy nhất (không trùng lặp) trong danh sách.
    8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
    9. In ra các đoạn con trong danh sách giảm liên tiếp.
          """)
    
import random

def create_list(n):  
    list = []
    for i in range(n):
        i = random(1,100)
        list.append(i)
    return list

def print_list(list):
    print(list)
    
def reverse(list):
    print(list.reverse())

def sorted_list(list):
    print(sorted(list))
    
def find_max_element(list):
    max = max(list)
    for index,value in list[::-1]:        
        if value == max:
            return index
        
def find_x(list,x):
    count = 0
    lst = []
    for index, value in enumerate(list):
        if value == x:
            lst.append(index)
            count +=1
    return lst,count
        
def index_elemental_num(list):
    list_ele = []
    count = 0
    for index, value in enumerate(list):
        for j in range(value):
            if value % j == 0:
                count +=1
        if count ==2:
            list_ele.append(index)
    return list_ele

def 

def choice(lc):
        

