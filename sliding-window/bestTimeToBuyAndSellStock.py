class Solution:
    def maxProfit(self, prices):
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        return maxP

a = Solution()
b = a.maxProfit([7,1,5,3,6,4])
print("B: ", b)