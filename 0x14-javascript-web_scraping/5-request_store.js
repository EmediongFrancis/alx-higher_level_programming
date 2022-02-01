#!/usr/bin/node
// Gets the contents of a webpage and
// stores it in a file.

const request = require('request');
const argv = process.argv;
const file = argv[3];
const url = argv[2];
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body);
    fs.writeFile(file, respBody, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
