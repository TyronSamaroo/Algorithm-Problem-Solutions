#!/usr/bin/env python3
class Node:
    def __init__(self, word = None):
        self.children = {}; self.word = word

class MultiwayTrie:
    def __init__(self):
        self.root = Node(); self.size = 0; self.iter_s = [self.root]
    def __len__(self):
        return self.size
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.iter_s) == 0:
            self.iter_s.append(self.root); raise StopIteration
        else:
            curr = Node()
            while curr.word is None and len(self.iter_s) != 0:
                curr = self.iter_s.pop()
                for c in sorted(curr.children.keys()):
                    self.iter_s.append(curr.children[c])
            if curr.word is not None:
                return curr.word
            else:
                self.iter_s.append(self.root); raise StopIteration
    def __contains__(self, key):
        if not isinstance(key, str) and not isinstance(key, list):
            raise TypeError("Keys must be str or list")
        curr = self.root
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word is not None
    def clear(self):
        del self.root; self.root = Node(); self.size = 0; self.iter_s = [self.root]
    def empty(self):
        return self.size == 0
    def add(self, key):
        if not isinstance(key, str) and not isinstance(key, list):
            raise TypeError("Keys must be str or list")
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        if curr.word is None:
            curr.word = key; self.size += 1; return True
        else:
            return False
    def remove(self, key):
        if not isinstance(key, str) and not isinstance(key, list):
            raise TypeError("Keys must be str or list")
        curr = self.root
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if curr.word is None:
            return False
        else:
            curr.word = None; self.size -= 1; return True