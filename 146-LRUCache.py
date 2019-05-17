class LRUCache:
    # 自己的python 3 写法，超时
    def __init__(self, capacity: int):
        self.queue = []
        self.queuecapacity = capacity

    def get(self, key: int) -> int:
        # print("get",self.queue)
        curLen = len(self.queue)
        i = curLen - 1
        while i >= 0:
            item = self.queue.pop(i)
            res = item.get(key)
            if res != None:
                self.queue.append(item)
                return res
            else:
                self.queue.insert(i,item)
            i = i - 1
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.queue)):
            if key in self.queue[i].keys():
                del self.queue[i]
                break
        if len(self.queue) < self.queuecapacity:
            self.queue.append({key:value})
        else: 
            self.queue.pop(0)
            self.queue.append({key:value})
        # print("put",self.queue)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)