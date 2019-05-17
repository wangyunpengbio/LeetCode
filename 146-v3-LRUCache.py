class LRUCache(object):
    # python 2 写法
    def __init__(self, capacity):

        self.csize = capacity
        self.cache = {}
        self.priority = [] # 要被移除的key = priority[0]


    def get(self, key): # 同時要標記used?

        if self.cache.has_key(key):
            self.priority.append(key)
            self.priority.remove(key)

        return self.cache.get(key,-1)


    def put(self, key, value):

        if self.cache.has_key(key): # 相同键，重新赋值的时候先删
            self.priority.remove(key)
            self.priority.append(key)

        else:# 写入，满了取代
            if len(self.cache)== self.csize: # 满了
                #print(replace)
                self.cache.pop(self.priority[0])
                self.priority.pop(0)

            self.priority.append(key)

        self.cache[key] = value 

        return 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)