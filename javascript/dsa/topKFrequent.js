// top k frequent elements
var topKFrequent = function (nums, k) {
    const arr = [];
    const obj2 = {};
    for (let i = 0; i < nums.length + 1; i++) {
        arr.push([]);
    }

    for (let i of nums) {
        if (!obj2[i]) {
            obj2[i] = 1;
        } else {
            obj2[i] += 1;
        }
    }

    for (const n in obj2) {
        arr[obj2[n]].push(n);
    }

    const finalArr = [];

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
