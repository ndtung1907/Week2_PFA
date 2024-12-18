"""
1. Nhập một chuỗi từ bàn phím, kiểm tra xem nó có tận cùng bởi 3
dấu chấm than hay không (!!!), nếu không thì hãy thêm dấu chấm than
vào cuối để chuỗi có tận cùng là 3 dấu chấm than.
"""
s = str(input("Nhập chuỗi: "))
while s[:len(s)-4:-1] != "!!!":
    s += "!"
print("Dãy sau khi thêm:",s)