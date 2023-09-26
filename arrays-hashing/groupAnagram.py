from collections import defaultdict
class Solution:
    def groupAnagram(self, strs):
        #time complexity : O(n * m), 
        # where n is the number of 
        # strings and m is the 
        # maximum length of a 
        # string in the input list.
        
        #space complexity: O(n)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
a = Solution()
b = a.groupAnagram(["eat","tea","tan","ate","nat","bat"])
print(b)