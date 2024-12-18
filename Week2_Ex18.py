"""
4. Nhập vào một chuỗi từ người dùng, kiểm tra xem đó có phải địa chỉ email hợp lệ hay không?
email hợp lệ: xxxxxx@gmail.com
"""
s = input("Nhập email: ")
tail = ''
for i in range (len(s)):
    if s[i] == '@':
        tail += s[i:]
if len(s) < 16 or tail != '@gmail.com':
    print("Email không hợp lệ")
else:
    print("Email hợp lệ")