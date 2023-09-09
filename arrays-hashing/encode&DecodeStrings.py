class Solution:
    def encode(self, strs):
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i]))+"#"+strs[i]
        return res
    
    def decode(self, string):
        res, i = [], 0
        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            print("I:J", i, j, length, string[i:j])
            res.append(string[j+1:j+1+length])
            i = j+1+length
        return res

            
 

a = Solution()
b = a.encode(["abhijeetchakravorty", "neet", "code"])
print(b)
c = a.decode(b)
print(c)