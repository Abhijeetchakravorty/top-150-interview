var sortData = function (arr1, arr2) {
    const arr = [...new Set([...new Set(arr1), ...new Set(arr2)])];
    arr.sort((a, b) => {
        return a - b;
    });
    return arr;
};

console.log(
    sortData(
        [1, 5, 2, 7, 4, 2, 1, 0, 1, 3, 3, 9, 15, 10, 21, 11, 28, 12, 29, 13],
        [1, 5, 2, 7, 4, 2, 1, 0, 1, 3, 3, 9, 15, 10, 21, 11, 28, 12, 29, 13]
    )
);
