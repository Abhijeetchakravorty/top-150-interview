var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;
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
    const arrOne = new Array(26).fill(0);
    const arrTwo = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        arrOne[allChars[s[i]]] += 1;
        arrTwo[allChars[t[i]]] += 1;
    }
    return arrOne.join("") === arrTwo.join("");
};

console.log(isAnagram("rat", "car"));
