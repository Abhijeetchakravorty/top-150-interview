class Solution:
    def validParantheses(self, s):
        lst = []
        newdict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        left = "({["
        for i in s:
            if i in left:
                lst.append(newdict[i])
            elif len(lst) > 0 and lst[-1]==i:
                lst.pop()
            else:
                return False
        return not lst
        