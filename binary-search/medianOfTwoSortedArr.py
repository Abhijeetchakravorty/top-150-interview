class Solution:
    def findMedianSortedArray(self, nums1, nums2):
        # Time Complexity: O(log(min(len(nums1), len(nums2))))
        # Space Complexity: O(1)

        # Ensure B is the longer array to simplify binary search
        A, B = nums1, nums2

        # Calculate the total length of the combined arrays
        total = len(nums1) + len(nums2)

        # Calculate the index representing the middle point of the combined arrays
        half = total // 2

        # Ensure B is the longer array to simplify binary search
        if len(B) < len(A):
            A, B = B, A
        
        # Initialize pointers for binary search within the longer array A
        l, r = 0, len(A) - 1

        # Binary search loop
        while True:
            # Calculate the midpoint index in array A
            i = (l+r) // 2

            # Calculate the corresponding index in array B based on the middle point
            j = half - i - 2

            # Determine values of elements around midpoints in both arrays
            Aleft = A[i] if (i >= 0) else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if (j >= 0) else float("-infinity")
            Bright = B[j+1] if (j+1)  < len(B) else float("infinity")

            # Check if the current partition is valid for finding the median
            if Aleft <= Bright and Bleft <= Aright:
                # Check if the total number of elements is odd
                if total % 2:
                    # Return the smaller of the two rightmost elements if the total is odd
                    return min(Aright, Bright)
                else:
                    # Return the average of the maximum left element and minimum right element if the total is even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # Adjust the search range in array A if the partition is not valid
                r = i - 1
            else:
                # Adjust the search range in array A if the partition is not valid in the opposite direction
                l = i + 1

# Create an instance of the Solution class
a = Solution()

# Call the findMedianSortedArrays method with two example arrays
b = a.findMedianSortedArrays([1, 2, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8])

# Print the result, which is the median of the combined sorted arrays
print(b)
