"""
================================================================================
HỆ THỐNG PHÂN TÍCH TẦN SUẤT VÀ THỐNG KÊ DOANH SỐ SẢN PHẨM (DICTIONARY PROCESS)
================================================================================
Mô tả bài toán (Kế thừa nội dung Slide Chapter 9 - Dictionaries):
1. Khái niệm Dictionary: Cấu trúc dữ liệu lưu trữ dưới dạng "Nhãn - Giá trị" 
   (Key - Value) thay vì chỉ mục bằng số như List.  Cho phép truy xuất dữ liệu 
   cực nhanh như một cơ sở dữ liệu thu nhỏ.
2. Tính Mutability (Có thể thay đổi): Có thể thêm mới hoặc cập nhật giá trị 
   của một Key đang tồn tại trong Dictionary một cách dễ dàng.
3. Mẫu thuật toán Đếm (Histogram Pattern): Ứng dụng kinh điển nhất của Dictionary 
   để đếm tần suất xuất hiện của các phần tử trong danh sách dữ liệu thô.
4. Phương thức .get(): "Vũ khí tối thượng" giúp lấy giá trị an toàn. Cung cấp 
   giá trị mặc định nếu Key chưa tồn tại, giúp rút gọn code từ 4 dòng xuống 1 dòng.
5. Cơ chế duyệt (Looping với hai biến): Sử dụng .items() để lấy đồng thời 
   cả Key và Value, kết hợp thuật toán tìm kiếm phần tử có giá trị cao nhất (Maximum).
================================================================================
"""

print("--- 1. DICTIONARY: KHỞI TẠO, TRUY XUẤT VÀ CẬP NHẬT ---")
# Khởi tạo Dictionary rỗng để lưu trữ tồn kho hiện tại (Có thể dùng dict() hoặc {})
ton_kho = dict()

# Thêm dữ liệu vào Dictionary: Gán Value thông qua Nhãn (Key)
ton_kho['Laptop'] = 15
ton_kho['Mouse'] = 45
ton_kho['Keyboard'] = 20

print(f"Báo cáo tồn kho ban đầu: {ton_kho}")
print(f"Truy xuất nhanh số lượng Chuột (Mouse): {ton_kho['Mouse']} chiếc")

# Tính Mutability: Cập nhật lại giá trị cho một Key đã tồn tại
ton_kho['Mouse'] = ton_kho['Mouse'] + 5  # Vừa nhập kho thêm 5 con chuột
print(f"Báo cáo tồn kho sau khi nhập thêm: {ton_kho}")


print("\n--- 2. MẪU THUẬT TOÁN ĐẾM (HISTOGRAM) & PHƯƠNG THỨC GET() ---")
# Giả sử chúng ta trích xuất được một Danh sách (List) các mặt hàng đã bán trong ngày
hang_da_ban = ['Laptop', 'Mouse', 'Monitor', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Mouse', 'Keyboard']
print(f"Danh sách dữ liệu bán hàng thô: \n{hang_da_ban}")

# Khởi tạo Dictionary rỗng để làm bảng thống kê đếm số lượng
doanh_so = dict()

# Vòng lặp duyệt qua từng sản phẩm trong dữ liệu thô
for sp in hang_da_ban:
    # Phương thức .get(sp, 0): Lấy số lượng hiện tại của 'sp' trong Dictionary.
    # Nếu 'sp' chưa từng xuất hiện (chưa có Key), hệ thống tự động trả về giá trị mặc định là 0.
    # Sau đó cộng thêm 1 cho lần xuất hiện này và lưu ngược lại vào Dictionary.
    doanh_so[sp] = doanh_so.get(sp, 0) + 1

print(f"Bảng thống kê số lượng bán ra đã gom nhóm: \n{doanh_so}")


print("\n--- 3. DUYỆT DICTIONARY KÉP (.ITEMS) & TÌM SẢN PHẨM BEST-SELLER ---")
# Khởi tạo các biến để lưu trữ sản phẩm bán chạy nhất (Thuật toán tìm Max)
best_seller = None
max_count = None

print("Báo cáo chi tiết từng mặt hàng:")
# Phương thức .items() trả về đồng thời cặp (Key, Value), giúp ta dùng 2 biến lặp (sp, count)
for sp, count in doanh_so.items():
    # In ra với định dạng căn lề :<10 để bảng báo cáo đẹp mắt hơn
    print(f"- Sản phẩm: {sp:<10} | Số lượng đã bán: {count}")
    
    # Logic tìm Maximum: Nếu là vòng lặp đầu tiên (max_count is None) 
    # HOẶC số lượng hiện tại lớn hơn số lượng kỷ lục cũ -> Cập nhật lại kỷ lục
    if max_count is None or count > max_count:
        max_count = count
        best_seller = sp

print("-" * 55)
print(f"🏆 KẾT LUẬN: Sản phẩm BÁN CHẠY NHẤT hôm nay là '{best_seller}' với {max_count} chiếc.")