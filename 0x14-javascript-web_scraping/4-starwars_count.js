#!/usr/bin/node
const request = require('request');
let count = 0; let film; let char;
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  for (film in content.results) {
    for (char in content.results[film].characters) {
      if (content.results[film].characters[char] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
