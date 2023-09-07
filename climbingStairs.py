class Solution:
    def climbingStairs(self, n):
        a=1 
        b=1
        for i in range(n):
            s = a+b
            a = b
            b = s
        return b