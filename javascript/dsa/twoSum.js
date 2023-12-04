var twoSum = function (nums, target) {
    const dict = {};
    for (let j = 0; j < nums.length; j++) {
        let complement = target - nums[j];
        if (complement in dict) {
            return [dict[complement], j];
        }
        dict[nums[j]] = j;
    }
    return [];
};

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 3], 6));
