class Solution:
    def mergeSortedArr(self, nums1, m, nums2, n):
        i=m
        j=n
        k=m+n-1

        while j>=0:
            if(i>=0 and nums1[i]>nums2[j]):
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        
        

