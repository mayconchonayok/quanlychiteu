import csv
import os

REPORT_FOLDER = 'reports'


def tao_thu_muc_bao_cao():
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)


def lay_du_lieu_chi_tieu_theo_danh_muc(transactions):
    data = {}
    for t in transactions:
        if t.trans_type == 'expense':
            if t.category not in data:
                data[t.category] = 0
            data[t.category] += t.amount
    return data


def xuat_bao_cao_txt(transactions):
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    filename = os.path.join(REPORT_FOLDER, 'bao_cao_chi_tieu.txt')
    total = 0
    for k in data:
        total += data[k]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('===== BÁO CÁO CHI TIÊU THEO DANH MỤC =====\n\n')
        f.write(f'Tổng chi: {total:,.0f} VND\n\n')
        for k in data:
            f.write(f'{k}: {data[k]:,.0f} VND\n')
    print('Đã xuất báo cáo TXT:', filename)


def xuat_bao_cao_csv(transactions):
    tao_thu_muc_bao_cao()
    data = lay_du_lieu_chi_tieu_theo_danh_muc(transactions)
    filename = os.path.join(REPORT_FOLDER, 'bao_cao_chi_tieu.csv')
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Danh mục', 'Số tiền'])
        for k in data:
            writer.writerow([k, data[k]])
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
    for k in data:
        labels.append(k)
        values.append(data[k])
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
    for k in data:
        labels.append(k)
        values.append(data[k])
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Biểu đồ tròn cơ cấu chi tiêu')
    plt.tight_layout()
    filename = os.path.join(REPORT_FOLDER, 'bieu_do_tron_chi_tieu.png')
    plt.savefig(filename)
    plt.close()
    print('Đã xuất biểu đồ tròn:', filename)
