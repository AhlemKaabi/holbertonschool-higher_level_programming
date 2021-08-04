#!/usr/bin/node

const Rectangle = require('./2-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.size = size;
  }

  print () {
    for (let j = 0; j < this.size; j++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  double () {
    this.size = this.size * 2;
  }

  rotate () {
    this.size = this.size;
  }
}
module.exports = Square;
