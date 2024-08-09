class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=1
        mprofit=0
        while sell<len(prices):
            if prices[sell]>prices[buy]:
                mprofit=max(prices[sell]-prices[buy],mprofit)
            else:
                buy=sell
            sell+=1
        return mprofit