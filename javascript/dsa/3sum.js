/*
To do: Given an integer array nums, 
    return all the triplets 
    [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.
*/
var threeSum = function (nums) {
    nums.sort();
    // console.log(nums);
    const arr = [];
    for (let i = 0; i < nums.length; i++) {
        // console.log(nums[i]);
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        let l = i + 1;
        let r = nums.length - 1;
        while (l <= r) {
            console.log(i, l, r);
            let curSum = nums[i] + nums[l] + nums[r];
            console.log(curSum);
            if (curSum > 0) {
                r -= 1;
            }

            if (curSum < 0) {
                l += 1;
            }
            if (curSum === 0) {
                arr.push([nums[i], nums[l], nums[r]]);
                while (l <= r) {
                    if (nums[l + 1] !== nums[l]) {
                        l += 1;
                    }
                }
            }
        }
    }
    return arr;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
