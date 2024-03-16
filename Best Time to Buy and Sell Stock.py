class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxprofit=0
        minpurchase= prices[0]
        for i in range(1,len(prices)):
            maxprofit=max(maxprofit,prices[i]-minpurchase)
            minpurchase=min(minpurchase,prices[i])
        return maxprofit
        
