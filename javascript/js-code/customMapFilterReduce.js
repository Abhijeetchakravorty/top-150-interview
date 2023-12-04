const arr = [1, 2, 3, 4, 5];

const updateArr = arr.map(function (data, i, arrr) {
    //   console.log(data, i, arrr);
    return data * data;
});
// console.log(updateArr)
// A custom map
Array.prototype.customMap = function (callback) {
    const resultArr = [];
    for (let i = 0; i < this.length; i++) {
        const result = callback(this[i], i, this);
        resultArr.push(result);
    }
    return resultArr;
};
// a custom filter
Array.prototype.customFilter = function (callback) {
    const resultArr = [];
    for (let i = 0; i < this.length; i++) {
        const result = callback(this[i], i, this);
        if (result) resultArr.push(result);
    }
    return resultArr;
};

// a custom reduce
Array.prototype.customReduce = function (callback, initialValue) {
    let accumulator = initialValue !== undefined ? initialValue : this[0];
    const startIndex = initialValue !== undefined ? 0 : 1;
    for (let i = startIndex; i < this.length; i++) {
        // Apply the callback function to the accumulator and the current element
        accumulator = callback(accumulator, this[i], i, this);
    }
    return accumulator;
};

const newUpdateMap = updateArr.customMap(function (data) {
    return data * data;
});

const newFilterMap = updateArr.customFilter(function (data) {
    if (data % 2 == 0) {
        return data;
    }
});
const newReduce = updateArr.customReduce(function (accumulator, data) {
    return accumulator + data;
}, 0);

console.log(newUpdateMap, newFilterMap, newReduce);

console.log("this: ", this);
this.newData = 10;
const data = (a, b) => {
    console.log("inside arrow: ", this);
    return a + b;
};

console.log(data(10, 12));
