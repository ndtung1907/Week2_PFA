"""
6.*Hãy nhập số nguyên n, tạo một list gồm các số
fibonacci nhỏ hơn n và in ra dãy fibonacci là dãy số nguyên
được định nghĩa một cách đệ quy như sau:
f(0)=0, f(1) = 1, f(1<n) = f(n-1) + f(n-2)
"""
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nhập n: "))
result = []
for i in range (n):
    if fibonacci(i) < n:
        result.append(fibonacci(i))
print(f"Các số Fibonacci nhỏ hơn {n}: {result}")