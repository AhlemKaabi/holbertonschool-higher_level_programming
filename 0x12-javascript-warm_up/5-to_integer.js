#!/usr/bin/node
const args = process.argv;
const MyNumber = parseInt(args[2], 10);
if (args[2] == null) {
  console.log('Not a number');
} else if (isNaN(MyNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + MyNumber);
}
