class Solution:
    def findUniChar(self, s):
        ans = 10**5
        a_z = "abcdefghijklmnopqrstuvwxyz"

        for c in a_z:
            idx = s.find(c)
            if idx != -1 and idx == s.rfind(c):
                ans = min(idx, ans)
                break
        return ans if ans < 10**5 else -1
