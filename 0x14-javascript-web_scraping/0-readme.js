#!/usr/bin/node

// take the file path as argument
if (process.argv.length === 3) {
  const fs = require('fs');

  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
