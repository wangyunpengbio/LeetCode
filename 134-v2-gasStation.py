class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = run = start = 0
        for i in range(len(gas)):
            run = run + gas[i] - cost[i]
            rest = rest + gas[i] - cost[i]
            if run < 0:
                start = i + 1
                run = 0
        if rest < 0:
            return -1
        else:
            return start
'''
【笔记】一次遍历法，车能开完全程需要满足两个条件：

车从i站能开到i+1。

所有站里的油总量要>=车子的总耗油量。

那么，假设从编号为0站开始，一直到k站都正常，在开往k+1站时车子没油了。这时，应该将起点设置为k+1站。

补充两个问题
问题1: 为什么应该将起始站点设为k+1？

因为k->k+1站耗油太大，0->k站每站的剩余油量都是不为负的，每减少一站，就少了一些剩余油量。所以如果从k前面的站点作为起始站，剩余油量不可能冲过k+1站。

问题2: 为什么如果k+1->end全部可以正常通行，且rest>=0就可以说明车子从k+1站点出发可以开完全程？

因为，起始点将当前路径分为A、B两部分。其中，必然有(1)A部分剩余油量<0。(2)B部分剩余油量>0。

所以，无论多少个站，都可以抽象为两个站点（A、B）。(1)从B站加满油出发，(2)开往A站，车加油，(3)再开回B站的过程。

重点：B剩余的油>=A缺少的总油。必然可以推出，B剩余的油>=A站点的每个子站点缺少的油。
'''