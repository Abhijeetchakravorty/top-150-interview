var isValid = function (s) {
    const obj = {
        "}": "{",
        ")": "(",
        "]": "[",
    };
    const stack = [];

    for (const i of s) {
        if (i in obj) {
            let bracket = stack.pop();
            if (obj[i] !== bracket) {
                return false;
            }
        } else {
            stack.push(i);
        }
    }
    return stack.length > 0 ? false : true;
};

console.log("Is Valid: ", isValid("()[]{}"));
