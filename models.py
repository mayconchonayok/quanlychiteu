class Transaction:
    def __init__(self, trans_id, date, trans_type, category, amount, note=''):
        self.trans_id = trans_id
        self.date = date
        self.trans_type = trans_type
        self.category = category
        self.amount = amount
        self.note = note

    def __str__(self):
        loai = 'Thu' if self.trans_type == 'income' else 'Chi'
        return f'{self.trans_id:>3} | {self.date:<10} | {loai:<3} | {self.category:<15} | {self.amount:>12,.0f} | {self.note}'


class Category:
    def __init__(self, name, note=''):
        self.name = name
        self.note = note

    def __str__(self):
        return f'{self.name:<20} | {self.note}'


class Budget:
    def __init__(self, category, month, limit):
        self.category = category
        self.month = month
        self.limit = limit

    def __str__(self):
        return f'{self.month} | {self.category:<15} | Hạn mức: {self.limit:,.0f}'
