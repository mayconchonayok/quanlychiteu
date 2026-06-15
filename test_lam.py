import os
import sys
import io
import csv
import tempfile

from data_structures import LinkedList, DynamicArray
from models import Transaction, Budget
from budget import kiem_tra_ngan_sach
from report import calculate_summary, calculate_monthly_report, hien_thi_bao_cao_thang, hien_thi_chi_theo_danh_muc
from export_report import xuat_bao_cao_txt, xuat_bao_cao_csv


def tao_du_lieu_mau():
    trans = LinkedList()
    trans.append(Transaction(1, '2026-06-01', 'income', 'Luong', 5000000, 'Luong thang 6'))
    trans.append(Transaction(2, '2026-06-02', 'expense', 'An uong', 200000, 'Com trua'))
    trans.append(Transaction(3, '2026-06-05', 'expense', 'An uong', 300000, 'Di an'))
    trans.append(Transaction(4, '2026-06-10', 'expense', 'Di lai', 100000, 'Xe om'))
    trans.append(Transaction(5, '2026-06-15', 'income', 'Luong', 1000000, 'Thuong'))
    return trans


def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout
    return captured.getvalue()


def test_bao_cao_tong_quan():
    trans = tao_du_lieu_mau()
    income, expense, balance = calculate_summary(trans)
    assert income == 6000000
    assert expense == 600000
    assert balance == 5400000
    print('PASS: bao cao tong quan')


def test_bao_cao_thang_co_du_lieu():
    trans = tao_du_lieu_mau()
    data = calculate_monthly_report(trans, '2026-06')
    assert data[0] == 6000000
    assert data[1] == 600000
    assert data[2] == 5400000
    by_category = data[3]
    assert len(by_category) == 2
    assert by_category.get(0)[0] == 'An uong'
    assert by_category.get(0)[1] == 500000
    assert by_category.get(1)[0] == 'Di lai'
    assert by_category.get(1)[1] == 100000
    print('PASS: bao cao thang co du lieu')


def test_bao_cao_thang_khong_co_du_lieu():
    trans = tao_du_lieu_mau()
    data = calculate_monthly_report(trans, '2026-07')
    assert data[0] == 0
    assert data[1] == 0
    assert data[2] == 0
    assert len(data[3]) == 0
    output = capture_output(hien_thi_bao_cao_thang, trans, '2026-07')
    assert 'Khong co khoan chi trong thang nay.' in output
    print('PASS: bao cao thang khong co du lieu')


def test_ngan_sach_vuot_muc():
    trans = tao_du_lieu_mau()
    budgets = DynamicArray()
    budgets.append(Budget('An uong', '2026-06', 200000))
    result = kiem_tra_ngan_sach(trans, budgets, '2026-06')
    assert len(result) == 1
    budget, used, remain = result[0]
    assert budget.category == 'An uong'
    assert used == 500000
    assert remain == -300000
    print('PASS: ngan sach vuot muc')


def test_ngan_sach_con_trong_han_muc():
    trans = tao_du_lieu_mau()
    budgets = DynamicArray()
    budgets.append(Budget('Di lai', '2026-06', 300000))
    result = kiem_tra_ngan_sach(trans, budgets, '2026-06')
    assert len(result) == 1
    budget, used, remain = result[0]
    assert budget.category == 'Di lai'
    assert used == 100000
    assert remain == 200000
    print('PASS: ngan sach con trong han muc')


def test_ngan_sach_thang_chua_dat():
    trans = tao_du_lieu_mau()
    budgets = DynamicArray()
    budgets.append(Budget('An uong', '2026-06', 200000))
    result = kiem_tra_ngan_sach(trans, budgets, '2026-07')
    assert len(result) == 0
    print('PASS: ngan sach thang chua dat')


def test_ascii_chart_chi_theo_danh_muc():
    trans = tao_du_lieu_mau()
    output = capture_output(hien_thi_chi_theo_danh_muc, trans)
    assert 'An uong' in output
    assert 'Di lai' in output
    assert '*' in output
    print('PASS: ascii chart chi theo danh muc')


def test_xuat_bao_cao_txt():
    trans = tao_du_lieu_mau()
    old_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            xuat_bao_cao_txt(trans)
            file_path = os.path.join('reports', 'bao_cao_chi_tieu.txt')
            assert os.path.exists(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert 'Tong chi: 600,000 VND' in content
            assert 'An uong: 500,000 VND' in content
            assert 'Di lai: 100,000 VND' in content
        finally:
            os.chdir(old_cwd)
    print('PASS: xuat bao cao TXT')


def test_xuat_bao_cao_csv():
    trans = tao_du_lieu_mau()
    old_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            xuat_bao_cao_csv(trans)
            file_path = os.path.join('reports', 'bao_cao_chi_tieu.csv')
            assert os.path.exists(file_path)
            with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
                rows = list(csv.reader(f))
            assert rows[0] == ['Danh mục', 'Số tiền']
            assert ['An uong', '500000'] in rows
            assert ['Di lai', '100000'] in rows
        finally:
            os.chdir(old_cwd)
    print('PASS: xuat bao cao CSV')


def run_all_tests():
    test_bao_cao_tong_quan()
    test_bao_cao_thang_co_du_lieu()
    test_bao_cao_thang_khong_co_du_lieu()
    test_ngan_sach_vuot_muc()
    test_ngan_sach_con_trong_han_muc()
    test_ngan_sach_thang_chua_dat()
    test_ascii_chart_chi_theo_danh_muc()
    test_xuat_bao_cao_txt()
    test_xuat_bao_cao_csv()
    print('\nTat ca test cua Lam deu PASS.')


if __name__ == '__main__':
    run_all_tests()
