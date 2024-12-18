"""
Bài 4: Viết chương trình cho phép người dung nhập vào liên tiếp một dãy số tự
nhiên (không biết trước độ dài). Việc nhập dãy sẽ kết thúc khi người dùng nhập
một số âm hoặc số 0.

Sau khi kết thúc, in ra màn hình ước số chung lớn nhất và bội số chung nhỏ nhất
của tất cả các số vừa nhập vào.
"""
from math import gcd
from functools import reduce

from fontTools.otlLib.builder import buildCaretValueForCoord


def ucln(nums):
    return reduce(gcd, nums)

def lcm(a,b):
    return a*b // gcd(a,b)

def bcnn(nums):
    return reduce(lcm, nums)
list = []
while True:
    n = int(input("Nhập số để thêm vào dãy (Nhập số âm hoặc 0 để kết thúc nhập): "))
    if n > 0:
        list.append(n)
    else:
        break
print("Ước chung lớn nhất:",ucln(list))
print("Bội chung nhỏ nhất:",bcnn(list))