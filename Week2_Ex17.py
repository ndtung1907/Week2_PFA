"""
3. Nhập số n, in ra màn hình các số nguyên dương nhỏ hơn n có tống các ước số lớn hơn chính nó.
"""
def tong_cac_uoc(n):
    return sum(i for i in range (1, n // 2 + 1) if n % i == 0)

n = int(input("Nhập số N: "))
result = []
for i in range(1, n):
    if tong_cac_uoc(i) > i:
        result.append(i)
print("các số nguyên dương nhỏ hơn n có tống các ước số lớn hơn chính nó là:",result)