class Solution:
        def plusOne(self, digits):
                s = [str(i) for i in digits]
                return map(int, str(int("".join(s))+1))