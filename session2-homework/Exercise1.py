def kiem_tra_hop_le(ma_don):
    # tự động làm sạch các khoảng trắng thừa ở hai đầu (nếu có)
    ma_don_clean = ma_don.strip()
    
    # phân tách chuỗi thành các thành phần thông tin độc lập dựa trên ký tự gạch ngang (-)
    parts = ma_don_clean.split('-')
    
    # Điều kiện 1: Chứa chính xác 5 thành phần thông tin sau khi phân tách.
    if len(parts) != 5:
        return False
        
    # chuyển thành chữ thường để so sánh không phân biệt hoa/thường
    quoc_gia = parts[0].lower()
    trong_luong_str = parts[3].lower()
    
    # Điều kiện 2: Mã quốc gia bắt buộc phải là VN hoặc US (không phân biệt hoa/thường).
    if quoc_gia not in ['vn', 'us']:
        return False
        
    # Điều kiện 3: Định dạng trọng lượng bắt buộc phải có phần hậu tố là KG (không phân biệt hoa/thường).
    if not trong_luong_str.endswith('kg'):
        return False

    return True

def tinh_phi(trong_luong_str, trang_thai):
    # bỏ chữ 'kg' ở cuối string trọng lượng để lấy phần số
    trong_luong_clean = trong_luong_str.strip().lower()
    if trong_luong_clean.endswith('kg'):
        so_str = trong_luong_clean[:-2]
    else:
        so_str = trong_luong_clean
        
    # Đảm bảo an toàn cho chương trình: Nếu phần giá trị số bị lỗi định 
    # dạng (ví dụ người dùng nhập abcKG), chương trình không được phép 
    # gián đoạn. Thay vào đó, cần in ra thông báo cảnh báo lỗi dữ liệu và 
    # quy định mức phí của đơn hàng đó bằng 0.
    try:
        trong_luong = float(so_str)
        if trong_luong < 0:
            print("Cảnh báo: Trọng lượng không được âm. Đặt phí bằng 0.")
            return 0
    except ValueError:
        print("Cảnh báo: Lỗi định dạng trọng lượng. Đặt phí bằng 0.")
        return 0

    # Công thức tính phí: Cước phí cơ bản là 15,000 VND cho mỗi 1 kg.
    cuoc_co_ban = trong_luong * 15000
    
    # Phụ phí thanh toán: Nếu trạng thái là COD (thu hộ), cộng thêm 10,000
    # VND. Nếu trạng thái là PAID, không cộng thêm phụ phí.
    phu_phi = 0
    trang_thai_clean = trang_thai.strip().lower()
    if trang_thai_clean == 'cod':
        phu_phi = 10000
    elif trang_thai_clean == 'paid':
        phu_phi = 0
        
    return cuoc_co_ban + phu_phi

def main():
    tong_so_don_hop_le = 0
    tong_doanh_thu = 0

    # Khi khởi chạy, chương trình cần hiển thị một menu liên tục
    while True:
        print("\n=== Logistics analyzer ===")
        print("[1] Xử lý mã vận đơn")
        print("[2] Thống kê")
        print("[3] Thoát")
        
        choice = input("Lựa chọn của bạn: ").strip()
        
        if choice == '1':
            while True:
                ma_don = input("Nhập mã vận đơn (gõ 'done' để quay lại menu): ")
                if ma_don.strip().lower() == 'done':
                    break
                
                if not kiem_tra_hop_le(ma_don):
                    print("Cảnh báo: Mã vận đơn không đúng định dạng. Vui lòng nhập lại.")
                else:
                    ma_don_clean = ma_don.strip()
                    parts = ma_don_clean.split('-')
                    quoc_gia = parts[0].upper()
                    chi_nhanh = parts[1]
                    ma_don_hang = parts[2]
                    trong_luong_str = parts[3]
                    trang_thai = parts[4]

                    phi = tinh_phi(trong_luong_str, trang_thai)

                    print(f"-> Mã hợp lệ:")
                    print(f"- Quốc gia: {quoc_gia}")
                    print(f"- Chi nhánh: {chi_nhanh}")
                    print(f"- Mã đơn: {ma_don_hang}")
                    print(f"- Trọng lượng thực tế: {trong_luong_str}")
                    print(f"- Tổng phí: {phi:,.0f} VND")

                    # cộng dồn thống kê
                    tong_so_don_hop_le += 1
                    tong_doanh_thu += phi

        elif choice == '2':
            print("\n=== THỐNG KÊ ===")
            print(f"Tổng số lượng mã vận đơn hợp lệ: {tong_so_don_hop_le}")
            print(f"Tổng doanh thu: {tong_doanh_thu:,.0f} VND")
            
        elif choice == '3':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại [1], [2], hoặc [3].")

if __name__ == "__main__":
    main()
