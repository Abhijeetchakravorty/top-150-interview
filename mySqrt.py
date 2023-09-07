class Solution:
    def mySqrt(self, x):
        left = 0
        right = x

        while(left <= right):
            middle = (left+right)//2
            sq = middle*middle

            if(sq == x):
                return middle
            if(sq > x):
                right = middle - 1
            else:
                left = middle + 1
        return left - 1
a = Solution()
b = a.mySqrt(16)
print(b)
