class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        i = 0
        while i < self.size:
            new_data[i] = self.data[i]
            i += 1
        self.data = new_data

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            return False
        self.data[index] = value
        return True

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            return False
        i = index
        while i < self.size - 1:
            self.data[i] = self.data[i + 1]
            i += 1
        self.data[self.size - 1] = None
        self.size -= 1
        return True

    def clear(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity

    def __len__(self):
        return self.size

    def __iter__(self):
        i = 0
        while i < self.size:
            yield self.data[i]
            i += 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_by_id(self, trans_id):
        prev = None
        cur = self.head
        while cur is not None:
            if getattr(cur.data, 'trans_id', None) == trans_id:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def find_by_id(self, trans_id):
        cur = self.head
        while cur is not None:
            if getattr(cur.data, 'trans_id', None) == trans_id:
                return cur.data
            cur = cur.next
        return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next
