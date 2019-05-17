class LRUCache(object):
    # python 3，借用内置的OrderedDict结构
    def __init__(self, capacity):
        from collections import OrderedDict
        self.od, self.cap = OrderedDict(), capacity

    def get(self, key):
        if key not in self.od: return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od: del self.od[key]
        elif len(self.od) == self.cap: self.od.popitem(False)
        self.od[key] = value