import random

def menu():
    print("""   --------------------------------MENU--------------------------------
    1. In ra danh sách vừa tạo.
    2. In đảo ngược danh sách.
    3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
    4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
    5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
    6. In ra vị trí các phần tử là số nguyên tố.
    7. Tìm các số duy nhất (không trùng lặp) trong danh sách.
    8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
    9. In ra các đoạn con trong danh sách giảm liên tiếp.
    """)
    
def create_list(n):
    lst = []
    for _ in range(n):
        lst.append(random.randint(1, 100))
    return lst

def print_list(lst):
    print(lst)

def reverse_list(lst):
    print(lst[::-1])

def sorted_list(lst):
    print(sorted(lst))

def find_max_element(lst):
    max_value = max(lst)
    last_index = len(lst) - 1 - lst[::-1].index(max_value)
    print("Giá trị lớn nhất:", max_value)
    print("Vị trí xuất hiện cuối cùng:", last_index)

def find_x(lst, x):
    positions = [i for i, val in enumerate(lst) if val == x]
    print(f"Số lần xuất hiện của {x} là {len(positions)} ở vị trí: {positions}")

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def index_elemental_num(lst):
    indices = [i for i, val in enumerate(lst) if is_prime(val)]
    print("Vị trí các số nguyên tố:", indices)

def find_unique(lst):
    uniques = [x for x in lst if lst.count(x) == 1]
    print("Các số không trùng lặp:", uniques)

def count_elements(lst):
    counter = {}
    for x in lst:
        counter[x] = counter.get(x, 0) + 1
    for k, v in counter.items():
        print(f"{k} xuất hiện {v} lần")

def decreasing_sublists(lst):
    print("Các đoạn con giảm liên tiếp:")
    sub = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            sub.append(lst[i])
        else:
            if len(sub) > 1:
                print(sub)
            sub = [lst[i]]
    if len(sub) > 1:
        print(sub)

def choice():
    while True:
        try:
            choice = int(input("Nhập lựa chọn của bạn (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = create_list(n)
    while True:
        menu()
        choice = choice()
        if choice == 1:
            print_list(lst)
        elif choice == 2:
            reverse_list(lst)
        elif choice == 3:
            sorted_list(lst)
        elif choice == 4:
            find_max_element(lst)
        elif choice == 5:
            x = int(input("Nhập giá trị X: "))
            find_x(lst, x)
        elif choice == 6:
            index_elemental_num(lst)
        elif choice == 7:
            find_unique(lst)
        elif choice == 8:
            count_elements(lst)
        elif choice == 9:
            decreasing_sublists(lst)