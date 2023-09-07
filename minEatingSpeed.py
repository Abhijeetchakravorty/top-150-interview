#Koko eating bananas
class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid  # No need for math.ceil, use integer division

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result



a = Solution()
b = a.minEatingSpeed([3,6,7,11], 8)
print(b)