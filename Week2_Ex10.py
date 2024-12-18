"""
5. Nhập một dãy các từ từ bàn phím,
hãy in ra từ dài nhất trong dãy vừa nhập, in ra mọi từ có cùng độ dài nhất.
"""
s = list(map(str, input("Nhập các từ: ").split()))
len_s = []
result = []
for x in s:
    len_s.append(len(x))
for idx, x in enumerate(len_s):
    if x == max(len_s):
        result.append(s[idx])
print("Từ dài nhất trong dãy vừa nhập:",result[0])
print("Mọi từ có cùng độ dài nhất:",result)