class Solution:
    def isPalindrome(self, s):
        # Time Complexity : O(n)
        # Space Complexity: O(n) 
        nospace = ("".join(filter(str.isalnum, s))).lower()
        return nospace == nospace[::-1]
    #     l, r = 0, len(s)-1

    #     while l < r:
    #         while l < r and not self.alphanum(s[l]):
    #             l += 1
    #         while r > l and not self.alphanum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l+1, r-1
        
    #     return True
    
    # def alphanum(self, c):
    #     return (
    #         (ord('A') <= ord(c) <= ord('Z')) or
    #         (ord('a') <= ord(c) <= ord('z')) or
    #         (ord('0') <= ord(c) <= ord('9'))
    #     )




        # nospace =  ("".join(filter(str.isalnum, s))).lower()
        # return nospace == nospace[::-1]
