const numbers = [1, 2, 3, 4, 5, 6];
const squaredNumbers = numbers
    .map((num) => num * num)
    .filter((num) => num % 2 == 0)
    .reduce((accumulator, num) => num + accumulator, 0);

console.log(squaredNumbers);
