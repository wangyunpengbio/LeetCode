class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(item) for item in version1.split(".")]
        version2 = [int(item) for item in version2.split(".")]
        minlen = min(len(version1),len(version2))
        # print(version1,version2)
        # 先遍历两者长度重合的部分是否一致
        for i in range(0,minlen):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        # 再遍历剩下的的部分是否有大于0的数字
        if len(version1) > len(version2):
            for i in range(minlen,len(version1)):
                if version1[i] != 0:
                    return 1
        elif len(version1) < len(version2):
            for i in range(minlen,len(version2)):
                if version2[i] != 0:
                    return -1
        return 0