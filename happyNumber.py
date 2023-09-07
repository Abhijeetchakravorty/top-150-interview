class Solution:
    def isHappy(self, n):
        visited = set()
        curr_sum = 0
        while n > 0 and n not in visited and n!=1:
            visited.add(n)
            while n > 0:
                remainder = n%10
                curr_sum = remainder*remainder
                n=n//10
            n=curr_sum
            curr_sum=0
        
        if n==1:
            return True
        else:
            return False

