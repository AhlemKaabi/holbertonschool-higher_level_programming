#!/usr/bin/node
let arg1 = parseInt(process.argv[2]);
let result = arg1;
if (arg1 === 0 || arg1 === 1 || arg1 === null || process.argv[2] === null) {
  console.log(1);
}
while (arg1 > 1) {
  arg1--;
  result = result * arg1;
}
console.log(result);
