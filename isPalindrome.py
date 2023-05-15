class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_striped_s = [c for c in s.lower() if c.isalnum()]
        backward_striped_s = forward_striped_s[::-1]
        return forward_striped_s == backward_striped_s
    
a = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(a)