"""
3. Nhập một tên người từ bàn phím, hãy tách phần họ và tên riêng
của người đó và in chúng ra màn hình (giả thiết họ và tên riêng chỉ gồm một âm).
"""
name = list(map(str, input("Nhập họ và tên: ").split()))
print("Họ:",name[0])
print("Tên:",name[-1])
