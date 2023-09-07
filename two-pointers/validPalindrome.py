class Solution:
    def valid(self, s):
        nospace = ("".join(filter(str.isalnum, s))).lower()
        return nospace == nospace[::-1]




        # nospace =  ("".join(filter(str.isalnum, s))).lower()
        # return nospace == nospace[::-1]
