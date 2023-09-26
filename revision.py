class Solution:
    def checkInclusion(self, s1, s2):
        # if len(s1) > len(s2): return False

        # s1Count, s2Count = [0]*26, [0]*26

        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')] += 1
        #     s2Count[ord(s2[i]) - ord('a')] += 1
        
        # matches = 0
        # for i in range(26):
        #     matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # l = 0
        # for r in range(len(s1), len(s2)):
        #     if matches == 26: return True

        #     index = s2[r] - ord('a')
        #     s2Count[index] += 1

        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         matches -= 1


        #     index = s2[l] - ord('a')
        #     s2Count[index] -= 1

        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         matches -= 1

        #     l += 1
        
        # return matches == 26
        if len(s1) > len(s2): return False
        
        
        # Use sliding window technique
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        window_len = len(s1)
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
    
        for j in range(window_len, len(s2)):
            if s1_count == s2_count: return True
            
            s2_count[ord(s2[j-window_len]) - ord('a')] -= 1
            s2_count[ord(s2[j]) - ord('a')] += 1
        return s1_count == s2_count   
        

            
        

a = Solution()
b = a.checkInclusion("abc", "baxyzabc")
print("Ans: ", b)