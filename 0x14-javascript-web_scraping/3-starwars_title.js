#!/usr/bin/node
const { title } = require('process');
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  const content = JSON.parse(body);
  console.log(content.title);
});
