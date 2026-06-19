"""
================================================================================
MĐọc dữ liệu web bằng urllib cấp cao
================================================================================
Đoạn code này minh họa sức mạnh của việc "sử dụng thư viện cấp cao" (Abstraction).
Thay vì phải tự quản lý Socket và giao thức HTTP thủ công, `urllib` tự động xử lý ẩn:
1. Tự động thiết lập kết nối Socket ẩn bên dưới.
2. Tự động gửi yêu cầu HTTP GET chuẩn chỉnh.
3. Tự động bóc tách và "giấu" phần HTTP Headers đi, chỉ trả lại phần nội dung (Body) cho lập trình viên.
4. Cho phép xử lý luồng dữ liệu mạng bằng vòng lặp `for` như đang đọc file cục bộ.

Bài toán mở rộng: Kết hợp đọc file từ mạng với cấu trúc dữ liệu Từ điển (Dictionary) 
để đếm tần suất xuất hiện của từng từ trong tác phẩm của Shakespeare.
================================================================================
"""

# ------------------------------------------------------------------------------
# ĐỌC VÀ IN NỘI DUNG TRANG WEB BẰNG URLLIB
# ------------------------------------------------------------------------------
print("=== ĐỌC VÀ IN NỘI DUNG FILE TỪ INTERNET ===")

# 1. Nhập thư viện urllib.request chuyên dùng để mở các liên kết URL
import urllib.request

# 2. Sử dụng hàm urlopen() để kết nối trực tiếp đến file.
# Biến 'fhand' (file handle) lúc này được xử lý giống hệt như khi ta dùng lệnh open() để mở một file trên máy tính.
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# 3. Sử dụng vòng lặp for để đọc từng dòng (line) từ luồng mạng trả về
for line in fhand:
    # - line.decode(): Vì dữ liệu nhận về vẫn là bytes nhị phân, ta vẫn cần giải mã sang chuỗi ký tự.
    # - .strip(): Loại bỏ các ký tự khoảng trắng thừa và ký tự xuống dòng (\n) ở hai đầu để hiển thị đẹp mắt.
    print(line.decode().strip())


# ------------------------------------------------------------------------------
# ĐỌC BINARY VÀ ĐẾM TẦN SUẤT TỪ (WORD COUNTING)
# ------------------------------------------------------------------------------
print("\n=== PHÂN TÍCH TẦN SUẤT TỪ BẰNG DICTIONARY ===")

# Nhập thêm các thư viện xử lý phân tách cú pháp và bắt lỗi mạng (theo giáo trình)
import urllib.parse
import urllib.error

# Mở lại file từ internet một lần nữa để con trỏ đọc file quay về vị trí đầu tiên
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Khởi tạo một từ điển rỗng để lưu trữ kết quả đếm: { 'từ_nào': số_lần_xuất_hiện }
counts = dict()

# Vòng lặp duyệt qua từng dòng của file thơ vừa tải về
for line in fhand:
    # Giải mã dòng byte thành chuỗi chữ, sau đó dùng .split() để tách dòng thành một danh sách các từ đơn lẻ dựa vào khoảng trắng
    words = line.decode().split()
    
    # Vòng lặp lồng: Duyệt qua từng từ đơn lẻ trong danh sách vừa tách được
    for word in words:
        # Sử dụng hàm .get(word, 0): Nếu từ này chưa có trong từ điển, lấy giá trị mặc định là 0. 
        # Sau đó cộng thêm 1 đơn vị đếm cho từ đó.
        counts[word] = counts.get(word, 0) + 1

# In toàn bộ từ điển kết quả đếm được ra màn hình
print("\nKết quả đếm tần suất các từ:")
print(counts)