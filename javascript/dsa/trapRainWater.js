var trap = function (height) {
    if (!height) return 0;

    let res = 0;
    let l = 0;
    let r = height.length - 1;
    let leftMax = height[0];
    let rightMax = height[r];

    while (l < r) {
        if (leftMax < rightMax) {
            l += 1;
            leftMax = Math.max(height[l], leftMax);
            res += leftMax - height[l];
        } else {
            r -= 1;
            rightMax = Math.max(height[r], rightMax);
            res += rightMax - height[r];
        }
    }
    return res;
};

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
