"""
9. Nhập chuỗi S, kiểm tra xem chuỗi S có là dạng đối xứng hay không?
"""
s = str(input("Nhập chuỗi: "))
print("S là chuỗi đối xứng" if s == s[::-1] else "S là chuỗi không đối xứng")