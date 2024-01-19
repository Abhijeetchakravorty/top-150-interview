var validPalindrome = function (s) {
    let arr = s.split("");
    let obj = {};

    if (s === arr.reverse().join("")) {
        return true;
    }

    for (let i = 0; i < arr.length; i++) {
        let tempArr = arr.slice();
        tempArr.splice(i, 1);
        obj["0"] = tempArr.join("");
        let tempArr2 = tempArr.slice();
        obj["1"] = tempArr2.reverse().join("");
        if (obj["0"] === obj["1"]) {
            return true;
        }
    }
    return false;
};

console.log(validPalindrome("aba"));
