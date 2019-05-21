class Solution:
    def simplifyPath(self, path: str) -> str:
        # 使用栈结构，顺序读入，遇到".."则弹出
        pathlist = path.split("/")
        stack = []
        for item in pathlist:
            if item == "" or item == ".":
                continue
            elif item == "..":
                try:
                    stack.pop()
                except:
                    pass
            else:
                stack.append(item)
        # 最后用"/"将目录连起来
        res = "/".join(stack)
        res = "/" + res
        return res