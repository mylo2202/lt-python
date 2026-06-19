"""
Đoạn code này mô phỏng hoạt động cốt lõi của một Trình duyệt Web đơn giản nhất thế giới 
(The world's simplest web browser) bằng cách sử dụng thư viện Socket cấp thấp của Python.

Mục đích chính để hiểu rõ mô hình Client-Server và giao thức HTTP:
1. THIẾT LẬP KẾT NỐI (TCP): Tạo một Socket và thiết lập một "đường truyền vật lý" 
   tin cậy tới Máy chủ (Web Server) tại địa chỉ 'data.pr4e.org' qua cổng dịch vụ chuẩn 80.
2. GỬI YÊU CẦU (HTTP Request): Tự tay soạn một bức thư yêu cầu dạng văn bản thô theo 
   đúng cú pháp quy định của giao thức HTTP (sử dụng phương thức GET), mã hóa nó thành 
   dạng bytes rồi gửi đi qua đường truyền TCP.
3. NHẬN PHẢN HỒI (HTTP Response): Duy trì một vòng lặp liên tục để đọc dữ liệu trả về 
   từ máy chủ theo từng gói nhỏ (mỗi gói tối đa 512 bytes). Dữ liệu nhận được bao gồm 
   hai phần: HTTP Headers (thông tin cấu hình kỹ thuật của Server) và HTTP Body (nội dung 
   thực tế của file văn bản 'romeo.txt').
4. GIẢI PHÓNG TÀI NGUYÊN: Đóng kết nối sau khi quá trình truyền tải dữ liệu kết thúc.
================================================================================
"""

# 1. Nhập thư viện socket gốc của Python để làm việc với các kết nối mạng cấp thấp
import socket

# 2. Tạo đối tượng socket (đầu cuối kết nối).
# - socket.AF_INET: Chỉ định dùng hệ thống địa chỉ IPv4 toàn cầu.
# - socket.SOCK_STREAM: Chỉ định dùng giao thức truyền tin cậy TCP (dữ liệu đi theo dòng, không mất mát).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Thực hiện bước "Bắt tay 3 bước" (3-way handshake) để kết nối tới máy chủ qua cổng HTTP chuẩn là 80
mysock.connect(('data.pr4e.org', 80))

# 4. Định nghĩa chuỗi yêu cầu HTTP GET hợp lệ để xin tệp tin 'romeo.txt'.
# - Phải kết thúc bằng cặp ký tự xuống dòng đặc biệt '\r\n\r\n' để báo hiệu hết phần Request Header.
# - Hàm .encode() chuyển chuỗi văn bản (String) thành chuỗi byte nhị phân để có thể truyền qua cáp mạng.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# 5. Đẩy toàn bộ chuỗi byte dữ liệu của câu lệnh yêu cầu (Request) đi sang phía máy chủ
mysock.send(cmd)

# 6. Khởi động vòng lặp vô hạn để liên tục "hứng" dữ liệu phản hồi (Response) truyền về từ máy chủ
while True:
    # 7. Đọc một khối dữ liệu từ luồng mạng, kích thước bộ đệm (buffer) tối đa cho mỗi lần đọc là 512 bytes
    data = mysock.recv(512)
    
    # 8. Điều kiện dừng: Nếu độ dài khối dữ liệu nhận được < 1 byte, chứng tỏ máy chủ đã truyền xong và đóng kết nối
    if len(data) < 1:
        # Bẻ gãy vòng lặp để chuyển xuống lệnh đóng socket
        break
        
    # 9. Giải mã chuỗi bytes nhận được ngược thành ký tự văn bản (.decode()) và in ra màn hình.
    # Sử dụng tham số end='' để ngăn hàm print() tự động chèn thêm dấu xuống dòng của Python, giữ nguyên định dạng gốc của file.
    print(data.decode(), end='')

# 10. Đóng socket để giải phóng tài nguyên hệ thống và giải phóng cổng (port) trên máy tính Client
mysock.close()