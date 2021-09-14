#!/usr/bin/node
const request = require('request');
let CharUrl;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  for (CharUrl in content.characters) {
    const request = require('request');
    request(content.characters[CharUrl], function (error, response, body) {
      if (error) throw error;
      const content2 = JSON.parse(body);
      console.log(content2.name);
    });
  }
});
