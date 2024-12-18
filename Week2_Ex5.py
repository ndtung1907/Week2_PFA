"""
Bài 5: Viết chương trình cho phép người dung nhập vào liên tiếp một dãy số bất
kì (không biết trước độ dài). Việc nhập dãy sẽ kết thúc khi người dùng nhập vào
số 0.

Sau khi kết thúc, in ra màn hình số lượng số đã nhập, giá trị nhỏ nhất và giá trị
lớn nhất của dãy số vừa nhập.
"""
list = []
while True:
    n = int(input("Nhập số để thêm vào dãy (Nhập số 0 để kết thúc nhập): "))
    if n != 0:
        list.append(n)
    else:
        break
print("Số lượng đã nhập:",len(list))
print("Giá trị nhỏ nhất:",min(list))
print("Giá trị lớn nhất:",max(list))