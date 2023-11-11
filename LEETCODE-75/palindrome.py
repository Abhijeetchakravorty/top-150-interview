# Palindome number
# check if a number is the same from forward as well as in reverse
# Input: 121 ==> true, -121==> False
# Time and space complexity: O(n)
# Check without converting it to string
import math
class Solution:
    def palindromeNumber(self, x):
        # if x < 0:
        #     return False
        # if x == 0:
        #     return True
        # res = []
        # count = math.log10(x)
        # length = int(count+1)
        # for i in range(length-1, -1, -1):
        #     if i == 0:
        #         res.append(x%10)
        #     else:
        #         res.append((x//10**i)%10)
        # l = 0
        # r = len(res)-1
        # while l <= r:
        #     if res[l] == res[r]:
        #         l += 1
        #         r -= 1
        #     else:
        #         return False
        # return True
        n, remainder = x, 0
        while n > 0:
            remainder *= 10
            print("Remainder: ", remainder)
            remainder += n % 10
            print("Remainder: ", remainder)
            n //= 10
            print("N: ", n, "\n")
        
        return remainder == x
    



a = Solution().palindromeNumber(121)
print("A: ", a)