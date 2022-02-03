#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const request = require('request');
const argv = process.argv;
const movieID = argv[2];
const url = `https://swapi.co/api/films/${movieID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    try {
      const respbody = JSON.parse(body);
      for (const i of respbody.characters) {
        request(i, (errorChar, responseChar, bodyChar) => {
          if (error) {
            console.error('error:', errorChar);
          } else {
            try {
              const charBody = JSON.parse(bodyChar);
              console.log(charBody.name);
            } catch (error) {
              console.error('error:', error);
            }
          }
        });
      }
    } catch (err) {
      console.error('error:', err);
    }
  }
});
