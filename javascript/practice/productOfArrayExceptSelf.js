var productOfArray = function (nums) {
    var prefix = 1;
    var postfix = 1;
    var res = new Array(nums.length).fill(1);
    for (let k = 0; k < nums.length; k++) {
        res[k] = prefix;
        prefix *= nums[k];
    }

    for (let g = nums.length - 1; g >= 0; g--) {
        res[g] *= postfix;
        postfix *= nums[g];
    }

    return res;
};

console.log(productOfArray([1, 2, 3, 4]));
