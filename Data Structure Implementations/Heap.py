#!/usr/bin/env python3
def left(index):
    return 2*index+1
def right(index):
    return 2*index+2
def parent(index):
    return int((index-1)/2)
def lt(a,b):
    return a < b
def gt(a,b):
    return a > b

class Heap:
    def __init__(self, max_heap = True): # max_heap = True -> MaxHeap; max_heap = False -> MinHeap
        if not isinstance(max_heap, bool):
            raise TypeError("max_heap must be a boolean")
        self.arr = []; self.comp = {True:gt,False:lt}[max_heap]
    def __del__(self):
        self.clear()
    def __len__(self):
        return len(self.arr)
    def clear(self):
        del self.arr; self.arr = []
    def empty(self):
        return len(self.arr) == 0
    def push(self, data):
        if len(self.arr) != 0 and type(data) != type(self.arr[0]):
            raise TypeError("All elements must be same type")
        i = len(self.arr); self.arr.append(data)
        while i > 0 and self.comp(self.arr[i], self.arr[parent(i)]):
            tmp = self.arr[i]; self.arr[i] = self.arr[parent(i)]; self.arr[parent(i)] = tmp; i = parent(i)
    def pop(self):
        if self.empty():
            return None
        elif len(self.arr) == 1:
            return self.arr.pop()
        out = self.arr[0]; self.arr[0] = self.arr.pop(); i = 0
        while (left(i) < len(self.arr) and self.comp(self.arr[left(i)], self.arr[i])) or (right(i) < len(self.arr) and self.comp(self.arr[right(i)], self.arr[i])):
            if right(i) >= len(self.arr) or self.comp(self.arr[left(i)], self.arr[right(i)]):
                c = left(i)
            else:
                c = right(i)
            tmp = self.arr[i]; self.arr[i] = self.arr[c]; self.arr[c] = tmp; i = c
        return out
    def top(self):
        if self.empty():
            return None
        else:
            return self.arr[0]

PriorityQueue = Heap