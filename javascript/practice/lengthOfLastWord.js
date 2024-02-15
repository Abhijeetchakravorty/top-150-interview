var lengthOfLastWord = function (s) {
    s = s.trim();
    let left = (right = s.length - 1);
    while (left >= 0) {
        console.log(s[left]);
        if (s[left] === " ") {
            break;
        }
        left--;
    }
    return right - left;
};

console.log(lengthOfLastWord("   fly me   to   the moon  "));
