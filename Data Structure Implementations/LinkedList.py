#!/usr/bin/env python3
class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data; self.prev = prev; self.next = next
    def __del__(self):
        del self.data; self.prev = None; self.next = None
    def __str__(self):
        return "(%s)" % str(self.data)
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next
    def set_prev(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.size = 0; self.front = None; self.back = None; self.iter_curr = None
    def __del__(self):
        curr = self.front
        for _ in range(self.size):
            tmp = curr.get_next(); del curr; curr = tmp
    def __len__(self):
        return self.size
    def __str__(self):
        if self.empty():
            return ""
        curr = self.front; out = str(curr)
        for _ in range(self.size-1):
            curr = curr.get_next(); out += "->%s" % str(curr)
        return out
    def __iter__(self):
        return self
    def __next__(self):
        if self.iter_curr is None:
            self.iter_curr = self.front; raise StopIteration
        else:
            tmp = self.iter_curr; self.iter_curr = self.iter_curr.get_next(); return tmp
    def empty(self):
        return self.size == 0
    def get_end(self):
        return self.back
    def get_front(self):
        return self.front
    def insert_back(self, data):
        self.back = Node(data, prev = self.back)
        if self.back.get_prev() is not None:
            self.back.get_prev().set_next(self.back)
        else:
            self.front = self.back; self.iter_curr = self.front
        self.size += 1
    def insert_front(self, data):
        self.front = Node(data, next = self.front); self.iter_curr = self.front
        if self.front.get_next() is not None:
            self.front.get_next().set_prev(self.front)
        else:
            self.back = self.front
        self.size += 1
    def remove_back(self):
        assert self.size != 0, "Removing from empty list"
        tmp = self.back.get_prev(); del self.back; self.back = tmp; self.size -= 1
    def remove_front(self):
        assert self.size != 0, "Removing from empty list"
        tmp = self.front.get_next(); del self.front; self.front = tmp; self.size -= 1
    def __delitem__(self, index):
        assert index >= 0, "Index must be at least 0"
        assert self.size != 0, "Removing from empty list"
        assert index < self.size, "Index is too large"
        if index == 0:
            self.remove_front()
        elif index == self.size-1:
            self.remove_back()
        else:
            curr = self.front
            for _ in range(index):
                curr = curr.get_next()
            curr.get_prev().set_next(curr.get_next())
            curr.get_next().set_prev(curr.get_prev())
            del curr; self.size -= 1
    def __getitem__(self, index):
        assert index >= 0, "Index must be at least 0"
        assert index < self.size, "Index is too large"
        curr = self.front
        for _ in range(index):
            curr = curr.get_next()
        return curr
    def __setitem__(self, index, data):
        assert index >= 0, "Index must be at least 0"
        assert index <= self.size, "Index is too large"
        if index == 0:
            self.insert_front(data)
        elif index == self.size:
            self.insert_back(data)
        else:
            curr = self.front
            for _ in range(index):
                curr = curr.get_next()
            curr = Node(data, prev = curr.get_prev(), next = curr)
            curr.get_prev().set_next(curr)
            curr.get_next().set_prev(curr)
            self.size += 1