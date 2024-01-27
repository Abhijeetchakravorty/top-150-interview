var topKFrequent = function (nums, k) {
    let arr = [];
    let finalArr = [];
    let obj = {};
    for (let i = 0; i < nums.length + 1; i++) {
        if (i < nums.length)
            obj[nums[i]] = obj[nums[i]] !== undefined ? obj[nums[i]] + 1 : 1;
        arr.push([]);
    }

    for (let k in obj) {
        // consolelog(obj[k]);
        arr[obj[k]].push(k);
    }
    for (let m = arr.length - 1; m >= 0; m--) {
        if (arr[m].length != 0) {
            for (let g = 0; g < arr[m].length; g++) {
                if (k != 0) {
                    finalArr.push(arr[m][g]);
                    k -= 1;
                } else {
                    break;
                }
            }
        }
    }

    return finalArr;
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));

console.log(topKFrequent([3, 0, 1, 0], 2));
