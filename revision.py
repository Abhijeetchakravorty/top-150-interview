class Solution:
    def topKFrequentElements(self, nums, k):
        freq = [[] for i in range(len(nums)+1)]
        res = []
        hashmap = {}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for c in hashmap:
            freq[hashmap[c]].append(c)

        for i in range(len(freq)-1, 0, -1):
            j = 0
            while j < len(freq[i]):
                if len(res) == k:
                    return res
                res.append(freq[i][j])
                j += 1
        
        return res

a = Solution()
b = a.topKFrequentElements([1, 1, 1, 2, 2, 3], 2)
print("B: ", b)

