from collections import defaultdict
class Solution:
    def groupAnagram(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                print(c, count)
                print("\n")
            res[tuple(count)].append(s)
            print(res)
        return res.values()



            
        

a = Solution()
b = a.groupAnagram(["eat","tea","tan","ate","nat","bat"])
print(b)