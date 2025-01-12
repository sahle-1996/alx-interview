#!/usr/bin/node

// A script that retrieves and prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characterUrls = JSON.parse(body).characters;

  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  };

  (async () => {
    for (const url of characterUrls) {
      try {
        const name = await fetchCharacterName(url);
        console.log(name);
      } catch (err) {
        console.error(err);
      }
    }
  })();
});
