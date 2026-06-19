"""
================================================================================
HỆ THỐNG TRÍCH XUẤT DỮ LIỆU TỰ ĐỘNG BẰNG BIỂU THỨC CHÍNH QUY (REGULAR EXPRESSIONS)
================================================================================
Mô tả bài toán (Kế thừa nội dung Slide Chapter 11 - Regular Expressions):
1. Bối cảnh: Xử lý tệp dữ liệu hỗn hợp (Email, Log hệ thống, Hóa đơn tài chính) 
   bằng thư viện 're' nhằm thay thế và nâng cấp các phương thức xử lý chuỗi cơ bản.
2. Hàm re.search(): Sử dụng ký tự neo dòng '^' để khớp điều kiện đầu dòng, mô phỏng 
   nâng cao tính năng tương đương với phương thức string.startswith().
3. Hàm re.findall(): Trích xuất toàn bộ các chuỗi con thỏa mãn mẫu định dạng mà 
   không cần sử dụng kỹ thuật cắt chuỗi thủ công (Slicing).
4. Ký tự đặc biệt (Greedy vs Non-Greedy & Special Characters):
   - '\\S+': Khớp với cụm ký tự liên tiếp không phải khoảng trắng (Non-blank).
   - '[0-9.]+': Khớp với một nhóm các ký tự số hoặc dấu chấm thập phân.
5. Kỹ thuật trích xuất trúng đích bằng Dấu ngoặc đơn '()': Định vị vùng dữ liệu 
   cần khớp để tìm kiếm, nhưng chỉ bóc tách riêng phần nội dung nằm trong ngoặc.
6. Ký tự thoát (Escape Character '\\'): Vô hiệu hóa ý nghĩa cú pháp hệ thống của 
   dấu '$' để tìm kiếm chính xác ký hiệu tiền tệ thực tế trong văn bản.
================================================================================
"""

import re  # Bước bắt buộc: Tích hợp thư viện biểu thức chính quy của Python

# Giả lập tài liệu văn bản thô, hỗn hợp thu thập từ hệ thống Email và Hóa đơn
raw_data = """
From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2026
X-DSPAM-Processed: Sat Jan  5 09:14:16 2026
X-DSPAM-Confidence: 0.8475
X-Content-Type-Message-Body: text/plain
Invoice Ref: #99214, Total Amount: $1550.25 paid via CreditCard.
From: louis@media.berkeley.edu Fri Jan  4 18:10:48 2026
X-DSPAM-Confidence: 0.6158
Invoice Ref: #99215, Total Amount: $420.00 pending.
"""

print("--- 1. RE.SEARCH() : THAY THẾ VÀ NÂNG CẤP STRING METHODS ---")
# Ký tự đặc biệt '^': Neo vị trí khớp tại điểm bắt đầu của một dòng văn bản
print("Các dòng chứa thông tin người gửi:")
for line in raw_data.split('\n'):
    # Kiểm tra dòng bắt đầu bằng 'From:'. Tương đương với line.startswith('From:')
    if re.search('^From:', line):
        print(f"  Tìm thấy: {line}")


print("\n--- 2. RE.FINDALL() : TRÍCH XUẤT EMAIL KHÔNG CẦN CẮT CHUỖI (SLICING) ---")
# Ý nghĩa cú pháp mẫu '\\S+@\\S+':
# - \\S : Đại diện cho bất kỳ ký tự nào KHÔNG PHẢI khoảng trắng (Non-whitespace character)
# - +   : Toán tử lặp lại, yêu cầu có ít nhất 1 hoặc nhiều ký tự liên tiếp thỏa mãn phía trước
# - @   : Ký tự đích bắt buộc phải xuất hiện cố định giữa hai cụm
emails = re.findall('\\S+@\\S+', raw_data)
print(f"Danh sách Email quét được tự động: {emails}")


print("\n--- 3. SỰ TINH TẾ CỦA DẤU NGOẶC ĐƠN () : CHỈ LẤY PHẦN CẦN THIẾT ---")
# Khái niệm Extraction: Dấu ngoặc đơn () quy định vùng trích xuất trúng đích (Sub-match).
# Hệ thống sẽ tìm kiếm theo toàn bộ biểu thức mẫu nhưng chỉ trả về dữ liệu nằm trong cặp ngoặc.

confidence_scores = []
for line in raw_data.split('\n'):
    # Mẫu tìm dòng bắt đầu bằng X-DSPAM-Confidence:, có 1 khoảng trắng, và theo sau là chuỗi số thực '[0-9.]+'
    # Cặp dấu () bao bọc lấy '[0-9.]+' giúp cô lập và chỉ trích xuất riêng phần số thực
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    
    if len(stuff) > 0:  # Điều kiện kiểm tra nếu danh sách kết quả không rỗng
        score = float(stuff[0])  # Ép kiểu phần tử chuỗi tìm thấy sang định dạng số thực (Float)
        confidence_scores.append(score)

print(f"Mảng số liệu Confidence để phân tích: {confidence_scores}")
print(f"Điểm tin cậy trung bình: {sum(confidence_scores) / len(confidence_scores)}")


print("\n--- 4. ESCAPE CHARACTER (KÍ TỰ THOÁT '\\') VÀ TRÍCH XUẤT DOANH THU ---")
# Trong cú pháp Regex, ký tự '$' mang ý nghĩa mặc định là "Neo tại vị trí cuối dòng" (End of line).
# Để bắt hệ thống tìm kiếm ký hiệu đồng đô-la thực tế, ta phải thêm dấu gạch chéo ngược '\\' phía trước để thoát chuỗi.

# Biểu thức '\\$([0-9.]+)': Tìm ký tự '$' thực tế, sau đó trích xuất nhóm chữ số và dấu chấm đi liền sau nó
amounts = re.findall('\\$([0-9.]+)', raw_data)
print(f"Danh sách số tiền hóa đơn quét được: {amounts}")