"""
6. Nhập một dãy các từ từ bàn phím,
thống kê xem có những chữ cái nào xuất hiện trong dãy và mỗi chữ xuất hiện bao nhiêu lần?
"""
input_string = input("Nhập một dãy các từ: ")
char_count = {}

for char in input_string:
    if char.isalpha():
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print("Số lần xuất hiện của các chữ cái:")
for char, count in char_count.items():
    print(f"{char}: {count}")
