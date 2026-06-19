"""
================================================================================
Đọc file nhị phân lớn bằng urllib
================================================================================
Mục tiêu trọng tâm là dạy sinh viên về quản lý bộ nhớ RAM khi lập trình mạng.

1. BẢN CHẤT CỦA HÀM .read() KHÔNG THAM SỐ: Khi gọi `urlopen().read()`, Python sẽ cố gắng
   "bốc" toàn bộ file từ Internet và nén chặt vào một biến nằm trên RAM. Nếu file nặng 4GB
   trong khi RAM máy tính chỉ còn trống 2GB, chương trình sẽ crash ngay lập tức (Out of Memory).
2. GIẢI PHÁP ĐỌC THEO KHỐI (Chonking/Buffering): Bằng cách truyền một con số vào hàm `.read(100000)`,
   ta giới hạn máy tính chỉ được phép lấy đúng 100,000 bytes mỗi lần. 
3. LUỒNG XỬ LÝ TỐI ƯU: Cứ nhận được khối nào, ta lập trình ghi ngay khối đó xuống ổ cứng (`fhand.write`) 
   rồi "xóa sạch" bộ nhớ tạm để đón khối tiếp theo. Nhờ vậy, máy tính có thể tải file vài GB 
   với lượng RAM tiêu thụ chỉ vài KB.
================================================================================
"""

import urllib.request
import urllib.parse
import urllib.error

# URL mục tiêu (file ảnh bìa sách)
url = 'http://data.pr4e.org/cover3.jpg'


# ------------------------------------------------------------------------------
# CÁCH 1: TẢI TOÀN BỘ FILE VÀO RAM CÙNG MỘT LÚC (Dành cho file nhỏ)
# ------------------------------------------------------------------------------
print("=== CÁCH 1: TẢI TOÀN BỘ FILE TRONG MỘT LẦN ===")

# Mở kết nối mạng và dùng .read() không tham số để nuốt trọn gói dữ liệu ảnh vào biến 'img'
img = urllib.request.urlopen(url).read()

# Mở một file cục bộ với chế độ "wb" (Ghi nhị phân)
fhand_simple = open('cover3_way1.jpg', 'wb')
fhand_simple.write(img) # Ghi một phát hết luôn
fhand_simple.close()

print("Đã tải xong bằng cách 1!")


# ------------------------------------------------------------------------------
# CÁCH 2: TẢI THEO TỪNG KHỐI (BUFFER) - GIẢI PHÁP CHO FILE LỚN (VIDEO, AUDIO)
# ------------------------------------------------------------------------------
print("\n=== CÁCH 2: TẢI THEO TỪNG KHỐI (AN TOÀN CHO BỘ NHỚ) ===")

# Bước A: Mở kết nối URL nhưng CHƯA gọi .read(), giữ nó ở dạng một luồng dữ liệu (Stream)
img_stream = urllib.request.urlopen(url)

# Bước B: Mở sẵn file lưu trữ trên ổ cứng
fhand_chunk = open('cover3_way2.jpg', 'wb')

# Khởi tạo biến đếm kích thước file thực tế nhận được
size = 0

# Bước C: Chạy vòng lặp vô hạn để "gặm" dần dữ liệu
while True:
    # Chỉ đọc đúng 100,000 bytes (~100 KB) từ luồng mạng đưa vào bộ nhớ tạm 'info'
    info = img_stream.read(100000)
    
    # Điều kiện dừng: Nếu không còn byte nào được trả về (< 1), tức là đã hết file
    if len(info) < 1:
        break
        
    # Tích lũy kích thước để theo dõi tiến trình
    size = size + len(info)
    
    # Ghi ngay khối dữ liệu vừa nhặt được xuống ổ cứng (RAM lập tức được giải phóng)
    fhand_chunk.write(info)

# Bước D: Dọn dẹp và đóng file sau khi vòng lặp kết thúc hoàn toàn
fhand_chunk.close()

print(f"Đã sao chép thành công: {size} characters (bytes) copied.")
print("File 'cover3_way2.jpg' đã sẵn sàng trong thư mục code.")