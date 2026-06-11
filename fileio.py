import asyncio
import os
from data_structures import LinkedList, DynamicArray
from models import Transaction, Budget, Category

DATA_DIR = 'data'
TRANSACTION_FILE = os.path.join(DATA_DIR, 'transactions.txt')
BUDGET_FILE = os.path.join(DATA_DIR, 'budgets.txt')
CATEGORY_FILE = os.path.join(DATA_DIR, 'categories.txt')


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def clean_text(value):
    return str(value).replace('|', '/').replace('\n', ' ').strip()


def parse_line(line):
    # Tự parse dữ liệu bằng split/strip, không dùng thư viện json.
    parts = line.strip().split('|')
    i = 0
    while i < len(parts):
        parts[i] = parts[i].strip()
        i += 1
    return parts


def _load_transactions_sync():
    ensure_data_dir()
    result = LinkedList()
    if not os.path.exists(TRANSACTION_FILE):
        return result
    try:
        with open(TRANSACTION_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == '':
                    continue
                parts = parse_line(line)
                if len(parts) < 6:
                    continue
                try:
                    t = Transaction(int(parts[0]), parts[1], parts[2], parts[3], float(parts[4]), parts[5])
                    result.append(t)
                except ValueError:
                    pass
    except OSError:
        pass
    return result


def _save_transactions_sync(transactions):
    ensure_data_dir()
    with open(TRANSACTION_FILE, 'w', encoding='utf-8') as f:
        for t in transactions:
            line = f'{t.trans_id}|{clean_text(t.date)}|{clean_text(t.trans_type)}|{clean_text(t.category)}|{t.amount}|{clean_text(t.note)}\n'
            f.write(line)


def _load_budgets_sync():
    ensure_data_dir()
    result = DynamicArray()
    if not os.path.exists(BUDGET_FILE):
        return result
    try:
        with open(BUDGET_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == '':
                    continue
                parts = parse_line(line)
                if len(parts) < 3:
                    continue
                try:
                    result.append(Budget(parts[0], parts[1], float(parts[2])))
                except ValueError:
                    pass
    except OSError:
        pass
    return result


def _save_budgets_sync(budgets):
    ensure_data_dir()
    with open(BUDGET_FILE, 'w', encoding='utf-8') as f:
        for b in budgets:
            f.write(f'{clean_text(b.category)}|{clean_text(b.month)}|{b.limit}\n')


def _load_categories_sync():
    ensure_data_dir()
    result = DynamicArray()
    if not os.path.exists(CATEGORY_FILE):
        result.append(Category('Ăn uống'))
        result.append(Category('Học phí'))
        result.append(Category('Đi lại'))
        result.append(Category('Lương'))
        result.append(Category('Giải trí'))
        return result
    try:
        with open(CATEGORY_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == '':
                    continue
                parts = parse_line(line)
                name = parts[0] if len(parts) > 0 else ''
                note = parts[1] if len(parts) > 1 else ''
                if name != '':
                    result.append(Category(name, note))
    except OSError:
        pass
    return result


def _save_categories_sync(categories):
    ensure_data_dir()
    with open(CATEGORY_FILE, 'w', encoding='utf-8') as f:
        for c in categories:
            f.write(f'{clean_text(c.name)}|{clean_text(c.note)}\n')


async def load_transactions():
    return await asyncio.to_thread(_load_transactions_sync)


async def save_transactions(transactions):
    await asyncio.to_thread(_save_transactions_sync, transactions)


async def load_budgets():
    return await asyncio.to_thread(_load_budgets_sync)


async def save_budgets(budgets):
    await asyncio.to_thread(_save_budgets_sync, budgets)


async def load_categories():
    return await asyncio.to_thread(_load_categories_sync)


async def save_categories(categories):
    await asyncio.to_thread(_save_categories_sync, categories)
