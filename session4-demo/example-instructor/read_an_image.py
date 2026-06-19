"""
================================================================================
Tải dữ liệu nhị phân qua HTTP):
================================================================================
Đoạn code này hướng dẫn cách tải một tệp tin không phải là văn bản (ở đây là
file ảnh 'cover3.jpg') từ Web Server và lưu lại thành một file ảnh cục bộ trên máy tính.

Các kiến thức cốt lõi:
1. GOM DỮ LIỆU TẬP TRUNG (Accumulation): Vì ảnh gồm nhiều gói nhỏ truyền về, ta không 
   in ngay mà phải dùng một biến tích lũy (`picture = b""`) để nối tất cả các gói lại.
2. SỰ KHÁC BIỆT GIỮA TEXT VÀ BINARY: Dữ liệu ảnh phải được giữ nguyên ở dạng chuỗi byte 
   (bytes string), tuyệt đối không dùng `.decode()` trong quá trình nhận.
3. KỸ THUẬT PARSING HTTP RESPONSE: Tìm ranh giới giữa phần Header và Body (ký hiệu bằng 
   b"\r\n\r\n"). Sau đó dùng kỹ thuật cắt chuỗi (slicing) để bóc tách riêng phần ảnh thô.
4. GHI FILE NHỊ PHÂN: Sử dụng chế độ "wb" (Write Binary) để ghi dữ liệu ảnh vào ổ cứng.
================================================================================
"""

import socket
import time # Thư viện thời gian (được import để sẵn sàng cho việc thử nghiệm làm chậm luồng mạng)

# Định nghĩa các hằng số cấu hình kết nối để code tường minh hơn
HOST = 'data.pr4e.org'
PORT = 80

# 1. Khởi tạo socket và kết nối tới máy chủ 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))

# 2. Gửi yêu cầu HTTP GET để xin file ảnh 'cover3.jpg'
# Chữ 'b' đặt trước chuỗi (b'GET...') giúp Python hiểu đây là một mảng bytes thô, không cần dùng .encode() nữa
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

# 3. Khởi tạo các biến để đếm và lưu trữ dữ liệu ảnh
count = 0        # Biến đếm tổng số bytes nhận được
picture = b""    # Biến chuỗi byte rỗng để gom tất cả các khối dữ liệu ảnh truyền về

# 4. Vòng lặp nhận dữ liệu từ luồng mạng
while True:
    # Nhận một khối dữ liệu lớn hơn bài trước (tối đa 5120 bytes một lần để tải ảnh cho nhanh)
    data = mysock.recv(5120)
    
    # Nếu máy chủ truyền xong và đóng kết nối (len < 1), thoát khỏi vòng lặp
    if len(data) < 1:
        break
    
    # [Tùy chọn] Có thể bỏ dấu comment dòng dưới để thấy mạng tải chậm sẽ gom dữ liệu thế nào
    # time.sleep(0.25)
    
    count = count + len(data)      # Cộng dồn số lượng byte vừa nhận vào biến tổng
    print(len(data), count)        # In ra tiến trình: (Số byte vừa nhận được trong lượt này, Tổng số byte đã tích lũy)
    picture = picture + data       # Tiến hành "nối" khối dữ liệu vừa nhận vào cuối biến 'picture' lớn

# 5. Ngắt kết nối mạng sau khi đã nhận toàn bộ dữ liệu thô vào bộ nhớ RAM
mysock.close()

print("\n--- QUÁ TRÌNH TẢI HOÀN THÀNH. BẮT ĐẦU XỬ LÝ HẬU KỲ ---")

# 6. TÌM RANH GIỚI GIỮA HEADER VÀ BODY
# Ký tự xuống dòng kép b"\r\n\r\n" là vạch phân cách giữa thông tin kỹ thuật và dữ liệu ảnh thực tế.
# Hàm .find() trả về vị trí (chỉ mục - index) đầu tiên của ký tự xuống dòng kép này.
pos = picture.find(b"\r\n\r\n")
print('Độ dài phần Header (tính bằng bytes):', pos)

# 7. IN THỬ PHẦN HEADER RA MÀN HÌNH ĐỂ KIỂM TRA
# Cắt chuỗi từ đầu đến vị trí 'pos' (chỉ lấy phần chữ kỹ thuật), giải mã thành text để đọc
print("\n--- NỘI DUNG HTTP HEADER NHẬN ĐƯỢC ---")
print(picture[:pos].decode())

# 8. TRÍCH XUẤT DỮ LIỆU ẢNH THÔ (HTTP BODY)
# Bỏ qua phần Header và 4 ký tự phân cách (\r\n\r\n dài đúng 4 bytes), lấy dữ liệu từ vị trí pos+4 trở đi
picture = picture[pos+4:]

# 9. GHI DỮ LIỆU ẢNH VÀO FILE TRÊN Ổ CỨNG
# - "stuff.jpg": Tên file ảnh sẽ được lưu lại trong cùng thư mục với file code Python này.
# - "wb": Chế độ ghi dữ liệu nhị phân (Write Binary), bắt buộc phải có đối với file ảnh/video/âm thanh.
fhand = open("stuff.jpg", "wb")
fhand.write(picture) # Đổ toàn bộ dữ liệu ảnh thô vào file
fhand.close()        # Đóng file, hoàn tất việc tạo ảnh

print("\nĐã lưu file thành công với tên 'stuff.jpg'. Hãy mở thư mục chứa code để kiểm tra!")