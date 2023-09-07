# class Solution:
#     def topKFrequentElements(self, nums, k):
#         count = {}                                  #creating an empty dictionary
#         freq = [[] for i in range(len(nums)+1)]     #creating empty arrays based on the number of elements + 1

#         for n in nums:                              #iterating over the array elements
#             count[n] = 1+count.get(n, 0)            #setting each value of nums in dictionary as key and assiging it a counter
        
#         for n, c in count.items():                  #iterating over the dictionary
#             print("n:c", n, c)      
#             freq[c].append(n)                       #setting index which is considered as count is being added with the actual element

#         res = []                                    #creating an empty array
#         for i in range(len(freq)-1, 0, -1):         #we start iterating the freq array from behind and iterating till the n-1 element
#             for n in freq[i]:                       #for each freq array we start another loop
#                 print(n)
#                 res.append(n)                       #we add n in res array
#                 if len(res) == k:                     #we check if the len of the final array has the number of elements equal to k
#                     return res                      #return res


# a = Solution()
# b = a.topKFrequentElements([1,1,1,2,2,3], 2)








class Solution:
    def topKFrequentElements(self, nums, k):
        freq = [[] for j in range(len(nums)+1)]
        item = dict()
        res = []
        for n in nums:
            item[n] = 1 + item.get(n, 0)
        # print(item)
        for k, v in enumerate(item):
            freq[v].append(k)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


a = Solution()
b = a.topKFrequentElements([1,1,1,2,2,3], 2)
print(b)










































