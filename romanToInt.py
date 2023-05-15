class Solution:
    def romanToInt(self, s: str) -> int:
        symbolToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prevValue = symbolToIntDict["M"]
        totalValue = 0
        for c in s:
            currentValue = symbolToIntDict[c]
            if prevValue < currentValue:
                totalValue -= prevValue * 2
            totalValue += currentValue
            prevValue = currentValue
        return totalValue
    