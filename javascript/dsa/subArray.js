"use strict";
var checkIfSubArr = function (arr, subarr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === subarr[0]) {
            let startIndex = i;
            let l = 0;
            let r = subarr.length - 1;
            while (
                l <= r &&
                startIndex < arr.length &&
                arr[startIndex] === subarr[l]
            ) {
                l += 1;
                startIndex += 1;
            }
            if (l === subarr.length) {
                return true;
            }
        }
    }
    return false;
};
console.log(checkIfSubArr([2, 3, 0, 5, 1, 1, 2], [3, 0, 5, 1]));

console.log(checkIfSubArr([3, 4, 5, 1, 2, 7], [4, 1, 2]));
