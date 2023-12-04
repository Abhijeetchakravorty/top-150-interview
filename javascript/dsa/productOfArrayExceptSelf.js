var productExceptSelf = function (nums) {
    let prefix = 1;
    let postfix = 1;
    let res = Array(nums.length).fill(1);
    for (let j = 0; j < nums.length; j++) {
        res[j] = prefix;
        prefix *= nums[j];
    }

    console.log(res);

    for (let k = nums.length - 1; k >= 0; k--) {
        res[k] *= postfix;
        postfix *= nums[k];
    }

    // console.log(res);
    return res;
};

console.log(productExceptSelf([1, 2, 3, 4]));
