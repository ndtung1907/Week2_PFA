"""
7. Nhập chuỗi S gồm toàn chữ số và số nguyên N,
chỉ ra cách xóa đúng N kí tự khỏi S để được số có giá trị lớn nhất.
"""
def maximize_number(S, N):
    stack = []
    sl = N
    for digit in S:
        while sl > 0 and stack and stack[-1] < digit:
            stack.pop()
            sl -= 1
        stack.append(digit)
    result = ''.join(stack[:len(S) - N])
    return result

S = input("Nhập chuỗi S (chỉ gồm chữ số): ")
N = int(input("Nhập số nguyên N: "))

result = maximize_number(S, N)
print(f"Số lớn nhất sau khi xóa {N} chữ số: {result}")
