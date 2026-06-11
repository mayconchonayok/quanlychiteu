from data_structures import LinkedList, DynamicArray
from models import Transaction, Budget
from report import calculate_summary, calculate_monthly_report
from budget import kiem_tra_ngan_sach


def test_calculate_summary():
    trans = LinkedList()
    trans.append(Transaction(1, '2026-06-01', 'income', 'Lương', 1000, ''))
    trans.append(Transaction(2, '2026-06-02', 'expense', 'Ăn uống', 300, ''))
    assert calculate_summary(trans) == (1000, 300, 700)


def test_monthly_report_empty_month():
    trans = LinkedList()
    data = calculate_monthly_report(trans, '2026-06')
    assert data['income'] == 0
    assert data['expense'] == 0


def test_budget_over_limit():
    trans = LinkedList()
    trans.append(Transaction(1, '2026-06-01', 'expense', 'Ăn uống', 600, ''))
    budgets = DynamicArray()
    budgets.append(Budget('Ăn uống', '2026-06', 500))
    result = kiem_tra_ngan_sach(trans, budgets, '2026-06')
    assert result[0][2] == -100
