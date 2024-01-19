var secondLargestWord = function (s) {
    // Find max word
    let arr = s.split(" ");
    let finalArr = [];
    let maxCount = 0;
    for (let j = 0; j < arr.length; j++) {
        maxCount = Math.max(maxCount, arr[j].length);
    }
    let obj = {};
    for (let m = 1; m < maxCount + 1; m++) {
        obj[m] = [];
    }

    for (let k = 1; k < arr.length; k++) {
        obj[arr[k].length].push(arr[k]);
    }

    for (let n = arr.length + 1; n > 0; n--) {
        for (let g = 0; g < obj[n.toString()].length; g++) {
            if (finalArr.length == 2) {
                return finalArr[finalArr.length - 1];
            }
            finalArr.push(obj[n.toString()][g]);
        }
    }
    return finalArr[finalArr.length - 1] ? undefined : "";
};

console.log(secondLargestWord("A very good morning to you"));
