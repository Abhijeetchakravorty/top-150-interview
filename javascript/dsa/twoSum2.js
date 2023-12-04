var twoSum = function (numbers, target) {
    l = 0;
    r = numbers.length - 1;
    while (l <= r) {
        let curSum = numbers[l] + numbers[r];
        if (curSum > target) {
            r -= 1;
        }

        if (curSum < target) {
            l += 1;
        }

        if (curSum == target) {
            return [l + 1, r + 1];
        }
    }
    return [];
};

// console.log(twoSum([2, 7, 11, 15], 9));
