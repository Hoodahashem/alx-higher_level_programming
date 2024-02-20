#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');
const toWrite = process.argv[3];

fs.writeFile(file, toWrite, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
