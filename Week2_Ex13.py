"""
8. Nhập chuỗi S, hãy thay thế tất cả các chữ số
trong S bằng kí tự hỏi chấm (?), sau đó in lại S ra màn hình
"""
from numpy.core.defchararray import isnumeric

s = str(input("Nhập vào chuỗi: "))
result = ""
for x in s:
    if not isnumeric(x):
        result += x
    else:
        result += '?'
print(result)