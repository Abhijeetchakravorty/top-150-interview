var threeSumClosest = function (nums, target) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let closestSum = Infinity;

    for (let i = 0; i < n - 2; i++) {
        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const currentSum = nums[i] + nums[left] + nums[right];

            if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
                closestSum = currentSum;
            }

            if (currentSum < target) {
                left++;
            } else if (currentSum > target) {
                right--;
            } else {
                return closestSum;
            }
        }
    }

    return closestSum;
};

console.log(threeSumClosest([-1, 2, 1, -4], 1));
console.log(threeSumClosest([1, 1, 1, 0], -100));
