"""
================================================================================
Bóc tách HTML bằng Regular Expression
================================================================================
Đoạn code này mô phỏng một "Web Crawler" sơ khai. Sau khi tải mã nguồn HTML của một 
trang web về, chương trình sẽ dùng công cụ Regex để tự động "quét" và trích xuất ra 
tất cả các đường link (URLs) ẩn bên trong mã HTML đó.

Các trọng tâm kiến thức:
1. BỎ QUA CHỨNG CHỈ SSL: Thực tế ngày nay hầu hết các trang web đều dùng HTTPS. 
   Thư viện `ssl` giúp ta cấu hình để Python bỏ qua các lỗi xác thực chứng chỉ bảo mật, 
   tránh cho chương trình bị ngắt giữa chừng khi truy cập các trang HTTPS.
2. CÚ PHÁP REGEX TRÍCH XUẤT LINK: `href="http[s]?://.+?"`
   - `http[s]?`: Tìm chữ "http", chữ "s" có thể có hoặc không (khớp cả http và https).
   - `://`: Tìm chính xác cụm ký tự "://".
   - `.+?`: Tìm một hoặc nhiều ký tự bất kỳ (`.+`), nhưng phải dừng lại ngay khi gặp 
     dấu nháy kép tiếp theo (`?` - chế độ non-greedy / không tham lam).
   - Cặp dấu ngoặc đơn `(...)`: Đánh dấu vùng dữ liệu mục tiêu cần trích xuất (chỉ lấy 
     cái ruột URL, bỏ chữ `href="` bên ngoài).
================================================================================
"""

import urllib.request
import urllib.parse
import urllib.error
import re # 1. Nhập thư viện Regular Expressions (re) chuyên dùng để tìm kiếm chuỗi theo mẫu
import ssl # 2. Nhập thư viện mã hóa bảo mật SSL để xử lý các trang web HTTPS

# 3. CẤU HÌNH BỎ QUA LỖI CHỨNG CHỈ SSL (Bắt buộc phải có khi cào dữ liệu web hiện đại)
# Tạo một ngữ cảnh mặc định nhưng tắt tính năng kiểm tra tên miền và chứng chỉ bảo mật
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 4. Yêu cầu người dùng nhập URL cần thu thập dữ liệu (Ví dụ nhập: http://www.dr-chuck.com/page1.htm)
url = input('Enter - ')

# 5. Mở URL với cấu hình ngữ cảnh SSL đã thiết lập, đọc toàn bộ mã HTML về dưới dạng chuỗi bytes
html = urllib.request.urlopen(url, context=ctx).read()

# 6. SỬ DỤNG REGEX ĐỂ TÌM TẤT CẢ CÁC ĐƯỜNG LINK
# - Vì biến 'html' đang ở dạng bytes, nên biểu thức mẫu Regex cũng phải đặt chữ 'b' phía trước (b'...')
# - Hàm re.findall() sẽ quét toàn bộ mã nguồn HTML và trả về một DANH SÁCH (List) chứa các chuỗi khớp mẫu
links = re.findall(b'href="http[s]?://.+?"', html)

print("\n--- CÁC ĐƯỜNG LINK TÌM THẤY ---")

# 7. Vòng lặp duyệt qua danh sách các đường link đã bóc tách được
for link in links:
    # Giải mã chuỗi bytes thành dạng chuỗi ký tự thông thường và in ra màn hình
    print(link.decode())