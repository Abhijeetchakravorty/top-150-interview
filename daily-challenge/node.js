const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map(function(val) {
    return val * val;
});
const updateNumbers = numbers.filter(function(val) {
    if (val % 2 == 0) {
        return val;
    }
});
const modifyNumbers = numbers.reduce(function(accumulator, val) {
    return val+accumulator;
});
console.log(squaredNumbers);
console.log(updateNumbers);
console.log(modifyNumbers);
console.log(a, b, c);
var a = 10;
let b = 20;
const c = 30;

