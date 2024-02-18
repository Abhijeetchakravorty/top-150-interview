var containsDuplicate = function (arr) {
    return arr.length > new Set(arr).size;
};

console.log("Contains Duplicate: ", containsDuplicate([1, 2, 3, 4, 5, 4, 5]));

var validAnangram = function (s, t) {
    const obj1 = {};
    const obj2 = {};
    if (s.length !== t.length) {
        return false;
    }
    for (let j = 0; j < s.length; j++) {
        if (obj1[s[j]] == undefined) {
            obj1[s[j]] = 1;
        }

        if (obj2[t[j]] == undefined) {
            obj2[t[j]] = 1;
        }

        obj1[s[j]] += 1;
        obj2[t[j]] += 1;
    }

    for (let k in obj1) {
        if (obj1[k] !== obj2[k]) {
            return false;
        }
    }
    return true;
};

console.log(validAnangram("anagrama", "pnagaram"));

var twoSum = function (nums, target) {
    const hashMap = {};
    for (let j = 0; j < nums.length; j++) {
        let complement = target - nums[j];
        if (complement in hashMap) {
            return [hashMap[complement], j];
        }
        hashMap[nums[j]] = j;
    }
    return [];
};

console.log(twoSum([2, 7, 11, 15], 9));

var groupAnagram = function (strs) {
    const obj = {};
    for (let k = 0; k < strs.length; k++) {
        let strArr = new Array(26).fill(0);
        let alphabet = "a";
        for (let s = 0; s < strs[k].length; s++) {
            strArr[strs[k][s].charCodeAt(0) - alphabet.charCodeAt(0)] += 1;
        }
        let objKey = strArr.join(",");
        console.log(objKey);
        if (obj[objKey] == undefined) {
            obj[objKey] = [];
        }
        obj[objKey].push(strs[k]);
    }
    return Object.values(obj);
};

console.log(groupAnagram(["bdddddddddd", "bbbbbbbbbbc"]));

var topKFrequent = function (nums, k) {
    const arr = [];
    const final = [];
    const obj = {};
    for (let k = 0; k < nums.length + 1; k++) {
        arr.push([]);
    }

    for (let m = 0; m < nums.length; m++) {
        if (obj.hasOwnProperty(nums[m])) {
            obj[nums[m]] += 1;
        } else {
            obj[nums[m]] = 1;
        }
    }

    Object.entries(obj).forEach((k, v) => {
        arr[k[1]].push(Number(k[0]));
    });

    for (let n = arr.length - 1; n > -1; n--) {
        if (k !== 0) {
            for (let h = 0; h < arr[n].length; h++) {
                if (k !== 0) {
                    final.push(arr[n][h]);
                    k -= 1;
                } else {
                    break;
                }
            }
        } else {
            break;
        }
    }
    return final;
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
