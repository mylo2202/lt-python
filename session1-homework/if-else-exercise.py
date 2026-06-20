try:
    hours = float(input("Nhập số giờ làm việc: "))

    rate = float(input("Nhập mức lương trên giờ: "))

    if hours < 0 or rate < 0:
        print("Số giờ và mức lương phải là số dương.")
    else:
        if hours <= 40:
            pay = hours * rate
        elif hours <= 70:
            pay = 40 * rate + (hours - 40) * rate * 1.5
        else:
            pay = 40 * rate + (70 - 40) * rate * 1.5 + (hours - 70) * rate * 2
        print(f"Tổng tiền lương của nhân viên: {pay:.2f}")

except ValueError:
    print("Vui lòng nhập số thực cho giờ làm.")

# print(help(print))


