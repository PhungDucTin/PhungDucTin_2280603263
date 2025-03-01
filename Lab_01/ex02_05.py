so_gio_lam = float(input("Nhập số giờ làm việc của nhân viên trong tuần: "))
muc_luong_hoi = float(input("Nhập mức lươnng theo giờ tiêu chuẩn: "))
gio_tieu_chuan = 44
if so_gio_lam <= gio_tieu_chuan:
    tien_thuc_nhan = so_gio_lam * muc_luong_hoi 
else:
    gio_lam_them = so_gio_lam - gio_tieu_chuan
    tien_thuc_nhan = (gio_tieu_chuan * muc_luong_hoi) + (gio_lam_them * muc_luong_hoi * 1.5)
print("Số tiền nhân viên thực nhận trong tuần là: ", tien_thuc_nhan)
