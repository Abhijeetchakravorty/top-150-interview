class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
        
    #     repeats = dict()  #create a dictionary
    #     start = longest = 0 #setting pointers at start

    #     for i, char in enumerate(s): # looping through all elements
    #         print("Char: ", char) 
    #         if char in repeats and repeats[char] >= start: #checking if char in dict and char index is greater than equal to staart
    #             start = repeats[char] + 1 #setting start as the next character of the repeat char
                    
    #         repeats[char] = i #setting each character in the dictionary

    #         # if longest < i - start + 1: # checking if longest is less than current index - 
    #         #     longest = i - start + 1
    #         longest = max(longest, i-start+1)
                
        
    #     return longest

        


    def lengthOfLongestSubstring(self, s):
        char = dict()
        longest = start = 0
        for i, v in enumerate(s):
            if v in char and char[v] >= start:
                start = char[v]+1

            char[v] = i
            longest = max(longest, i-start+1)
        return longest


            

        


a = Solution()
b = a.lengthOfLongestSubstring("dvdf")
print(b)

b = a.lengthOfLongestSubstring("pwwkew")
print(b)

b = a.lengthOfLongestSubstring(" ")
print(b)