class Solution:
    def twoSum(self, nums, target):
        obj = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                return [nums[complement], i]
            obj[nums[i]] = i
    
    def longestSubString(self, s):
        ans = 0
        leftPointer = 0
        obj = dict()
        for i, val in enumerate(s):
            if val in obj:
                if obj[val]+1>leftPointer:
                    leftPointer = obj[val]+1
            obj[val] = i
            lengthSub = i + 1 - leftPointer
            if ans < lengthSub:
                ans = lengthSub
        
        return ans
    
    def romanToInt(self, s):
        romanToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        totalValue = 0
        prevValue = romanToIntDict["M"]
        for c in s:
            currVal = romanToIntDict[c]
            if prevValue < currVal:
                totalValue -= prevValue * 2
            totalValue += currVal
            prevValue = currVal
        return totalValue
        
    
    def validParenthesis(self, s):
        if s[0] not in ["(", "{", "["]:
            return False
        lst = []
        for bracket in s:
            if bracket in ["(", "{", "["]:
                lst.append(bracket)
            elif(len(lst)==0):
                return False
            else:
                opening = lst.pop()
                if((opening == "(" and bracket == ")") or (opening == "{" and bracket == "}") or (opening == "[" and bracket == "]")):
                    continue
                else:
                    return False
        if (len(lst) == 0):
            return True
        return False