#!/usr/bin/node
const args = process.argv;
if (args[2] != null) {
  let arg2 = parseInt(args[2]);
  if (!(isNaN(arg2))) {
    while (arg2 - 1 >= 0) {
      console.log('C is fun');
      arg2--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
