import json
import urllib.request
import urllib.error

API_URL = "https://open.er-api.com/v6/latest/USD"


def fetch_rates():
    try:
        with urllib.request.urlopen(API_URL, timeout=10) as response:
            raw = response.read().decode("utf-8")
            data = json.loads(raw)
            if data.get("result") != "success":
                raise ValueError("Không lấy được dữ liệu tỷ giá từ API.")
            return data.get("rates", {})
    except urllib.error.HTTPError as e:
        print(f"Lỗi HTTP khi gọi API: {e.code} {e.reason}")
    except urllib.error.URLError as e:
        print(f"Lỗi kết nối API: {e.reason}")
    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    return {}

def get_vnd_rate(rates, currency_code):
    currency_code = currency_code.upper()
    if currency_code not in rates or "VND" not in rates:
        return None
    if currency_code == "USD":
        return rates["VND"]
    foreign_rate = rates[currency_code]
    vnd_rate = (1 / foreign_rate) * rates["VND"]
    return vnd_rate


def fetch_and_validate_currency(currency_code):
    currency_code = currency_code.upper()
    rates = fetch_rates()
    if not rates:
        print("Không thể lấy dữ liệu tỷ giá. Vui lòng thử lại sau.")
        return None

    if currency_code not in rates:
        print(f"Mã ngoại tệ '{currency_code}' không hợp lệ hoặc không có trong dữ liệu API.")
        return None

    vnd_rate = get_vnd_rate(rates, currency_code)
    if vnd_rate is None:
        print("Không tìm thấy tỷ giá VND trong dữ liệu API.")
        return None

    return vnd_rate


def function_lookup_rate():
    currency_code = input("Nhập mã ngoại tệ cần tra cứu (VD: USD, EUR, JPY): ").strip().upper()
    if not currency_code:
        print("Vui lòng nhập mã ngoại tệ hợp lệ.")
        return
    vnd_rate = fetch_and_validate_currency(currency_code)
    if vnd_rate is None:
        return

    if currency_code == "USD":
        print(f"1 USD = {vnd_rate} VND")
    else:
        print(f"1 {currency_code} = {int(vnd_rate)} VND")


def function_calculate_order_cost():
    currency_code = input("Nhập mã ngoại tệ thanh toán (Ví dụ: EUR, JPY): ").strip().upper()
    if not currency_code:
        print("Vui lòng nhập mã ngoại tệ hợp lệ.")
        return

    amount_text = input(f"Nhập giá gốc đơn hàng (bằng {currency_code}): ").strip()
    try:
        amount = float(amount_text.replace(",", ""))
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Giá trị gốc phải là một số lớn hơn hoặc bằng 0.")
        return

    vnd_rate = fetch_and_validate_currency(currency_code)
    if vnd_rate is None:
        return

    amount_vnd = amount * vnd_rate
    import_tax = amount_vnd * 0.10
    total_cost = amount_vnd + import_tax

    print("\n=== KẾT QUẢ PHÂN TÍCH CHI PHÍ ĐƠN HÀNG ===")
    print(f"Tỷ giá áp dụng: 1 {currency_code} = {round(vnd_rate):,} VND")
    print(f"Giá gốc đơn hàng: {round(amount):,} {currency_code}")
    print(f"Quy đổi sang VND: {round(amount_vnd):,} VND (Chưa thuế)")
    print(f"Thuế nhập khẩu (10%): {round(import_tax):,} VND")
    print(f"Tổng chi phí doanh nghiệp phải trả (đã gồm thuế): {round(total_cost):,} VND")
    print("===========================================\n")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ CHI PHÍ NGOẠI TỆ DOANH NGHIỆP ===")
        print("1. Tra cứu nhanh tỷ giá ra VND")
        print("2. Tính toán chi phí đơn hàng nhập khẩu (có thuế)")
        print("3. Thoát chương trình")
        choice = input("Chọn chức năng (1-3): ").strip()

        if choice == "1":
            function_lookup_rate()
        elif choice == "2":
            function_calculate_order_cost()
        elif choice == "3":
            print("Kết thúc chương trình. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")


if __name__ == "__main__":
    main()
