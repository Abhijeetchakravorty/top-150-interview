#Given: reverse words in a string and the word should not get reversed
#ToDo: reverse the word
#Edge case: remove any trailing spaces and extra spaces between words 
# Input: s = "  the sky   is blue  "
# Output: "blue is sky the"
class Solution:
    def reverseWordsInAString1(self, s):
        s = s.strip().split()
        s = " ".join(s[::-1])
        return s

a = Solution()
b = a.reverseWordsInAString1("    a good   example    ")