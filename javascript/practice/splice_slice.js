var createASubArray = function (arr) {
    let subArr = arr.slice(1, 4);
    return subArr;
};

console.log(createASubArray([1, 2, 3, 4, 5]));

var createASubSplice = function (arr) {
    arr.splice(1, 0, "orange", "abhijeet");
    return arr;
    const food = ["pizza", "cake", "salad", "cookie"];

    food.splice(1, 0, "burrito");
    return food;
};

console.log(createASubSplice(["a", "b", "c", "d"]));
