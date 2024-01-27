var groupAnagram = function (strs) {
    const dict = {};
    const allChars = {
        a: 0,
        b: 1,
        c: 2,
        d: 3,
        e: 4,
        f: 5,
        g: 6,
        h: 7,
        i: 8,
        j: 9,
        k: 10,
        l: 11,
        m: 12,
        n: 13,
        o: 14,
        p: 15,
        q: 16,
        r: 17,
        s: 18,
        t: 19,
        u: 20,
        v: 21,
        w: 22,
        x: 23,
        y: 24,
        z: 25,
    };
    for (let j = 0; j < strs.length; j++) {
        const arr = new Array(26).fill(0);
        for (let s = 0; s < strs[j].length; s++) {
            arr[allChars[strs[j][s]]] += 1;
        }
        if (
            !dict[JSON.stringify(arr)] ||
            dict[JSON.stringify(arr)].length === 0
        ) {
            dict[JSON.stringify(arr)] = [];
        }
        dict[JSON.stringify(arr)].push(strs[j]);
    }
    return Object.values(dict);
};

console.log(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]));
