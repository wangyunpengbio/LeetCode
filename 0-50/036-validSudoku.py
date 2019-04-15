class Solution:
    # 如何确保行 / 列 / 子数独中没有重复项？
    # 可以利用 value -> count 哈希映射来跟踪所有已经遇到的值。
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        # i row的id
        # j column的id
        # (i//3)*3+j//3 # box的id
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_id = (i//3)*3+j//3 # box的id
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_id][num] = boxes[box_id].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_id][num] > 1:
                        return False   
        return True