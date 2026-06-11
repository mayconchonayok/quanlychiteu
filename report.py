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
    by_category = {}
    for t in transactions:
        if not t.date.startswith(month):
            continue
        if t.trans_type == 'income':
            income += t.amount
        elif t.trans_type == 'expense':
            expense += t.amount
            if t.category not in by_category:
                by_category[t.category] = 0
            by_category[t.category] += t.amount

    result = {
        'income': income,
        'expense': expense,
        'balance': income - expense,
        'by_category': by_category
    }
    if cache is not None:
        cache.month_key = month
        cache.month_value = result
    return result


def calculate_spending_by_category(transactions, cache=None):
    if cache is not None and cache.category_value is not None:
        return cache.category_value

    data = {}
    for t in transactions:
        if t.trans_type == 'expense':
            if t.category not in data:
                data[t.category] = 0
            data[t.category] += t.amount

    # Bubble sort trên cặp key-value để đúng tinh thần tự cài thuật toán đơn giản.
    items = []
    for k in data:
        items.append([k, data[k]])
    n = len(items)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if items[j][1] < items[j + 1][1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
            j += 1
        i += 1

    result = {}
    for item in items:
        result[item[0]] = item[1]

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
    print(f'\n--- BÁO CÁO THÁNG {month} ---')
    print(f'Tổng thu : {data["income"]:,.0f}')
    print(f'Tổng chi : {data["expense"]:,.0f}')
    print(f'Số dư    : {data["balance"]:,.0f}')
    print('\nChi theo danh mục:')
    if len(data['by_category']) == 0:
        print('Không có khoản chi trong tháng này.')
    else:
        for category in data['by_category']:
            print(f'- {category}: {data["by_category"][category]:,.0f}')


def hien_thi_chi_theo_danh_muc(transactions, cache=None):
    data = calculate_spending_by_category(transactions, cache)
    print('\n--- CHI TIÊU THEO DANH MỤC ---')
    if len(data) == 0:
        print('Chưa có khoản chi nào.')
        return

    max_value = 0
    for k in data:
        if data[k] > max_value:
            max_value = data[k]

    for category in data:
        amount = data[category]
        bar_len = int(amount / max_value * 30) if max_value > 0 else 0
        print(f'{category:<15} {amount:>12,.0f}  {"*" * bar_len}')
