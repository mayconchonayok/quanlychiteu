from datetime import datetime


def is_valid_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_month(value):
    try:
        datetime.strptime(value, '%Y-%m')
        return True
    except ValueError:
        return False


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != '':
            return value
        print('Không được để trống. Vui lòng nhập lại.')


def read_date(prompt):
    while True:
        value = input(prompt).strip()
        if is_valid_date(value):
            return value
        print('Ngày không hợp lệ. Định dạng đúng là YYYY-MM-DD.')


def read_month(prompt):
    while True:
        value = input(prompt).strip()
        if is_valid_month(value):
            return value
        print('Tháng không hợp lệ. Định dạng đúng là YYYY-MM.')


def read_positive_money(prompt):
    while True:
        raw = input(prompt).replace(',', '').strip()
        try:
            amount = float(raw)
            if amount > 0:
                return amount
            print('Số tiền phải lớn hơn 0.')
        except ValueError:
            print('Số tiền không hợp lệ. Vui lòng nhập bằng số.')


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print('Giá trị phải là số nguyên.')


def read_transaction_type():
    while True:
        print('1. Thu nhập')
        print('2. Chi tiêu')
        choice = input('Chọn loại giao dịch: ').strip()
        if choice == '1':
            return 'income'
        if choice == '2':
            return 'expense'
        print('Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.')
