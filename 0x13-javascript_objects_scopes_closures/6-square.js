#!/usr/bin/node
const SquareClass = require('./5-square.js');

class Square extends SquareClass {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let j = 0; j < this.width; j++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log('');
    }
  }
}
module.exports = Square;
