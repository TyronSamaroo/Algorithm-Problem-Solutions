#!/usr/bin/env python3
class UpTree:
    def __init__(self):
        self.parent = dict(); self.size = dict()
    def __len__(self):
        return len(self.parent)
    def __getitem__(self, key): # "find" function
        if key not in self.parent:
            raise KeyError(str(key))
        q = [key]
        while self.parent[q[-1]] is not None:
            q.append(self.parent[q[-1]])
        sentinel = q.pop(); n_to_sub = 0
        for n in q:
            self.parent[n] = sentinel # path compression
            self.size[n] -= n_to_sub; n_to_sub += self.size[n]
        return sentinel
    def __iter__(self):
        return iter(self.parent.keys())
    def __next__(self):
        return next(iter(self.parent.keys()))
    def add(self, key):
        if key in self.parent:
            raise ValueError("Duplicate key: %s" % str(key))
        self.parent[key] = None; self.size[key] = 1
    def sentinels(self):
        return {n for n in self.parent if self.parent[n] is None}
    def union(self, u, v):
        if u not in self.parent:
            raise KeyError(str(u))
        if v not in self.parent:
            raise KeyError(str(v))
        sentinel_u = self[u]; sentinel_v = self[v]
        if sentinel_u == sentinel_v:
            return
        elif self.size[sentinel_u] > self.size[sentinel_v]: # union by size
            self.parent[sentinel_v] = sentinel_u
        else:
            self.parent[sentinel_u] = sentinel_v