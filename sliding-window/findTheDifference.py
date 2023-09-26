class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for i, v in enumerate(s):
            hashmap[v] = 1+hashmap.get(v, 0)
        
        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            else:
                return i
        
        for j in hashmap:
            if hashmap[j] < 0 or hashmap[j] == 1:
                return j
        