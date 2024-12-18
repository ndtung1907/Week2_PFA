"""
5. Nhập n, in n dòng đầu tiên của tam giác pascal
"""
def tao_tam_giac_pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

n = int(input("Nhập n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
triangle = tao_tam_giac_pascal(n)
print("Tam giác Pascal:")
max_width = len(" ".join(map(str, triangle[-1])))
for row in triangle:
    row_str = " ".join(map(str, row))
    print(row_str.center(max_width)) 
