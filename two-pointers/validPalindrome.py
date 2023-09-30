class Solution:
    def isPalindrome(self, s):
        # Time Complexity : O(n) #There is no O(log n) solution
        # Space Complexity: O(1) 
        # Initialize two pointers, 
        # one at the beginning and 
        # one at the end of the string
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move the left pointer to the 
            # right while it points to a 
            # non-alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            
            # Move the right pointer to the 
            # left while it points to a 
            # non-alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare the characters (ignoring case)
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers towards the center
            l += 1
            r -= 1
            
        # If we've checked all pairs 
        # of characters and they match, 
        # it's a palindrome
        return True
