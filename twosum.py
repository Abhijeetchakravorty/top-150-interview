class Solution:
    def twoSum(self, nums, target: int):
        ## Sample Input: nums = [2,11,15,7], target = 9
        numMap = dict()                         # dictionary ---> Object          
        for i in range(len(nums)):              # We start a loop
            complement = target - nums[i]       # We get the second number from here which is required
            if complement in numMap:            # We check if the second number is present in the dictionary or not
                return [numMap[complement], i]  # We are returning the index of the complement and the current index as it is the second number
            numMap[nums[i]] = i                 # We set the key as the array value and the value we set as the index

### STEP 1: CREATE AN OBJECT
### STEP 2: LOOP THROUGH ARRAY
### STEP 3: FIND THE SECOND NUMBER FOR EACH ELEMENT
### STEP 4: FIND THE SECOND NUMBER IN AN OBJECT
### STEP 5: IF FOUND RETURN THE CURRENT INDEX AND THE SECOND NUMBER INDEX FROM THE OBJECT
### STEP 6: SET ELEMENT IN THE OBJECT AS IT'S KEY AND THE INDEX AS IT'S VALUE

## nums --> 4-1 = 3
## nums --> 
 