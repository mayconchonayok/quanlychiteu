from data_structures import DynamicArray, LinkedList
from models import Transaction, Category
from category import tim_danh_muc, bubble_sort_categories, tong_hop_chi_theo_danh_muc

def test_dynamic_array_resize():
    arr = DynamicArray(capacity=2)
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert len(arr) == 3
    assert arr.get(2) == 3
    print("PASS: dynamic array resize")

def test_linked_list_remove_by_id():
    lst = LinkedList()
    lst.append(Transaction(1, '2026-06-01', 'expense', 'An uong', 50000, ''))
    lst.append(Transaction(2, '2026-06-02', 'income', 'Luong', 500000, ''))
    assert lst.remove_by_id(1) == True
    assert lst.remove_by_id(99) == False
    assert len(lst) == 1
    print("PASS: linked list remove by id")

def test_tim_danh_muc():
    cats = DynamicArray()
    cats.append(Category('An uong'))
    cats.append(Category('Di lai'))
    assert tim_danh_muc(cats, 'di lai') == 1
    assert tim_danh_muc(cats, 'Hoc phi') == -1
    print("PASS: tim danh muc")

def test_bubble_sort_categories():
    cats = DynamicArray()
    cats.append(Category('Di lai'))
    cats.append(Category('An uong'))
    bubble_sort_categories(cats)
    assert cats.get(0).name == 'An uong'
    print("PASS: bubble sort categories")

def test_tong_hop_chi_theo_danh_muc():
    trans = LinkedList()
    trans.append(Transaction(1, '2026-06-01', 'expense', 'An uong', 100000, ''))
    trans.append(Transaction(2, '2026-06-02', 'expense', 'An uong', 50000, ''))
    trans.append(Transaction(3, '2026-06-03', 'expense', 'Di lai', 200000, ''))
    bang = tong_hop_chi_theo_danh_muc(trans)
    assert bang.get(0)[0] == 'Di lai'
    assert bang.get(0)[1] == 200000
    assert bang.get(1)[1] == 150000
    print("PASS: tong hop chi theo danh muc")

test_dynamic_array_resize()
test_linked_list_remove_by_id()
test_tim_danh_muc()
test_bubble_sort_categories()
test_tong_hop_chi_theo_danh_muc()
print("\nTat ca test deu PASS.")