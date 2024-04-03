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

    def productOfArrayExceptSelf(self, nums):
        prefix = 1
        postfix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res

    def validSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        group = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in group[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                group[(r // 3, c // 3)].add(board[r][c])
        return True

    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

    def consecutiveNums(self, nums):
        maxLength = 0
        num_set = set(nums)
        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength

    def isPalindrome(self, string):
        l, r = 0, len(string) - 1
        while l < r:

            while l < r and not string[l].isalnun():
                l += 1

            while l < r and not string[r].isalnum():
                r -= 1

            if string[l] != string[r]:
                return False

            l += 1
            r -= 1

        return True

    def twoSum2(self, nums, target):
        pass

    def threeSum(self, nums, target):
        pass

    def maxArea(self, nums):
        pass

    def trapWater(self, nums):
        pass

    def validParanthesis(self, s):
        pass

    def minStack(self, nums):
        pass

    def rpn(self, string):
        pass

    def generateParanthesis(self, n):
        pass

    def temperature(self, temp):
        pass

    def carFleet(self, nums):
        pass

    def maxHorizontalArea(self, nums):
        pass

    def binarySearch(self, nums):
        pass

    def findIn2DMatrix(self, nums):
        pass

    def minEatingSpeed(self, piles, h):
        pass

    def findMinInRotatedSortedArray(self, nums):
        pass

    def searchInRotatedSortedArray(self, nums):
        pass

    def medianOfTwoSortedArray(self, arr1, arr2):
        pass

    def maxProfit(self, prices):
        pass

    def lengthOfLongestSubstring(self, s):
        repeats = dict()
        start = longest = 0

        for i, char in enumerate(s):
            if char in repeats and repeats[char] >= start:
                start = repeats[char] + 1
            repeats[char] = i

            longest = max(longest, i - start + 1)

        return longest

    def characterReplacement(self, s, k):
        counts = {}
        maxf = 0
        l = 0
        for r, ch in enumerate(s):
            counts[ch] = 1 + counts.get(ch, 0)
            maxf = max(maxf, counts[ch])
            if r - l + 1 - maxf > k:
                counts[s[l]] -= 1
                l += 1

        return len(s) - l


a = Solution()
b = a.lengthOfLongestSubstring("au")
print(b)
