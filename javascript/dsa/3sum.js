/*
To do: Given an integer array nums, 
    return all the triplets 
    [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.
*/
var threeSum = function (nums) {
    nums.sort((a, b) => a - b);
    const arr = [];
    for (let [i, a] of nums.entries()) {
        if (i > 0 && a == nums[i - 1]) continue;
        let l = i + 1;
        let r = nums.length - 1;
        while (l < r) {
            let threeSum = a + nums[l] + nums[r];
            if (threeSum > 0) {
                r -= 1;
            } else if (threeSum < 0) {
                l += 1;
            } else {
                arr.push([a, nums[l], nums[r]]);
                l += 1;
                while (nums[l] === nums[l - 1] && l < r) l += 1;
            }
        }
    }
    return arr;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
