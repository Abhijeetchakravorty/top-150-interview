class Solution:
    def encode(self, strs):
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i]))+"#"+strs[i]
        return s

    def decode(self, string):
        res, i = [], 0
        while i < len(string):
            j = string.index("#", i)
            length = int(string[i:j])
            res.append(string[j+1:j+1+length])
            i = j+1+length
        return res


a = Solution()

b = a.encode(["abcd", "abcd1", "abcd2"])
print("B: ", b)

c = a.decode(b)
print("C: ", c)