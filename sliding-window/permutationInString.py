class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity : O(len(s2)) 
        # Space Complexity: O(1)
        if len(s1) > len(s2): return False
        
        
        # Use sliding window technique
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        window_len = len(s1)
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        print(s1_count, "\n", s2_count, "\n")
    
        for j in range(window_len, len(s2)):
            if s1_count == s2_count: return True
            
            s2_count[ord(s2[j-window_len]) - ord('a')] -= 1
            s2_count[ord(s2[j]) - ord('a')] += 1
            print("S2_count After: ", s2_count)
            print("\n")
        return s1_count == s2_count   


a = Solution()
b = a.checkInclusion("ab", "eidbaooo")