class Solution:
    def isHappy(self, n):
        visited = set()
        while n > 0 and n not in visited and n != 1:
            visited.add(n)
            while n != 0:
                remainder = n % 10
                cur_sum += (remainder * remainder)
                n = n // 10
            n = cur_sum
            cur_sum = 0
        
        if(n == 1):
            return True
        else:
            return False