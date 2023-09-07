class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={} #empty object
        def dfs(i,j): #depth first search function
            print(i, j)
            if (i,j) in cache: #checking if parameters exists in object
                return cache[(i,j)] # returning cache i, j along with its index
            
            if i>=len(s) and j>=len(p): #checking if i is greater than equal to len(s) and j is greater than equal to len(p)
                return True #returning true
            if j>=len(p): #check if only j is greater than len(p)
                return False # return false
            
            match = i<len(s) and (s[i]==p[j] or p[j]==".") #i less than len(s) and (s[i]==p[j] or p[j]==".")
            if (j+1)<len(p) and p[j+1]=="*": #if j+1 is less than len(p) and p[j+1] is equal to '*'
                cache[(i,j)]=(dfs(i,j+2) or (match and dfs(i+1,j))) 
                return cache[(i,j)]
            if match:
                cache[(i,j)]=dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)]=False
            return False
        return dfs(0,0)


a = Solution()
b = a.isMatch("aa", "a*")
# b = a.isMatch("aa", "aa")
print(b)