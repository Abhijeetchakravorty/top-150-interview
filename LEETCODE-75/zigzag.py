# The string "PAYPALISHIRING" is written in a zigzag pattern 
# on a given number of rows like this: (you may want to display 
# this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
class Solution:
    def conversion(self, s, numRows):
        #first we create an empty 2d array
        freq = ["" for i in range(numRows)]
        index = None
        #Then we update our start counter
        counter = 0
        goingDown = True
        #We create two counters one is called start and the other is called end
        #Start will always increase and end will always decrease
        #When start reaches end then end starts working and start is reset
        #When end reaches start then start starts working and end is reset
        
        for indx, c in enumerate(s):
            if len(freq) < counter+1:
                index = indx
                break
            freq[counter] += c
            if goingDown:
                counter += 1
            else:
                counter -= 1

            if counter == numRows-1:
                goingDown = False
            
            if counter == 0:
                goingDown = True
        res = ""
        for j in range(len(freq)):
            res += freq[j]
        
        if index:
            for k in range(index, len(s)):
                res += s[k]

        return res


       

            
        


            
            


a = Solution().conversion("PAYPALISHIRING", 3)
print(a)

a = Solution().conversion("PAYPALISHIRING", 4)
print(a)

a = Solution().conversion("ABC", 1)
print(a)


a = Solution().conversion("AB", 1)
print(a)