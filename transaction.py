from models import Transaction
from validators import read_transaction_type, read_date, read_non_empty, read_positive_money, read_int


def next_transaction_id(transactions):
    max_id = 0
    for t in transactions:
        if t.trans_id > max_id:
            max_id = t.trans_id
    return max_id + 1


async def them_giao_dich(transactions, save_func, cache=None):
    print('\n--- THÊM GIAO DỊCH ---')
    trans_type = read_transaction_type()
    date = read_date('Ngày (YYYY-MM-DD): ')
    category = read_non_empty('Danh mục: ')
    amount = read_positive_money('Số tiền: ')
    note = input('Ghi chú: ').strip()

    new_t = Transaction(next_transaction_id(transactions), date, trans_type, category, amount, note)
    transactions.append(new_t)
    if cache is not None:
        cache.clear()
    await save_func(transactions)
    print('Đã thêm giao dịch.')


def sua_giao_dich(transactions, cache=None):
    print('\n--- SỬA GIAO DỊCH ---')
    trans_id = read_int('Nhập mã giao dịch cần sửa: ')
    t = transactions.find_by_id(trans_id)
    if t is None:
        print('Không tìm thấy giao dịch.')
        return False

    print('Bỏ trống nếu không muốn sửa thông tin đó.')
    new_date = input(f'Ngày mới ({t.date}): ').strip()
    if new_date != '':
        t.date = new_date

    new_category = input(f'Danh mục mới ({t.category}): ').strip()
    if new_category != '':
        t.category = new_category

    new_amount = input(f'Số tiền mới ({t.amount:,.0f}): ').replace(',', '').strip()
    if new_amount != '':
        try:
            value = float(new_amount)
            if value > 0:
                t.amount = value
            else:
                print('Số tiền không hợp lệ, giữ nguyên giá trị cũ.')
        except ValueError:
            print('Số tiền không hợp lệ, giữ nguyên giá trị cũ.')

    new_note = input(f'Ghi chú mới ({t.note}): ').strip()
    if new_note != '':
        t.note = new_note

    if cache is not None:
        cache.clear()
    print('Đã sửa giao dịch.')
    return True


async def xoa_giao_dich(transactions, save_func, cache=None):
    print('\n--- XÓA GIAO DỊCH ---')
    if len(transactions) == 0:
        print('Chưa có giao dịch để xóa.')
        return
    trans_id = read_int('Nhập mã giao dịch cần xóa: ')
    ok = transactions.remove_by_id(trans_id)
    if ok:
        if cache is not None:
            cache.clear()
        await save_func(transactions)
        print('Đã xóa giao dịch.')
    else:
        print('Không tìm thấy giao dịch có mã này.')


def tim_giao_dich_theo_ma(transactions):
    trans_id = read_int('Nhập mã giao dịch: ')
    t = transactions.find_by_id(trans_id)
    if t is None:
        print('Không tìm thấy giao dịch.')
    else:
        print('\nGiao dịch tìm thấy:')
        print(t)


def tim_giao_dich_theo_ngay(transactions):
    date = read_date('Nhập ngày cần tìm (YYYY-MM-DD): ')
    found = False
    for t in transactions:
        if t.date == date:
            print(t)
            found = True
    if not found:
        print('Không có giao dịch trong ngày này.')


def tim_giao_dich_theo_loai(transactions):
    trans_type = read_transaction_type()
    found = False
    for t in transactions:
        if t.trans_type == trans_type:
            print(t)
            found = True
    if not found:
        print('Không có giao dịch thuộc loại này.')
