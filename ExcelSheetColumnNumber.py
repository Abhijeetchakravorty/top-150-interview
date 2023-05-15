class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a_z = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            print(ans)
            ans += a_z.index(columnTitle[i])
        return ans


a = Solution().titleToNumber("BC")