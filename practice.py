from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(s[i]):
                return False
        return True

    def twoSum(self, nums, target):
        dictMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictMap:
                return [dictMap[complement], i]
            dictMap[nums[i]] = i
        return []

    def groupAnagram(self, strs):
        ans = defaultdict(list)  # This is a bit crucial
        for i in strs:
            count = [0] * 26
            for s in i:
                count[ord(s) - ord(i)] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def topKFrequent(self, nums, k):
        res = []
        ans = []
        obj = dict()
        for i in range(len(nums)):
            if str(nums[i]) not in obj:
                obj[str(nums[i])] = 0
            obj[str(nums[i])] += 1
            ans.append([])
        ans.append([])

        for key, val in obj.items():
            ans[int(val)].append(key)
        for j in range(len(ans) - 1, 0, -1):
            if k > 0:
                for i in range(len(ans[j])):
                    if k > 0:
                        res.append(int(ans[j][i]))
                        k -= 1
                    else:
                        break
            else:
                break
        return res


a = Solution()
b = a.topKFrequent([1], 1)
print(b)
