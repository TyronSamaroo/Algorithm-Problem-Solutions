#!/usr/bin/env python3
from LinkedList import LinkedList # separate chaining using LinkedList
class HashTable:
    def __init__(self, cap = 100, load = 0.7): # cap = initial capacity, load = max load factor
        if not isinstance(cap, int) or cap <= 0:
            raise TypeError("cap must be a positive integer")
        if not isinstance(load, float) and not isinstance(load, int):
            raise TypeError("load must be a number")
        elif load <= 0 or load > 1:
            raise ValueError("load must be in range (0,1]")
        self.load = load; self.cap = cap; self.size = 0; self.arr = [None]*cap; self.iter_i = 0
    def __del__(self):
        self.clear()
    def __len__(self):
        return self.size
    def __iter__(self):
        return self
    def __next__(self):
        while self.iter_i < len(self.arr):
            if self.arr[self.iter_i] is None:
                self.iter_i += 1
            else:
                try:
                    return next(self.arr[self.iter_i])
                except StopIteration:
                    self.iter_i += 1
        self.iter_i = 0; raise StopIteration
    def clear(self):
        self.size= 0; del self.arr; self.arr = [None]*self.cap
    def empty(self):
        return len(self) == 0
    def resize(self):
        tmp = self.arr; self.arr = [None]*(2*len(self.arr)); self.size = 0
        for l in tmp:
            if l is not None:
                for k in l:
                    self.insert(k)
        del tmp
    def __contains__(self, data):
        i = hash(data) % len(self.arr)
        return self.arr[i] is not None and data in self.arr[i]
    def insert(self, data):
        if len(self) >= self.load*len(self.arr):
            self.resize()
        i = hash(data) % len(self.arr)
        if self.arr[i] is None:
            self.arr[i] = LinkedList()
        if data in self.arr[i]:
            return False
        else:
            self.arr[i].insert_back(data); self.size += 1; return True
    def remove(self, data):
        i = hash(data) % len(self.arr)
        if self.arr[i] is not None and self.arr[i].remove(data):
            self.size -= 1; return True
        return False