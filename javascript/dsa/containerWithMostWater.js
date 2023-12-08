var maxArea = function (height) {
    let l = 0;
    let r = height.length - 1;
    let maxArea = 0;
    while (l < r) {
        let currArea = Math.min(height[l], height[r]) * (r - l);
        maxArea = Math.max(currArea, maxArea);

        if (height[l] < height[r]) {
            l += 1;
        } else {
            r -= 1;
        }
    }
    return maxArea;
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
