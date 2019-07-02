class MyQueue:
    # 使用列表实现队列 此种实现较慢
    # 最大的开销发生在超过当前分配大小的增长，这种情况下所有元素都需要移动；或者是在起始位置附近插入或者删除元素，这种情况下所有在该位置后面的元素都需要移动。如果你需要在一个队列的两端进行增删的操作，应当使用collections.deque（双向队列）
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()