/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
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
    const charOne = Array(26).fill(0);
    const charTwo = Array(26).fill(0);
    // console.log(charOne, charTwo);
    l = 0;
    r = s.length;
    for (let i = 0; i < s.length; i++) {
        charOne[allChars[s[i]]] += 1;
        charTwo[allChars[t[i]]] += 1;
    }

    for (let j = 0; j < charOne.length; j++) {
        if (charOne[j] !== charTwo[j]) {
            return false;
        }
    }
    return true;
};

console.log(isAnagram("anagram", "nagaram"));
