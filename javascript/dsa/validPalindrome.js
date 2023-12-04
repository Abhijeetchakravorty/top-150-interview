var isPalindrome = function (s) {
    if (s.trim().length === 0 || s.trim().length === 1) return true;
    let l = 0;
    let r = s.length - 1;
    while (l <= r) {
        while (l <= r && !/^[a-zA-Z0-9]+$/.test(s[l])) {
            l += 1;
        }

        while (l <= r && !/^[a-zA-Z0-9]+$/.test(s[r])) {
            r -= 1;
        }

        if (l <= r && s[l].toLowerCase() !== s[r].toLowerCase()) {
            return false;
        }
        l += 1;
        r -= 1;
    }
    return true;
};

// console.log(isPalindrome(`A man, a plan, a canal: Panama`));

// console.log(isPalindrome(`race a car`));

console.log(isPalindrome(".,"));
