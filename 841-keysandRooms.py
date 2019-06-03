class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res = set([0])
        queue = rooms[0]
        while len(queue) != 0: # bfs基于队列的广度优先遍历
            keyID = queue.pop(0)
            res.add(keyID)
            queue.extend([item for item in rooms[keyID] if item not in res]) # 只添加没有访问过的房间
        for i in range(len(rooms)):
            if i not in res:
                return False
        return True