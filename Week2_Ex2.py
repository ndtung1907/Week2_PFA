"""
Bài 2: Viết chương trình nhập hai số A và B, in ra tất cả các số nguyên tố nằm
trong khoảng [A, B]
"""
import math as m
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def ex2(a,b):
    for i in range(a,b+1):
        if is_prime(i):
            print(i, end=" ")
ex2(2,10)