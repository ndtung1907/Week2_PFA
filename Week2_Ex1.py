# Bài 1: Viết hàm is_prime kiểm tra xem N có phải số nguyên tố hay không?
import math as m
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(is_prime(5))
print(is_prime(6))