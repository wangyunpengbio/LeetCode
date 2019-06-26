class FreqStack:
    # 超时
    def __init__(self):
        from collections import defaultdict
        self.stack = []
        self.dic = defaultdict(int)
        self.maxFrequency = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.dic[x] = self.dic[x] + 1
        self.calculateMaxFrequency()

    def pop(self) -> int:
        # print(self.stack,self.dic,self.maxFrequency)
        for i in range(len(self.stack)-1,-1,-1):
            # print(self.stack[i])
            if self.dic[self.stack[i]] == self.maxFrequency:
                self.dic[self.stack[i]] = self.dic[self.stack[i]] - 1
                item = self.stack.pop(i)
                break
        self.calculateMaxFrequency()
        return item

    def calculateMaxFrequency(self):
        self.maxFrequency = 0
        for key,value in self.dic.items():
            if value > self.maxFrequency:
                self.maxFrequency = value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()