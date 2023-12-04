"use strict";
var encode = function (string) {
    let res = "";
    for (let i = 0; i < string.length; i++) {
        if (i === 0) res += string[i];
        if (i !== 0) res += "#" + string[i];
    }
    return res;
};

var decode = function (string) {
    let l = 0;
    let r = string.length - 1;
    const arr = [];
    while (l <= r) {
        let res = "";
        while (string[l] != "#" && l <= r) {
            res += string[l];
            l += 1;
        }
        arr.push(res);
        res = "";
        l += 1;
    }
    return arr;
};

var encodedStr = encode(["abhijeetchakravorty", "neet", "code"]);
console.log(encodedStr);
var decodeStr = decode(encodedStr);
console.log(decodeStr);
