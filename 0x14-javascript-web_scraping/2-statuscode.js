#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  // Print the response status code if a response was received
  console.log('code:', response.statusCode);
});
