/*
To do: Given an integer array nums, 
    return all the triplets 
    [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.
*/
var threeSum = function (nums) {
    // console.log(nums);
    const arr = [];
    for (let i = 0; i < nums.length; i++) {
        // console.log(nums[i]);
        let l = i + 1;
        let r = nums.length - 1;
        while (l <= r) {
            let curSum = nums[i] + nums[l] + nums[r];
            if (curSum > 0) {
                r -= 1;
            }

            if (curSum < 0) {
                l += 1;
            }
            if (curSum === 0) {
                arr.push([nums[i], nums[l], nums[r]]);
            }
        }
    }
    return arr;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
