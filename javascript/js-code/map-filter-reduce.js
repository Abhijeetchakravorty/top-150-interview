const numbers = [1, 2, 3, 4, 5, 6];
const squaredNumbers = numbers.map((num) => num * num);
const filteredNumbers = numbers.filter((num) => num % 2 == 0);
const sumNumbers = numbers.reduce((num, accumulator) => num + accumulator, 0);

console.log(squaredNumbers, filteredNumbers, sumNumbers);
