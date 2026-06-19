"""
================================================================================
ĐỀ BÀI: LÀM SẠCH VÀ PHÂN TÍCH DOANH THU KINH DOANH CHUỖI CỬA HÀNG
================================================================================

1. BỐI CẢNH THỰC TẾ:
   Bạn đang đảm nhận vai trò Quản lý Phân tích Dữ liệu của một chuỗi siêu thị. 
   Hệ thống máy POS cũ tại chi nhánh xuất ra một tệp dữ liệu thô dạng văn bản ghi 
   lại doanh thu theo từng ngày. Tuy nhiên, do lỗi đồng bộ hoặc do cửa hàng đóng 
   cửa nghỉ lễ, dữ liệu thu được bị lẫn các ký tự nhiễu như "CLOSED", "ERR_SYSTEM", 
   hoặc "N/A".

2. NHIỆM VỤ CỦA HỌC VIÊN:
   Viết một chương trình Python ứng dụng cấu trúc dữ liệu List (Danh sách) để:
   - Nhiệm vụ 1 (Làm sạch dữ liệu): Duyệt qua tập dữ liệu thô, sử dụng phương thức 
     split() để bóc tách thông tin, loại bỏ các dòng lỗi và dùng phương thức 
     append() để gom các giá trị doanh thu hợp lệ vào một List mới.
   - Nhiệm vụ 2 (Phân tích thống kê): Sử dụng các hàm dựng sẵn tương tác với List 
     như len(), sum(), max(), min() để tính toán các chỉ số kinh doanh cốt lõi.
   - Nhiệm vụ 3 (Tối ưu vận hành): Sử dụng phương thức sort() và kỹ thuật cắt mảng 
     (Slicing) để tìm ra Top 3 ngày có doanh thu thấp nhất, phục vụ báo cáo quản trị.

3. MỤC TIÊU KIẾN THỨC (SLIDE CHƯƠNG 8):
   - Hiểu bản chất của List như một "Collection" (Bộ sưu tập dữ liệu).
   - Sử dụng vòng lặp 'for' duyệt List và kỹ thuật bắt lỗi Try-Except.
   - Thành thạo các hàm toán học của List và kỹ thuật Slicing mảng [start:end].
================================================================================
"""

# 1. Tập dữ liệu thô mô phỏng từ hệ thống POS
# Định dạng chuỗi: "Ngày, Tên_Cửa_Hàng, Doanh_Thu_(Triệu_Đồng)"
raw_sales_data = [
    "2026-01-01, Store_HaNoi, 45.5",
    "2026-01-02, Store_HaNoi, 48.2",
    "2026-01-03, Store_HaNoi, CLOSED",       # Ngày nghỉ lễ
    "2026-01-04, Store_HaNoi, 52.0",
    "2026-01-05, Store_HaNoi, ERR_SYSTEM",   # Lỗi mất kết nối máy POS
    "2026-01-06, Store_HaNoi, 39.8",
    "2026-01-07, Store_HaNoi, 61.4",
    "2026-01-08, Store_HaNoi, N/A"           # Nhân viên quên nhập số liệu
]

# Khởi tạo một List rỗng để tích lũy dữ liệu doanh thu hợp lệ (Collection)
clean_revenue_list = list()

print("--- BƯỚC 1: TIẾN HÀNH LÀM SẠCH DỮ LIỆU THÔ ---")

for line in raw_sales_data:
    # Tách chuỗi văn bản dựa trên dấu phẩy để phân rã các trường thông tin
    pieces = line.split(',')
    
    # Trích xuất phần tử doanh thu (vị trí index = 2) và xóa khoảng trắng thừa
    revenue_str = pieces[2].strip()
    
    # Sử dụng Try-Except để sàng lọc dữ liệu bẩn
    try:
        # Ép kiểu sang số thực float, nếu là chữ ("CLOSED", "N/A"...) sẽ nhảy vào except
        revenue_data = float(revenue_str)
        
        # Thêm dữ liệu đã làm sạch vào danh sách tổng hợp
        clean_revenue_list.append(revenue_data)
        print(f"Hợp lệ -> Ngày {pieces[0]}: Doanh thu đạt {revenue_data} triệu VNĐ")
        
    except ValueError:
        # Thông báo và bỏ qua các dữ liệu lỗi không thể phân tích
        print(f"CẢNH BÁO -> Ngày {pieces[0]}: Phát hiện dữ liệu nhiễu ('{revenue_str}'). Đã loại bỏ.")


print("\n--- BƯỚC 2: PHÂN TÍCH THỐNG KÊ KINH DOANH (LIST FUNCTIONS) ---")

# Kiểm tra điều kiện bảo vệ (Đảm bảo danh sách không rỗng trước khi tính toán)
if len(clean_revenue_list) > 0:
    
    # Tối ưu hóa tính toán bằng các hàm tích hợp sẵn (Built-in Functions) của List
    total_days = len(clean_revenue_list)        # Đếm số phần tử (số ngày hợp lệ)
    total_revenue = sum(clean_revenue_list)     # Tính tổng các phần tử trong List
    max_rev = max(clean_revenue_list)           # Tìm giá trị lớn nhất
    min_rev = min(clean_revenue_list)           # Tìm giá trị nhỏ nhất
    avg_rev = total_revenue / total_days        # Tính toán giá trị trung bình doanh thu
    
    print(f"📊 BÁO CÁO HIỆU SUẤT DOANH THU:")
    print(f"- Tổng số ngày ghi nhận số liệu: {total_days} ngày")
    print(f"- Tổng doanh thu toàn giai đoạn: {total_revenue} triệu VNĐ")
    print(f"- Doanh thu trung bình mỗi ngày: {avg_rev:.2f} triệu VNĐ")
    print(f"- Biên độ dao động doanh thu: Từ {min_rev} đến {max_rev} triệu VNĐ")

    print("\n--- BƯỚC 3: HOẠCH ĐỊNH CHIẾN LƯỢC QUẢN TRỊ (SORT & SLICING) ---")
    
    # Sắp xếp lại danh sách theo thứ tự tăng dần trực tiếp trên List gốc
    clean_revenue_list.sort()
    
    # Áp dụng kỹ thuật Slicing List để lấy ra 3 phần tử đầu tiên (3 mức thấp nhất)
    top_3_lowest = clean_revenue_list[0:3]
    
    print(f"⚠️ ĐỀ XUẤT CHO BAN GIÁM ĐỐC:")
    print(f"- Danh sách doanh thu sau sắp xếp: {clean_revenue_list}")
    print(f"- Top 3 mức doanh thu thấp nhất cần rà soát vận hành: {top_3_lowest}")
    print("👉 Khuyến nghị: Cần tối ưu lại chi phí nhân sự hoặc đẩy mạnh chương trình marketing vào các ngày này.")

else:
    print("Hệ thống kiểm tra lỗi: Không tìm thấy dữ liệu hợp lệ để thực hiện phân tích.")