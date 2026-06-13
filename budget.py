from transaction import chon_danh_muc
from models import Budget
from validators import read_month, read_non_empty, read_positive_money


def them_ngan_sach(budgets, categories):
    print('\n--- ĐẶT NGÂN SÁCH ---')
    month = read_month('Tháng (YYYY-MM): ')
    category = chon_danh_muc(categories)
    limit = read_positive_money('Hạn mức: ')

    for b in budgets:
        if b.month == month and b.category.lower() == category.lower():
            b.limit = limit
            print('Đã cập nhật ngân sách.')
            return
    budgets.append(Budget(category, month, limit))
    print('Đã thêm ngân sách.')


def kiem_tra_ngan_sach(transactions, budgets, month):
    result = []
    for b in budgets:
        if b.month == month:
            used = 0
            for t in transactions:
                if t.trans_type == 'expense' and t.category.lower() == b.category.lower() and t.date.startswith(month):
                    used += t.amount
            result.append((b, used, b.limit - used))
    return result


def hien_thi_ngan_sach(transactions, budgets):
    month = read_month('Nhập tháng cần kiểm tra (YYYY-MM): ')
    result = kiem_tra_ngan_sach(transactions, budgets, month)
    print(f'\n--- KIỂM TRA NGÂN SÁCH THÁNG {month} ---')
    if len(result) == 0:
        print('Chưa đặt ngân sách cho tháng này.')
        return
    for b, used, remain in result:
        if remain >= 0:
            status = 'Còn trong hạn mức'
        else:
            status = 'Đã vượt ngân sách'
        print(f'{b.category:<15} Đã chi: {used:>12,.0f} / Hạn mức: {b.limit:>12,.0f} / {status}')
