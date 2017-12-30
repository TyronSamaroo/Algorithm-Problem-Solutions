#!/usr/bin/env python3
class Node:
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data; self.left = left; self.right = right; self.parent = None
    def __del__(self):
        del self.data; self.left = None; self.right = None
    def __str__(self):
        return str(self.data)
    def get_data(self):
        return self.data
    def get_left(self):
        return self.left
    def get_parent(self):
        return self.parent
    def get_right(self):
        return self.right
    def get_successor(self):
        if self.right is not None:
            curr = self.right
            while curr.left is not None:
                curr = curr.left
            return curr
        else:
            curr = self; par = self.parent
            while par is not None and curr != par.left:
                curr = par; par = curr.parent
            return par
    def set_data(self, data):
        self.data = data
    def set_left(self, left):
        self.left = left
        if self.left:
            self.left.set_parent(self)
    def set_parent(self, parent):
        self.parent = parent
    def set_right(self, right):
        self.right = right
        if self.right:
            self.right.set_parent(self)
    def preorder(self):
        yield self
        if self.left is not None:
            for e in self.left.preorder():
                yield e
        if self.right is not None:
            for e in self.right.preorder():
                yield e
    def inorder(self):
        if self.left is not None:
            for e in self.left.inorder():
                yield e
        yield self
        if self.right is not None:
            for e in self.right.inorder():
                yield e
    def postorder(self):
        if self.left is not None:
            for e in self.left.postorder():
                yield e
        if self.right is not None:
            for e in self.right.postorder():
                yield e
        yield self

class BinarySearchTree:
    def __init__(self):
        self.size = 0; self.root = None; self.leftmost = None; self.iter_curr = None
    def __del__(self):
        self.clear()
    def __len__(self):
        return self.size
    def __iter__(self):
        return self
    def __next__(self):
        if self.iter_curr is None:
            self.iter_curr = self.leftmost; raise StopIteration
        else:
            tmp = self.iter_curr.get_data(); self.iter_curr = self.iter_curr.get_successor(); return tmp
    def __contains__(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.get_data():
                curr = curr.get_left()
            elif curr.get_data() < data:
                curr = curr.get_right()
            else:
                return True
        return False
    def clear(self):
        if self.root:
            for node in self.root.postorder():
                node.set_data(None); node.set_parent(None); node.set_left(None); node.set_right(None)
        self.size = 0; self.root = None; self.leftmost = None; self.iter_curr = None
    def empty(self):
        return self.size == 0
    def insert(self, data):
        if self.empty():
            self.root = Node(data); self.leftmost = self.root; self.iter_curr = self.leftmost; self.size += 1; return True
        else:
            if type(data) != type(self.root.get_data()):
                raise TypeError("All elements must be same type")
            curr = self.root
            while True:
                if data < curr.get_data():
                    if curr.get_left() is None:
                        curr.set_left(Node(data, parent = curr)); self.size += 1
                        if self.leftmost == curr:
                            self.leftmost = curr.get_left(); self.iter_curr = self.leftmost
                        return True
                    else:
                        curr = curr.get_left()
                elif curr.get_data() < data:
                    if curr.get_right() is None:
                        curr.set_right(Node(data, parent = curr)); self.size += 1; return True
                    else:
                        curr = curr.get_right()
                else:
                    return False
    def remove(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.get_data():
                curr = curr.get_left()
            elif curr.get_data() < data:
                curr = curr.get_right()
            else:
                if curr.get_left() is None and curr.get_right() is None:
                    if curr.get_parent() is None:
                        self.root = None; self.leftmost = None; self.iter_curr = self.leftmost
                    elif curr == curr.get_parent().get_left():
                        curr.set_left(None)
                        if curr == self.leftmost:
                            self.leftmost = curr.get_parent(); self.iter_curr = self.leftmost
                    else:
                        curr.set_right(None)
                elif curr.get_left() is None:
                    self.leftmost = curr.successor(); self.iter_curr = self.leftmost
                    if curr.get_parent() is None:
                        self.root = curr.get_right()
                    elif curr == curr.get_parent().get_left():
                        curr.get_parent().set_left(curr.get_right())
                    else:
                        curr.get_parent().set_right(curr.get_right())
                elif curr.get_right() is None:
                    if curr.get_parent() is None:
                        self.root = curr.get_left()
                    elif curr == curr.get_parent().get_left():
                        curr.get_parent().set_left(curr.get_left())
                    else:
                        curr.get_parent().set_right(curr.get_left())
                else:
                    suc = curr.get_successor(); curr.set_data(suc.get_data())
                    if suc.get_parent() == curr:
                        curr.set_right(suc.get_right())
                    else:
                        suc.get_parent().set_left(suc.get_right())
                    curr = suc
                del curr; self.size -= 1; return True #DELETE
        return False
    def preorder(self):
        if self.root:
            for e in self.root.preorder():
                yield e.get_data()
    def inorder(self):
        if self.root:
            for e in self.root.inorder():
                yield e.get_data()
    def postorder(self):
        if self.root:
            for e in self.root.postorder():
                yield e.get_data()