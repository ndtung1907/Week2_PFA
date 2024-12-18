"""
1. Người dùng nhập từ bàn phím liên tiếp các từ tiếng Anh viết tách nhau bởi dấu cách. Hãy
nhập chuỗi đầu vào và tách thành các từ sau đó in ra màn hình các từ đó theo thứ tự từ điển.
"""
s = list(map(str, input("Nhập các từ tiếng Anh: ").split()))
print(sorted(s))