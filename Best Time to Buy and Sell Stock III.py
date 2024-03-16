class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ini=0
        bou1=float('-inf')
        sol1=0
        bou2=float('-inf')
        sol2=0
        for x in prices:
            bou1=max(ini-x,bou1)
            sol1=max(bou1+x,sol1)
            bou2=max(sol1-x,bou2)
            sol2=max(bou2+x,sol2)
        return sol2
