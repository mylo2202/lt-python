"""
NHÓM 4,5,6: XÂY DỰNG CÔNG CỤ THEO DÕI NĂNG SUẤT VÀ QUẢN LÝ NHÂN SỰ TOÀN CẦU (HR / IT)
"""

import urllib.request
import json

BASE_URL = "https://time.now/developer/api/timezone"

TEN_NGAY_TRONG_TUAN = {
    0: "Chủ Nhật",
    1: "Thứ Hai",
    2: "Thứ Ba",
    3: "Thứ Tư",
    4: "Thứ Năm",
    5: "Thứ Sáu",
    6: "Thứ Bảy",
}

def goi_api(url):
    """Gọi API và trả về dữ liệu JSON đã được parse."""
    try:
        # req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            du_lieu_text = response.read().decode("utf-8")
            return json.loads(du_lieu_text)
    except urllib.error.URLError as e:
        print(f"[LỖI] Không thể kết nối API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"[LỖI] Dữ liệu API không hợp lệ: {e}")
        return None


def in_duong_ke(ky_tu="=", do_dai=60):
    """In đường kẻ phân cách."""
    print(ky_tu * do_dai)


def chuc_nang_1_liet_ke_mui_gio():
    """Liệt kê 10 vùng múi giờ đầu tiên từ API."""
    in_duong_ke()
    print("Chức năng 1: Liệt kê các khu vực múi giờ hệ thống hỗ trợ")
    in_duong_ke()

    print("Đang gọi API để lấy danh sách múi giờ...")
    danh_sach = goi_api(BASE_URL)

    if danh_sach is None:
        print("Không thể lấy danh sách múi giờ. Vui lòng thử lại.\n")
        return

    print(f"\nHệ thống hỗ trợ tổng cộng {len(danh_sach)} vùng múi giờ.")
    print("Dưới đây là 10 vùng múi giờ đầu tiên để tham khảo:\n")

    for idx, ten_vung in enumerate(danh_sach[:10], start=1):
        print(f"{idx:>2}. {ten_vung}")

    print()

def chuc_nang_2_kiem_tra_gio_lam_viec():
    """Kiểm tra giờ làm việc của nhân sự tại một vùng múi giờ."""
    in_duong_ke()
    print("Chức năng 2: Kiểm tra giờ làm việc của nhân sự nước ngoài")
    in_duong_ke()

    print("Ví dụ tên vùng múi giờ: America/New_York, Europe/London, Asia/Tokyo")
    ten_vung = input("Nhập tên vùng múi giờ: ").strip()

    if not ten_vung:
        print("[LỖI] Tên vùng không được để trống.\n")
        return

    # Gọi API chi tiết
    url_chi_tiet = f"{BASE_URL}/{ten_vung}"
    print(f"\nĐang gọi API cho vùng '{ten_vung}'...")
    du_lieu = goi_api(url_chi_tiet)

    if du_lieu is None:
        print(f"Không tìm thấy thông tin cho vùng '{ten_vung}'.")
        print("Vui lòng kiểm tra lại tên vùng múi giờ (phân biệt chữ hoa/thường).\n")
        return

    # Bóc tách dữ liệu
    chuoi_datetime = du_lieu.get("datetime", "")
    day_of_week = du_lieu.get("day_of_week", -1)
    utc_offset = du_lieu.get("utc_offset", "N/A")

    # Lấy phần thời gian: bóc tách phần "HH:MM:SS"
    try:
        # Tách phần sau "T"
        phan_thoi_gian = chuoi_datetime.split("T")[1]
        # Lấy 8 ký tự đầu: "HH:MM:SS"
        phan_gio_phut_giay = phan_thoi_gian[:8]
        gio, phut, giay = [int(x) for x in phan_gio_phut_giay.split(":")]
    except (IndexError, ValueError):
        print(f"[LỖI] Không thể parse chuỗi thời gian: '{chuoi_datetime}'\n")
        return

    ten_ngay = TEN_NGAY_TRONG_TUAN.get(day_of_week, "Không xác định")

    # Giờ làm việc: 08:00 đến 17:00
    if 8 <= gio < 17:
        trang_thai = "Đang trong giờ làm việc - Có thể đặt lịch họp"
        co_the_hop = True
    else:
        trang_thai = "Đã hết giờ làm việc / Giờ nghỉ - Không đặt lịch họp"
        co_the_hop = False

    # In báo cáo gửi phòng HR
    in_duong_ke("-", 60)
    print("BÁO CÁO GỬI PHÒNG HR")
    in_duong_ke("-", 60)
    print(f"Vùng quản lý           : {ten_vung}")
    print(f"Giờ hiện tại           : {gio:02d}:{phut:02d}:{giay:02d}")
    print(f"Ngày trong tuần        : {ten_ngay}")
    print(f"Múi giờ (UTC)          : {utc_offset}")
    print(f"Trạng thái liên lạc    : {trang_thai}")
    in_duong_ke("-", 60)

    if co_the_hop:
        print("Khuyến nghị: Có thể liên hệ và đặt lịch họp với nhân sự tại vùng này.")
    else:
        print("Khuyến nghị: Tránh đặt lịch họp. Chờ đến khung 08:00 - 17:00 giờ địa phương.")

    print()

def main():
    """menu tương tác"""
    while True:
        in_duong_ke("=", 60)
        print("CÔNG CỤ THEO DÕI NĂNG SUẤT VÀ QUẢN LÝ NHÂN SỰ TOÀN CẦU (HR / IT)")
        in_duong_ke("=", 60)
        print("[1] Liệt kê các khu vực múi giờ hệ thống hỗ trợ")
        print("[2] Kiểm tra giờ làm việc của nhân sự nước ngoài")
        print("[3] Thoát chương trình")
        in_duong_ke("=", 60)
        lua_chon = input("Nhập lựa chọn của bạn (1/2/3): ").strip()

        if lua_chon == "1":
            chuc_nang_1_liet_ke_mui_gio()

        elif lua_chon == "2":
            chuc_nang_2_kiem_tra_gio_lam_viec()

        elif lua_chon == "3":
            in_duong_ke()
            print("Cám ơn bạn đã sử dụng chương trình.")
            in_duong_ke()
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.\n")


if __name__ == "__main__":
    main()
