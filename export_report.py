import csv
import os
from data_structures import DynamicArray
from category import tong_hop_chi_theo_danh_muc

REPORT_FOLDER = 'reports'


def tao_thu_muc_bao_cao():
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)




def lay_du_lieu_chi_tieu_theo_danh_muc(transactions):
    return tong_hop_chi_theo_danh_muc(transactions)


def xuat_bao_cao_txt(transactions):
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    filename = os.path.join(REPORT_FOLDER, 'bao_cao_chi_tieu.txt')
    total = 0
    i = 0
    while i < len(data):
        total += data.get(i)[1]
        i += 1
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('===== BÁO CÁO CHI TIÊU THEO DANH MỤC =====\n\n')
        f.write(f'Tong chi: {total:,.0f} VND\n\n')
        i = 0
        while i < len(data):
            cap = data.get(i)
            f.write(f'{cap[0]}: {cap[1]:,.0f} VND\n')
            i += 1
    print('Đã xuất báo cáo TXT:', filename)


def xuat_bao_cao_csv(transactions):
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    filename = os.path.join(REPORT_FOLDER, 'bao_cao_chi_tieu.csv')
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Danh mục', 'Số tiền'])
        i = 0
        while i < len(data):
            cap = data.get(i)
            writer.writerow([cap[0], cap[1]])
            i += 1
    print('Đã xuất báo cáo CSV:', filename)


def ve_bieu_do_cot(transactions):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('Máy chưa cài matplotlib. Chạy: pip3 install matplotlib')
        return
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    if len(data) == 0:
        print('Chưa có dữ liệu chi tiêu để vẽ biểu đồ.')
        return
    labels = []
    values = []
    i = 0
    while i < len(data):
        cap = data.get(i)
        labels.append(cap[0])
        values.append(cap[1])
        i += 1
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title('Biểu đồ cột chi tiêu theo danh mục')
    plt.xlabel('Danh mục')
    plt.ylabel('Số tiền')
    plt.xticks(rotation=30)
    plt.tight_layout()
    filename = os.path.join(REPORT_FOLDER, 'bieu_do_cot_chi_tieu.png')
    plt.savefig(filename)
    plt.close()
    print('Đã xuất biểu đồ cột:', filename)


def ve_bieu_do_tron(transactions):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print('Máy chưa cài matplotlib. Chạy: pip3 install matplotlib')
        return
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    if len(data) == 0:
        print('Chưa có dữ liệu chi tiêu để vẽ biểu đồ.')
        return
    labels = []
    values = []
    i = 0
    while i < len(data):
        cap = data.get(i)
        labels.append(cap[0])
        values.append(cap[1])
        i += 1
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Biểu đồ tròn cơ cấu chi tiêu')
    plt.tight_layout()
    filename = os.path.join(REPORT_FOLDER, 'bieu_do_tron_chi_tieu.png')
    plt.savefig(filename)
    plt.close()
    print('Đã xuất biểu đồ tròn:', filename)
