class Solution:
    def convertToColumnNumber(self, columnTitle):
        a_z = "0ABCDEDFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for i in range(len(columnTitle)):
            ans *= 26
            ans += a_z.index(columnTitle[i])
        return ans