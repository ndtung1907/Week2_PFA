"""
4. Nhập một chuỗi từ bàn phím, hãy loại bỏ tất cả các
chữ số khỏi chuỗi và in lại nội dung chuỗi mới ra màn hình.
"""
from numpy.core.defchararray import isnumeric

s = str(input("Nhập chuỗi: "))
s_new = ""
for x in s:
    if not isnumeric(x):
        s_new += x
print("Dãy mới sau khi xóa các chữ số:",s_new)
