"""
================================================================================
HỆ THỐNG PHÂN TÍCH HIỆU SUẤT VÀ XẾP HẠNG KÊNH BÁN HÀNG (TUPLES & SORTING PROCESS)
================================================================================
Mô tả bài toán (Kế thừa nội dung Slide Chapter 10 - Tuples):
1. Khái niệm Tuple: Cấu trúc dữ liệu có thứ tự giống List nhưng mang tính chất 
   Bất biến (Immutable). Ứng dụng để bảo vệ tính toàn vẹn của dữ liệu gốc.
2. Cơ chế Tuple Unpacking: Kỹ thuật mở gói, phân rã nhanh các phần tử của Tuple 
   ra thành nhiều biến độc lập một cách đồng thời trên một dòng lệnh.
3. Cơ chế so sánh (Tuple Comparison): So sánh tuần tự từ trái qua phải. Gặp cặp 
   phần tử đầu tiên có sự khác biệt về giá trị sẽ dừng lại và ra kết quả.
4. Thuật toán xếp hạng Dictionary (Sorting by Value): Do Dictionary không thể 
   tự sắp xếp theo giá trị (Value), hệ thống áp dụng mẫu thiết lập đảo ngược: 
   Chuyển cấu trúc (Key, Value) thành cấu trúc Tuple (Value, Key) để sắp xếp.
5. List Comprehension: Kỹ thuật cô đọng cấu trúc vòng lặp và điều kiện, tối ưu 
   tốc độ thực thi và rút gọn mã nguồn về một dòng lệnh duy nhất.
================================================================================
"""

print("--- 1. TUPLE: SỰ KHÁC BIỆT CỐT LÕI VỚI LIST VÀ TÍNH BẤT BIẾN (IMMUTABLE) ---")
# Khởi tạo một Tuple hằng số bằng cặp dấu ngoặc đơn () thay vì dấu ngoặc vuông []
channel_info = ('E-commerce', 'Hanoi', 45000)
print(f"Thông tin kênh: {channel_info}")
print(f"Tên kênh: {channel_info[0]} | Doanh thu: ${channel_info[2]}")

# Khối Try/Except kiểm thử đặc tính bất biến của Tuple
try:
    # Lệnh gán này sẽ phát sinh lỗi hệ thống vì Tuple không hỗ trợ thay đổi giá trị phần tử
    channel_info[2] = 50000 
except TypeError:
    print("[An Toàn] Lỗi: Tuple là BẤT BIẾN! Không cho phép thay đổi dữ liệu gốc sau khi khởi tạo.")


print("\n--- 2. TUPLE UNPACKING (MỞ GÓI) & COMPARISON (CƠ CHẾ SO SÁNH) ---")
# Kỹ thuật Tuple Unpacking: Phân rã cấu trúc mảng để gán đồng thời cho 3 biến độc lập
name, city, revenue = channel_info
print(f"Mở gói thành công -> Thành phố: {city} | Doanh thu: ${revenue}")

# Cơ chế so sánh: Quét từ trái sang phải, so sánh cặp phần tử đầu tiên (100 và 90). 
# Do 100 > 90 là Đúng (True), thuật toán dừng lại và kết luận, bỏ qua các phần tử chữ phía sau.
print(f"So sánh Tuple (100, 'Apple') > (90, 'Zebra'): {(100, 'Apple') > (90, 'Zebra')}")


print("\n--- 3. ỨNG DỤNG TUPLE ĐỂ XẾP HẠNG DICTIONARY (SẮP XẾP THEO VALUE) ---")
# Khởi tạo Dictionary chứa dữ liệu thô (Key là tên kênh, Value là doanh thu)
channel_sales = {'Retail': 15000, 'E-commerce': 45000, 'Wholesale': 35000, 'Agent': 12000}

# Khởi tạo danh sách rỗng để chứa các Tuple đảo ngược phục vụ sắp xếp
temp_list = list()

# Sử dụng phương thức .items() để duyệt qua từng cặp cấu trúc (Key, Value) của Dictionary
for key, val in channel_sales.items():
    # Kỹ thuật đảo vị trí: Đưa giá trị số (val) lên trước để làm tiêu chí so sánh, nhãn (key) ra sau
    new_tuple = (val, key) 
    temp_list.append(new_tuple)

print(f"Danh sách (Value, Key) trước khi xếp hạng:\n {temp_list}")

# Hàm sorted(): Sắp xếp lại danh sách Tuple. Tham số reverse=True quy định xếp giảm dần
ranked_list = sorted(temp_list, reverse=True)
print(f"Danh sách sau khi đã xếp hạng giảm dần:\n {ranked_list}")

# Kỹ thuật Slicing [:3]: Trích xuất phân đoạn lấy đúng 3 phần tử đầu tiên có giá trị cao nhất
print("\n🏆 BÁO CÁO TOP 3 KÊNH DOANH THU CAO NHẤT:")
for val, key in ranked_list[:3]:
    print(f"- Kênh: {key:<12} | Doanh thu đạt: ${val}")


print("\n--- 4. PHIÊN BẢN RÚT GỌN CHUYÊN NGHIỆP (LIST COMPREHENSION) ---")
# Tối ưu hóa mã nguồn: Gom toàn bộ quy trình duyệt vòng lặp, tạo tuple đảo ngược 
# và chuyển bảng thành danh sách sắp xếp giảm dần vào trong một dòng lệnh duy nhất.
shortcut_sorted = sorted([ (v, k) for k, v in channel_sales.items() ], reverse=True)

print(f"Kết quả rút gọn (Top 2): {shortcut_sorted[:2]}")