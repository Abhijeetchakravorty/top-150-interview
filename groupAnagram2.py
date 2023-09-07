from collections import defaultdict
class Solution:
    def groupAnagram(self, strs):
        res = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord("a")] += 1
            res[tuple(count)].append(i)
        return res.values()
a = Solution()
b = a.groupAnagram(["eat","tea","tan","ate","nat","bat", "tae"])
print(b)