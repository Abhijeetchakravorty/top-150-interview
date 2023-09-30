class Solution:
    def maxProfit(self, prices):
        # Time Complexity : O(n)
        # Space Complexity: O(1)
        curMin, profit = -1, 0
        for price in prices:
            if curMin == -1:
                curMin = price
            else:
                curProf = price - curMin
                if curProf > profit:
                    profit = curProf
                if price < curMin:
                    curMin = price
        return profit


a = Solution()
b = a.maxProfit([7,1,5,3,6,4])
print("B: ", b)