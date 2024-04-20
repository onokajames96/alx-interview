#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const characterURLs = JSON.parse(body).characters;
  exactOrder(characterURLs, 0);
});
const exactOrder = (characterURLs, x) => {
  if (x === characterURLs.length) return;
  request(characterURLs[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(characterURLs, x + 1);
  });
};
