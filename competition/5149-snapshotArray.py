class SnapshotArray:

    def __init__(self, length: int):
        self.currentArr = [0]*length
        self.snapshotArr = []
        self.callNums = 0

    def set(self, index: int, val: int) -> None:
        self.currentArr[index] = val

    def snap(self) -> int:
        self.callNums += 1
        self.snapshotArr.append(self.currentArr[:])
        return self.callNums - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshotArr[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)