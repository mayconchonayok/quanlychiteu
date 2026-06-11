# Quản lý chi tiêu cá nhân

Bài tập Kỹ thuật lập trình - nhóm làm app console để quản lý thu/chi, danh mục, ngân sách và báo cáo.

## Chạy chương trình

```bash
python3 main.py
```

Nếu muốn xuất biểu đồ cột/tròn:

```bash
pip3 install matplotlib
```

## Các file chính

```text
data_structures.py   DynamicArray, LinkedList tự cài
models.py            Transaction, Category, Budget
transaction.py       Thêm, sửa, xóa, tìm giao dịch
category.py          Thêm, sửa, xóa danh mục; tìm tuần tự; bubble sort
budget.py            Đặt ngân sách, kiểm tra vượt hạn mức
report.py            Tổng thu/chi, báo cáo tháng, ASCII chart, cache
fileio.py            Đọc/ghi file bằng split/strip, không dùng json
export_report.py     Xuất TXT, CSV, biểu đồ cột/tròn
validators.py        Kiểm tra dữ liệu nhập
app.py               Menu chính và gọi các module
main.py              File chạy chương trình
tests/test_report.py Test nhanh cho báo cáo và ngân sách
```

## Kỹ thuật đã dùng

- Top-down: từ `main.py` -> `app.py` -> từng module nhỏ.
- OOP: có các lớp `Transaction`, `Category`, `Budget`, `DynamicArray`, `LinkedList`.
- Cấu trúc dữ liệu tự cài: giao dịch lưu bằng `LinkedList`, danh mục và ngân sách lưu bằng `DynamicArray`.
- Modular: mỗi phần tách thành file riêng theo nhiệm vụ.
- Defensive programming: kiểm tra ngày, tháng, số tiền, chuỗi rỗng, lựa chọn menu và dữ liệu file lỗi.
- Debugging: có ghi log vào `app.log`.
- Testing: có test mẫu trong thư mục `tests`.
- Code tuning: dùng cache cho báo cáo, cộng chi tiêu theo danh mục bằng bảng tạm.
- Lazy evaluation: chỉ tính báo cáo khi người dùng chọn chức năng báo cáo.
- Async/await: đọc/ghi file chạy qua `asyncio.to_thread` để tránh nghẽn khi thao tác file.
- Không dùng thư viện `json`: file dữ liệu được ghi dạng text và tự tách bằng `split('|')`.

## Test nhanh

```bash
python3 -m pytest tests
```

Nếu máy chưa có `pytest` thì cài:

```bash
pip3 install pytest
```
