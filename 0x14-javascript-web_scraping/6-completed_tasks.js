#!/usr/bin/node
const request = require('request');
const data = {};
let task = 0;
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  for (task in content) {
    if (!(content[task].userId in data)) {
      data[content[task].userId] = 0;
      if (content[task].completed === true) {
        data[content[task].userId] += 1;
      }
    } else {
      if (content[task].completed === true) {
        data[content[task].userId] += 1;
      }
    }
  }
  console.log(data);
});
