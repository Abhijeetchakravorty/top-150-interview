var groupAnagrams = function (strs) {
    const dict = {};
    for (let i = 0; i < strs.length; i++) {
        const chars = Array(26).fill(0);
        for (let j = 0; j < strs[i].length; j++) {
            const charCode = strs[i][j].charCodeAt(0) - "a".charCodeAt(0);
            chars[charCode] += 1;
        }
        // Use the character count array as a key directly
        const key = chars.join(",");

        if (dict[key] === undefined) {
            dict[key] = [];
        }

        dict[key].push(strs[i]);
    }
    return Object.values(dict);
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
