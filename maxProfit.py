class Solution:
    def maxProfit(self, prices):
        lo = float('inf')
        mx = float('-inf')
        ret = 0

        for p in prices:
            if p < lo:
                lo = mx = p
            if p > mx:
                mx = p
                ret = max(ret, mx-lo)

        return ret