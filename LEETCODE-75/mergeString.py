# Given: 2 strings
# ToDo: merge strings byadding letters in alternating order sstarting with w1
# Edge case:  if a string is longer then added remaining words at the end

class Solution:
    def mergeStringAlternatively(self, word1, word2):
        # we can have four pointers
        firstLeft, firstRight = 0, len(word1)-1
        secondLeft, secondRight = 0, len(word2)-1
        # first two pointers on word1
        # next two pointers on word2
        # Then we start a while loop with an and condition for all four pointers
        s = ""
        while firstLeft <= firstRight and secondLeft <= secondRight:
            s += word1[firstLeft]+word2[secondLeft]
            firstLeft += 1
            secondLeft += 1
        
        # When the loop ends check if firstleft pointer has reached end or not if not then add all elements to word
        if firstLeft < firstRight+1:
            s += word1[firstLeft:firstRight+1]
        # next check if secondleft pointer has reached end or not if not then add aall elements to word
        if secondLeft < secondRight+1:
            s += word2[secondLeft:secondRight+1]
        
        print(secondLeft, secondRight)
        return s


a = Solution()
print(a.mergeStringAlternatively('abc', "pqr"))


a = Solution()
print(a.mergeStringAlternatively('ab', "pqrs"))

a = Solution()
print(a.mergeStringAlternatively('abcd', "pq"))

