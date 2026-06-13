from data_structures import DynamicArray
from category import tong_hop_chi_theo_danh_muc

class ReportCache:
    def __init__(self):
        self.month_key = None
        self.month_value = None
        self.category_value = None

    def clear(self):
        self.month_key = None
        self.month_value = None
        self.category_value = None


def calculate_summary(transactions):
    income = 0
    expense = 0
    for t in transactions:
        if t.trans_type == 'income':
            income += t.amount
        elif t.trans_type == 'expense':
            expense += t.amount
    return income, expense, income - expense


def calculate_monthly_report(transactions, month, cache=None):
    if cache is not None and cache.month_key == month and cache.month_value is not None:
        return cache.month_value

    income = 0
    expense = 0
    by_category = DynamicArray()
    for t in transactions:
        if not t.date.startswith(month):
            continue
        if t.trans_type == 'income':
            income += t.amount
        elif t.trans_type == 'expense':
            expense += t.amount
            found = False
            i = 0
            while i < len(by_category):
                cap = by_category.get(i)
                if cap[0].lower() == t.category.lower():
                    cap[1] += t.amount
                    found = True
                    break
                i += 1
            if not found:
                by_category.append([t.category, t.amount])

    result = [income, expense, income - expense, by_category]

    if cache is not None:
        cache.month_key = month
        cache.month_value = result
    return result


def calculate_spending_by_category(transactions, cache=None):
    if cache is not None and cache.category_value is not None:
        return cache.category_value
    result = tong_hop_chi_theo_danh_muc(transactions)
    if cache is not None:
        cache.category_value = result
    return result

def hien_thi_tong_quan(transactions):
    income, expense, balance = calculate_summary(transactions)
    print('\n--- BÁO CÁO TỔNG QUAN ---')
    print(f'Tổng thu : {income:,.0f}')
    print(f'Tổng chi : {expense:,.0f}')
    print(f'Số dư    : {balance:,.0f}')


def hien_thi_bao_cao_thang(transactions, month, cache=None):
    data = calculate_monthly_report(transactions, month, cache)
    print(f'\n--- BAO CAO THANG {month} ---')
    print(f'Tong thu : {data[0]:,.0f}')
    print(f'Tong chi : {data[1]:,.0f}')
    print(f'So du    : {data[2]:,.0f}')
    print('\nChi theo danh muc:')
    by_category = data[3]
    if len(by_category) == 0:
        print('Khong co khoan chi trong thang nay.')
    else:
        i = 0
        while i < len(by_category):
            cap = by_category.get(i)
            print(f'- {cap[0]}: {cap[1]:,.0f}')
            i += 1


def hien_thi_chi_theo_danh_muc(transactions, cache=None):
    data = calculate_spending_by_category(transactions, cache)
    print('\n--- CHI TIEU THEO DANH MUC ---')
    if len(data) == 0:
        print('Chua co khoan chi nao.')
        return
    max_value = 0
    i = 0
    while i < len(data):
        cap = data.get(i)
        if cap[1] > max_value:
            max_value = cap[1]
        i += 1
    i = 0
    while i < len(data):
        cap = data.get(i)
        bar_len = int(cap[1] / max_value * 30) if max_value > 0 else 0
        print(f'{cap[0]:<15} {cap[1]:>12,.0f}  {"*" * bar_len}')
        i += 1

