var longestConsecutive = function (nums) {
    const newNums = new Set(nums);
    let longest = 0;
    for (n of newNums) {
        if (!newNums.has(n - 1)) {
            let length = 0;
            // while (n+length)
            while (newNums.has(n + length)) {
                length += 1;
            }
            longest = Math.max(length, longest);
        }
    }
    return longest;
};

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
