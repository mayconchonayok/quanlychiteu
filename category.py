from models import Category
from data_structures import DynamicArray
from validators import read_non_empty, read_int


def tao_danh_muc_mac_dinh():
    arr = DynamicArray()
    arr.append(Category('Ăn uống'))
    arr.append(Category('Học phí'))
    arr.append(Category('Đi lại'))
    arr.append(Category('Lương'))
    arr.append(Category('Giải trí'))
    return arr


def tim_danh_muc(categories, name):
    i = 0
    while i < len(categories):
        c = categories.get(i)
        if c is not None and c.name.lower() == name.lower():
            return i
        i += 1
    return -1


def them_danh_muc(categories):
    name = read_non_empty('Tên danh mục: ')
    if tim_danh_muc(categories, name) != -1:
        print('Danh mục này đã tồn tại.')
        return
    note = input('Ghi chú: ').strip()
    categories.append(Category(name, note))
    print('Đã thêm danh mục.')


def sua_danh_muc(categories):
    old_name = read_non_empty('Nhập tên danh mục cần sửa: ')
    pos = tim_danh_muc(categories, old_name)
    if pos == -1:
        print('Không tìm thấy danh mục.')
        return
    c = categories.get(pos)
    new_name = input(f'Tên mới ({c.name}): ').strip()
    if new_name != '':
        c.name = new_name
    new_note = input(f'Ghi chú mới ({c.note}): ').strip()
    if new_note != '':
        c.note = new_note
    print('Đã sửa danh mục.')


def xoa_danh_muc(categories):
    name = read_non_empty('Nhập tên danh mục cần xóa: ')
    pos = tim_danh_muc(categories, name)
    if pos == -1:
        print('Không tìm thấy danh mục.')
        return
    categories.remove_at(pos)
    print('Đã xóa danh mục.')


def bubble_sort_categories(categories):
    n = len(categories)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            c1 = categories.get(j)
            c2 = categories.get(j + 1)
            if c1.name.lower() > c2.name.lower():
                categories.set(j, c2)
                categories.set(j + 1, c1)
            j += 1
        i += 1


def hien_thi_danh_muc(categories):
    if len(categories) == 0:
        print('Chưa có danh mục nào.')
        return
    bubble_sort_categories(categories)
    print('\n--- DANH SÁCH DANH MỤC ---')
    i = 0
    while i < len(categories):
        print(f'{i + 1}. {categories.get(i)}')
        i += 1


def tao_bang_tong_hop():
    return DynamicArray()


def cong_vao_tong_hop(bang, ten_danh_muc, so_tien):
    i = 0
    while i < len(bang):
        cap = bang.get(i)
        if cap[0].lower() == ten_danh_muc.lower():
            cap[1] += so_tien
            return
        i += 1
    bang.append([ten_danh_muc, so_tien])


def sap_xep_tong_hop_giam_dan(bang):
    n = len(bang)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            a = bang.get(j)
            b = bang.get(j + 1)
            if a[1] < b[1]:
                bang.set(j, b)
                bang.set(j + 1, a)
            j += 1
        i += 1


def tong_hop_chi_theo_danh_muc(transactions):
    bang = tao_bang_tong_hop()
    for t in transactions:
        if t.trans_type == 'expense':
            cong_vao_tong_hop(bang, t.category, t.amount)
    sap_xep_tong_hop_giam_dan(bang)
    return bang