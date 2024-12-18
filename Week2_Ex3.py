"""
Bài 3: Nhập 2 số nguyên dương A và B, tính và in ra màn hình ước số chung lớn
nhất và bội số chung nhỏ nhất của 2 số đó.
"""
def ex3_ucln(a,b):
    max0 = max(a,b)
    min0 = min(a,b)
    a, b = max0, min0
    while b != 0:
        a, b = b, a % b
    return a

def ex3_bcnn(a,b):
    ucln = ex3_ucln(a,b)
    return (a*b) // ucln

print(ex3_ucln(91,287))
print(ex3_bcnn(23,47))