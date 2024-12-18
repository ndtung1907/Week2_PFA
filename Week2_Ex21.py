"""
7. Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu
• Số nguyên tố là số tự nhiên có 2 ước số là 1 và chính nó.
"""
import math as m
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

P = tuple(num for num in range (2, 10**6) if is_prime(num))
print(P)