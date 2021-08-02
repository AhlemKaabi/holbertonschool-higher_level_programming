#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
function factorial (number) {
  if (number < 0) {
    return (-1);
  } else if (number === 0 || isNaN(number)) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(arg1));
