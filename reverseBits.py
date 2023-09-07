class Solution:
    def reverseBits(self, num):
        a = str(bin(num).split('b')[-1]).zfill(32)
        b = a[::-1]
        return int(b, 2)