#!/usr/bin/node

const character = 'Wedge Antilles';
const url = process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body);
    const results = allData.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) { count += 1; }
      }
    }
    console.log(count);
  }
});
