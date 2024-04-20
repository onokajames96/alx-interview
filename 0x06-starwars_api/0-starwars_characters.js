#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const charURLs = JSON.parse(body).characters;
  exactOrder(charURLs, 0);
});
const exactOrder = (charURLs, x) => {
  if (x === charURLs.length) return;
  request(charURLs[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(charURLs, x + 1);
  });
};
