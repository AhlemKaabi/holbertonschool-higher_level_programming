#!/usr/bin/node
const fs = require('fs');
if (process.argv.length === 4) {
  fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
    if (err) throw err;
  });
}
